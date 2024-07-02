import pymysql

def add_user(user_id, username):
    schema_name = 'aaa'
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='root', passwd='123', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('{username}', {user_id})")

    cursor.close()
    conn.close()
