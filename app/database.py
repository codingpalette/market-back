import pymysql

# Connect to the database

async def basic():
    try:
        conn = pymysql.connect(
            host='host.docker.internal',
            port=3306,
            user='root',
            password='root',
            db='test',
            charset='utf8'
        )
        return conn
    except Exception as e:
        print(e)
        return False
