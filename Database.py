import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "bubuFeb2016!",
    database = "testdb"
)

my_cursor = mydb.cursor()

############################################################################################################
# CREATE DATABASE
############################################################################################################
# my_cursor.execute("CREATE DATABASE testdb")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])

############################################################################################################
# CREATE TABLE
############################################################################################################
# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), \
# user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")
# for tbl in my_cursor:
#     print(tbl[0])

############################################################################################################
# INSERT ONE RECORD
############################################################################################################
# sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Deepak", "Deepakm.Rajendra@gmail.com", 33)
# my_cursor.execute(sql, record1)
# mydb.commit()

############################################################################################################
# INSERT MULTIPLE RECORDS
############################################################################################################
# sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# records = [("Tim", "tim@tim.com", 32),
#     ("Mary", "mary@mary.com", 21),
#     ("Steve", "Steve@somethingelse.com", 27),
#     ("Tina", "Tina@tinasemail.com", 37),]
# my_cursor.executemany(sql, records)
# mydb.commit()

############################################################################################################
# READ TABLE AS TUPLE
############################################################################################################
# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

############################################################################################################
# READ TABLE FORMATTED
############################################################################################################
# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# print("NAME\tEMAIL\t\t\tAGE\tID")
# print("----\t-----\t\t\t---\t--")
# for row in result:
#     print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

############################################################################################################
# READ TABLE WITH WHERE CLAUSE
############################################################################################################
# my_cursor.execute("SELECT * FROM users where name = 'Deepak'")
# result = my_cursor.fetchall()
# print("NAME\tEMAIL\t\t\tAGE\tID")
# print("----\t-----\t\t\t---\t--")
# for row in result:
#     print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

############################################################################################################
# UPDATE TABLE WITH WHERE CLAUSE
############################################################################################################
sql = "UPDATE users set age = 34 where name = 'Deepak'"
my_cursor.execute(sql)
mydb.commit()






