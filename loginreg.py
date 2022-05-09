#program for login and register of username and password in user's name file 
import os
def main():
    print("<Enter your choice>")
    print("Do you want to login/register: for login enter L and for register enter R")
    choice=input("Enter your choice : ").upper()
    def login():
        name=input("Enter Your name : ")
        username=input("Enter your username:")
        password=input("Enter your password:")
        check(name,username,password)
    def check(name,username,password):
        list=os.listdir()
        for i in list:
            if name==i:
                print("Your data is here!")
                file=open(name,'r')
                data=file.read()
                data=data.split('\n')
                file.close()
                for i in range(len(data)):
                    if data[i] == "USERNAME : "+username:
                        print("founded your username!")
                        for j in range(i+1,len(data)):
                            if data[j] == "PASSWORD : "+password:
                                print("You are logged in!")
                                sub_choice(name)
                                break
                        else:
                            print("You entered incorrect password!")
                            print("Please login again!")
                            login()
                        break
                else:
                    print("<You entered incorrect username!Back to login>")
                    login()
                break
        else:
            print("You're not here!so you can register!")
            reg=input("Enter 'ok' to register yourself otherwise enter any other key : " ).upper()
            if reg=="OK":
                register(name,username,password)
            else:
                exit()
    def user_update(name,pas):
        file=open(name,'w')
        username=input("Enter a new username : ")
        file.write("USERNAME : "+username+'\n')
        file.write(pas)
        file.close()
    def add(name):
        file=open(name,'a')
        username=input("Create your username:")
        password=input("Create your password:")
        file.write("USERNAME : "+username+'\n')
        file.write("PASSWORD : "+password+'\n')
        file.close()
    def read(name):
        file=open(name,'r')
        print("Here is your data : ")
        print(file.read())
        file.close()
    def register(name,username,password):
        file=open(name,'w')
        file.write("USERNAME : "+username+'\n')
        file.write("PASSWORD : "+password+'\n')
        file.close()
        print("You are registered succesfully!")
        sub_choice(name)
    def sub_choice(name):
        print("<If you want to see your data, enter 'y'>")
        print("<If you want to login, enter 'l'>")
        print("<If you want to register new data, enter 'r'>")
        print("<If you want to update your username, enter'u'> ")
        opt=input("Enter your choice : ").lower()
        if opt=="y":
            read(name)
        elif opt=="l":
            login()
        elif opt=="r":
            add(name)
        elif opt=="u":
            print("Update your data : ")
            file=open(name,'r')
            new=file.read()
            new =new.split('\n')
            file.close()
            user=new[0]
            pas=new[1]
            user_update(name,pas)
        else:
            main()
    if choice=="L":
        login()
    elif choice=="R":
        name=input("Enter your name : ")
        username=input("Create your username:")
        password=input("Create your password:")
        check(name,username,password)
    else:
       print("Wrong choice.Exit!")
       exit()
main()   