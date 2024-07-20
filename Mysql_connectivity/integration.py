from tabulate import tabulate
import mysql.connector

con_=mysql.connector.connect(host="localhost",user="root",password="guhan",database="data_")


def select():
    cursor=con_.cursor()
    sql_query="Select * from person"
    cursor.execute(sql_query)
    result=cursor.fetchall()
    print(tabulate(result,["Id","Name","Age","Location"]))
    
    
    
def insert(name,age,location):
    cursor=con_.cursor()
    sql_query="insert into person (Name,age,location) values (%s,%s,%s)"
    user=(name,age,location)
    cursor.execute(sql_query,user)
    con_.commit()
    print("Data Stored Successfully")

    

def update(id,name,age,location):
    cursor=con_.cursor()
    sql_query="update person set name=%s,age=%s,location%s where id=%s"
    user=(name,age,location,id)
    cursor.execute(sql_query,user)
    con_.commit()
    print("Date update successfully")

def delete(id):
    cursor=con_.cursor()
    sql_query="delete from person where id=%s"
    user=(id)
    cursor.execute(sql_query,user)
    con_.commit()
    print("Data Delete Successfully")

def drop():
    cursor=con_.cursor()
    query="drop table person"
    cursor.execute(query)
    con_.commit()
    print("Table droped")
    







while True:
    print("1.Select")
    print("2.Insert")
    print("3.Update")
    print("4.Delete")
    print("5.drop")
    print("6.Quit")
    choice=int(input("Enter here: "))
    
    if choice==1:
        select()
        
    elif choice==2:
        name=input("Enter the name: ")
        age=input("Enter the age: ")
        location=input("Enter the location: ")
        insert(name,age,location)
        
    elif choice==3:
        id=input("Enter the id :")
        name=input("Enter the name: ")
        age=input("Enter the age: ")
        location=input("Enter the location: ")
        update(id,name,age,location)
        
    elif choice==4:
        id=input("Enter the id :")
        delete(id)

    elif choice==5:
        drop()
        
    elif choice==6:
        quit()

    else:
        print("Entered the wrong choice..check :)")
    
