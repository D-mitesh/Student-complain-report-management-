#importing all reqiuired libraries
import mysql.connector
import random as rn
import string as str
#creating a main class for account opening or login
class bank:
    #constructor class connecting to database and giving option to login/Open Account to customer
    def __init__(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="Bank")
        self.pointer=self.mydb.cursor()
        choice=int(input("1:Login 2:Open Account >>>"))
        if choice==1:
            self.clogin()
        elif choice==2:
            self.acc_open()
        else:
            print("No such option available!")
            self.__init__()
    #login function which checks user's userid and password
    def clogin(self):
        userid=input("Enter Your Userid : ")
        pas=input("Enter Your password : ")
        show="select * from bank_customer;"
        self.pointer.execute(show)
        data=self.pointer.fetchall()
        for i in data:
            if i[1]==userid:
                if i[2]==pas:
                    print("You're logged in!",userid)
                    break
                else:
                    print("You entered wrong password!")
                    self.clogin()
                break
        else:
            print("You entered wrong userid or you are not a account holder!")
            opt=input("1:Login 2:Open Account>>>")
            if opt=="1":
                self.clogin()
            elif opt=="2":
                self.acc_open()
            else:
                print("No such option available!")
    #account opening main function for selecting account type
    def acc_open(self):
        print("Welcome to Our Bank!")
        self.acctype=int(input("Select Your account type : 1>Insta Plus Saving Account 2>Insta savings Account>>>"))
        if self.acctype==1:
            print(">Full KYC account and no limititation on balance/transaction")
            self.acc_type="Insta Plus Saving Account"
            self.acc_opening_form(self.acc_type)
        elif self.acctype==2:
            print(">Limited KYC with maximuim balance upto Rs. 1 lakh and aggregate credit during a year in the account not to exceed Rs. 2 lakh")
            self.acc_type="Non Insta Plus Saving Account"
            self.acc_opening_form(self.acc_type)
        else:
            print("No such option available!")
            self.acc_open()
    #account number generation function which generates a random account number
    def acc_numgen(self):
        digi=str.digits
        self.acc_num=""
        for i in range(11):
            rann=rn.choice(digi)
            self.acc_num=rann+self.acc_num
        return self.acc_num
    #account opening form for bank customers who want to open a account
    def acc_opening_form(self,acc_type):
        try:
            self.mob=int(input("Enter Your Mobile number : "))
            self.email=input("Enter Your Email address : ")
            self.aadhar=int(input("Enter your aadhar number here : "))
            self.pan=input("Enter Your PAN number : ")
            self.fname=input("Enter Your Full Name : ").capitalize()
            self.gen=input("Enter Your Gender(Male/Female/Trans) : ").capitalize()
            self.dob=input("Enter Your Date of Birth[YYYY\MM\DD] : ")
            self.add=input("Enter Your Full Adress : ")
            self.state=input("Enter Your State : ")
            self.dis=input("Enter Your District : ")
            self.vill=input("Enter Your Village Name : ")
            self.tdate=input("Enter today's date[YYYY\MM\DD] : ")
            self.edu=input("Enter Educational Qualification[1>Below SSC 2>SSC/HSC 3>Graduate 4>Post Graduate 5>Professional] : ").upper()
            self.ms=input(r"Enter your marital status[Married/Unmarried/Others] : ")
            self.father=input("Enter Your Father's Name : ").capitalize()
            self.mother=input("Enter Your Mother's Name : ").capitalize()
            self.rel=input("Enter Your Religion : ")
            self.nomname=input("Enter Your Nominee's Name : ").capitalize()
            self.nomrel=input("Enter Your Nominee's relationship : ")
            self.branch=input("Enter Your Home Branch : ")
            print("Your given data is saved!")
            self.userid=input("Create a Userid of atleast 6 letters containing a uppercase,a lowercase,a number and a special character : ")
            self.pas=input("Create a password of atleast 8 letters containing a uppercase,a lowercase,a number and a special character : ")
            self.accno=self.acc_numgen()
            data=(self.acc_type,self.userid,self.pas,self.accno,self.fname,self.gen,self.father,self.mother,self.dob,self.mob,self.pan,self.aadhar,self.email,self.state,self.dis,self.vill,self.branch,self.ms,self.rel,self.edu,self.add,self.tdate,self.nomname,self.nomrel)
            query="insert into bank_customer(acc_type,Userid,password,Account_no,Full_name,gender,father_name,mother_name,birthdate,Mobile,PAN_no,aadhar_no,email,state,district,village,branch_name,marital_status,religion,education,address,tdate,Nominee_name,Nominee_relation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.pointer.execute(query,data)
            self.mydb.commit()
            print("Your account is successfully opened with Account Number : ",self.accno)
            opt=input(r"Do you want to login? [Yes/No] : ").lower()
            if opt=="yes":
                self.clogin()
            else:
                print("Thank you for choosing our bank to serve you!")
        except Exception as error:
            print("Error Occured : ",error)
            self.acc_opening_form(self.acc_type)
'''objj=bank
objj()'''