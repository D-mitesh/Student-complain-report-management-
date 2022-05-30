#importing all required libraries
import mysql.connector
from bank import bank
#creating a class where customer can see all details,total balance,can do money withdraw and deposit
class customer_acc_work:
    def __init__(self):
        #constructor class connecting to database and giving option to see details/ check total balance/withdraw/deposit to customer
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="Bank")
        self.pointer=self.mydb.cursor()
        self.opt=int(input("1:See Your Details 2:Check Total Balance 3:Withdraw Money 4:Deposit Money >>>"))
        if self.opt==1:
            self.see_details()
        elif self.opt==2:
            self.total_balance()
        elif self.opt==3:
            self.withdraw()
        elif self.opt==4:
            self.deposit()
        else:
            print("No such option available!")
            self.__init__()
    def see_details(self):
        cust_id=input("Enter your userid : ")
        show="select * from bank_customer"
        self.pointer.execute(show)
        data=self.pointer.fetchall()
        for i in data:
            if i[1]==cust_id:
                print("Your Account type : ",i[0])
                print("Userid : ",i[1])
                print("Account Number : ",i[3])
                print("Name : ",i[4])
                print("Gender : ",i[5])
                print("Father's Name : ",i[6])
                print("Mother's Name : ",i[7])
                print("Date of Birth : ",i[8])
                print("Email Address : ",i[12])
                print("Branch name : ",i[16])
                print("Residance's Address : ",i[20])
                print("Nominee's Name : ",i[22],"(",i[23],")")
                break
            else:
                print("No data available with this userid!")
                bank.__init__()
    def total_balance(self):
        accno=(input("Enter Your Account NUmber : "))
        show="select * from bank_customer"
        self.pointer.execute(show)
        data=self.pointer.fetchall()
        for i in data:
            if i[3]==accno:
                print("Total Balance : ",i[24])
                break
            else:
                print("No Data available with this account number!")
    def withdraw(self):
        accno=(input("Enter Your Account Number : "))
        show="select * from bank_customer"
        self.pointer.execute(show)
        data=self.pointer.fetchall()
        for i in data:
            if i[3]==accno:
                wd=int(input("Enter the amount you want to withdraw : "))
                if i[24]>wd:
                    current=i[24]-wd
                    print("Rs.",wd,"withdrawn from account number ",i[3])
                    print("Your current Balance is Rs.",current)
                    query="update bank_customer set Total_balance=%s where Account_no=%s; "
                    self.pointer.execute(query,(current,accno,))
                    self.mydb.commit()
                    break
                else:
                    print("You have low balance than you want to withdraw!")
                    print("Your current balance : ",i[24])
                break
            else:
                print("No Data available with this account number!")
    def deposit(self):
        accno=(input("Enter Your Account Number : "))
        show="select * from bank_customer"
        self.pointer.execute(show)
        data=self.pointer.fetchall()
        for i in data:
            if i[3]==accno:
                depo=int(input("Enter the amount you want to deposit : "))
                current=i[24]+depo
                print("Rs.",depo,"deposited on account number ",i[3])
                print("Your current Balance is Rs.",current)
                query="update bank_customer set Total_balance=%s where Account_no=%s; "
                self.pointer.execute(query,(current,accno,))
                self.mydb.commit()
                break
        else:
            print("No Data available with this account number!")
obj=customer_acc_work
obj()