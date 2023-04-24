#
# import redis
#
# redis_client = redis.Redis(host="localhost", port=6379, db=0)
#
# with redis_client as redis_client:
#     output = StringIO.StringIO()
#     im = Image.open("/ico/maxresdefault.jpg")
#     im.save(output, format=im.format)
#     redis_client.set('imagedata', output.getvalue())

import os

import redis

directory = 'ico/'
client = redis.Redis()

for imeg in os.listdir(directory):
    if imeg.endswith(".jpg"):
        
        im = os.path.join(directory, imeg)
        c = open(im, "rb").read()
        #size = os.stat(im).st_size
        client.set(imeg, c)





# with redis.Redis() as client:
#     while True:
#         a = str(all_imeg)
#         client.set("bild1", a)
