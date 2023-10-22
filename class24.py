#python -m pip install mysql-connector-python


import mysql.connector

mysql_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345678",
    database="django_class"
)

# print(mysql_db)

mysql_cursor = mysql_db.cursor()

# try:
#     mysql_cursor.execute("CREATE TABLE users (user_id int,username varchar(255),phone_number varchar(255))")
#     print("table create successfull.")
# except Exception as e:
#     print(str(e))


# mysql_cursor.execute("SHOW TABLES;")


# for data in mysql_cursor:
#     print(data)




# mysql_cursor.execute("insert into users (user_id,username,phone_number) values (2,'mahidul','01800000000');")

# query = "insert into users (user_id,username,phone_number) values (%s,%s,%s)" 
# value = (3,'moon','01900000000')

# mysql_cursor.execute(query,value)
# mysql_db.commit()

# try:
#     mysql_cursor.execute('delete from users where user_id = 3;')
#     print("deleted successfully.")
#     mysql_db.commit()
# except Exception as e:
#     print(str(e))

try:
    mysql_cursor.execute('update users set username="mahidul" where user_id=2')
    print("updated successfully.")
    mysql_db.commit()
except Exception as e:
    print(str(e))

mysql_cursor.execute('select * from users;')

dataresult = mysql_cursor.fetchall()

for data in dataresult:
    print(data)


mysql_db.close()