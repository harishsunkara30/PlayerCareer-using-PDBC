from tabulate import tabulate
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "harish7822",
    database = "career"
)
def insert(id, name, innings, average):
    cr = conn.cursor()
    sql = "insert into player(id, name, innings, average) values (%s, %s, %s, %s)"
    user = (id, name, innings, average)
    cr.execute(sql, user)
    conn.commit()
    print("successfully data inserted")

def update(id, name, innings, average):
    cr = conn.cursor()
    sql = "update player set id=%s, name=%s, innings=%s, average=%s"
    user = (id, name, innings, average)
    cr.execute(sql, user)
    conn.commit()
    print("successfully data updated")
def select():
    cr = conn.cursor()
    sql = "select * from player"
    cr.execute(sql)
    result = cr.fetchall()
    print(tabulate(result, headers=["ID", "Name", "Innings", "Average"]))
def delete(id):
    cr = conn.cursor()
    sql = "delete from player where id=%s"
    user = (id,)
    cr.execute(sql, user)
    conn.commit()
    print("successfully data deleted")
while True:
    print("1.Insert data")
    print("2.Update data")
    print("3.Select data")
    print("4.Delete data")
    print("5.Exit")
    options = int(input("enter your options: "))
    if options ==1:
        id = input("Enter the ID: ")
        name = input("Enter the Name: ")
        innings = input("Enter No of Innings: ")
        average = input("Enter the Average: ")
        insert(id, name, innings, average)

    elif options == 2:
        id = input("Enter the ID: ")
        name = input("Enter the Name: ")
        innings = input("Enter No of Innings: ")
        average = input("Enter the Average: ")
        update(id, name, innings, average)

    elif options == 3:
        select()
    elif options == 4:
        id = input("Enter your ID: ")
        delete(id)

    elif options == 5:
        break
    else:
        print("Not found, Try Again!")



