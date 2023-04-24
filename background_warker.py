import datetime
import redis
import psycopg2
import psycopg2.extras


from config import host, user, password, db_name
from psycopg2._psycopg import connection


client = redis.Redis()
get_keys = client.keys()

for i in get_keys:
    decode_name = i.decode(encoding='utf-8')
    get_img = client.get(decode_name)
    size = client.memory_usage(decode_name)
    time = datetime.datetime.now()


    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port="5433"
        )
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
 
            cursor.execute(
                "INSERT INTO redis_im (imege, size, time) VALUES (%s, %s, %s) returning imege", (get_img, size, time)
                
            )
        
            print(f'Запись {cursor.fetchone()}')
            
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
 
            cursor.execute(
                "SELECT * FROM redis_im"
                
            )
        
            print(f'Результат записи {cursor.fetchone()}')
        
    except Exception as _ex:
        print("[INFO] Ошибка при работе с Базой Postgres", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Работа с базой окончена")
        