import mysql.connector
try:
    mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="Bank")
    pointer=mydb.cursor()
    query="delete from bank_customer where Userid='M!tesh0404';"
    pointer.execute(query)
    mydb.commit()
    print("Task done successfully!")
except Exception as error:
    print("Error : ",error)