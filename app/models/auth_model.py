import pymysql
from fastapi import HTTPException
from database import basic

class AuthModel():

    async def test(post_data):
        try:
            conn = await basic()
            curs = conn.cursor(pymysql.cursors.DictCursor)

            sql = f'''
                select * from User
            '''
            curs.execute(sql)
            data = curs.fetchall()
            conn.close()
            print(data)

            return True
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})
