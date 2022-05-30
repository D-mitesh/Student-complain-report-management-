from asyncio.windows_events import NULL
import mysql.connector

#making a class giving option to choose staff or student
class complain:
    def __init__(self):
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="complain_section")
        self.pointer=self.mydb.cursor()
        print("Choose an option who are you>>>>")
        self.opt=int(input("1>Staff 2>Student : "))
        if self.opt==1:
            sobj=staff
            opt=int(input("Do you want to 1>login or 2>Make a complain 3>Complain status : "))
            if opt==1:
                sobj.login(self)
            elif opt==2:
                complainer.staff_form(self)
            elif opt==3:
                self.complain_status()
            else:
                print("No such option available")
        elif self.opt==2:
            opt=int(input("1>Make a complain 2>Complain status : "))
            if opt==1:
                complainer.student_form(self)
            elif opt==2:
                self.complain_status()
            else:
                print("Wrong entry!")
                self.__init__()
        else:
            print("No such option available")
            self.__init__()
    
    #Showing complain status to complainer
    def complain_status(self):
        id=input("Enter your id : ")
        query="select * from complaint_box where complainer_id=%s;"
        self.pointer.execute(query,(id,))
        data=self.pointer.fetchall()
        for i in data:
            if i!=NULL:
                print("Your complain : ",i[1])
                print("Status of complain : ",i[2])
                print("Staff_id of staff who are incharge of your complain : ",i[0])
                break
            else:
                print("You make no complain here!")
                self.__init__()

#this class is for complainer whom are complaining
class complainer(complain):
    def __init__(self):
        opt=int(input("1>Staff 2>Student : "))
        if opt==1:
            self.staff_form()
        elif opt==2:
            self.student_form()
        else:
            print("No such option available")
    
    #complain form if complainer is a staff of university
    def staff_form(self):
        print("~~~~~~~~~~~~~COMPLAINT FORM~~~~~~~~~~~~~~~")
        sid=input("Enter your staff id : ")
        fname=input("Enter your first name : ").upper()
        lname=input("Enter your last name : ").upper()
        desg=input("Enter your designation : ").upper()
        dept=input("Enter your department : ").upper()
        resname=input("Enter name of student against whom you are complaining : ").upper()
        resdept=input("Enter the department of complainee : ").upper()
        complain=input("Enter your complain and any details about complainee if know : ")
        hodid=input("Enter the id of HOD of  complainee department : ")
        dict={"Staff id":sid,"first name":fname,"last name":lname,"designation":desg,"department":dept,"complainee_name":resname,"complainee_department":resdept,"Complain":complain}
        query="insert into complaint_box(staff_id,complain,status,complainer_id,complainee_name) values(%s,%s,%s,%s,%s)"
        self.pointer.execute(query,(hodid,str(dict),"Pending",sid,resname))
        self.mydb.commit()
        print("Your complain submitted succesfully!")
        main()

    #complain form if complainer is a student
    def student_form(self):
        print("~~~~~~~~~~~~~COMPLAINT FORM~~~~~~~~~~~~~~~")
        senroll=input("Enter your Enrollment number : ").upper()
        rollno=int(input("Enter your roll number : "))
        name=input("Enter your name : ").upper()
        email=input("Enter your email : ")
        course=input("Enter your course program : ").upper()
        dept=input("Enter your department : ").upper()
        resname=input("Enter name of student against whom you are complaining : ").upper()
        resdept=input("Enter the department of complainee : ").upper()
        complain=input("Enter your complain and any details about complainee if know : ")
        hodid=input("Enter the id of HOD of complainee department : ") 
        d={"Enrollment Number":senroll,"Roll no":rollno,"Name":name,"Email Address":email,"Course":course,"Department":dept,"complainee_name":resname,"complainee_department":resdept,"Complain":complain}
        query="insert into complaint_box(staff_id,complain,status,complainer_id,complainee_name) values(%s,%s,%s,%s,%s)"
        self.pointer.execute(query,(hodid,str(d),"Pending",senroll,resname))
        self.mydb.commit()
        print("Your complain submitted succesfully!")
        main()

#this class will give login option and other option to staff of university/Departments of university
class staff(complain):
    def login(self):
        sid=input("Enter your staff_id : ")
        spass=input("Enter your password : ")
        query="select * from staff"
        self.pointer.execute(query)
        data=self.pointer.fetchall()
        for i in data:
            if i[0]==sid:
                if i[1]==spass:
                    print("login successfully!")
                    staff.complain_check(self,sid)
                    break
                else:
                    print("Incorrect password entered!")
                    staff.login(self)
                break
        else:
            print("Incorrect staff id eneterd!")
            staff.login(self)

    def complain_check(self,sid):
        queryy="select * from staff where staff_id=%s;"
        self.pointer.execute(queryy,(sid,))
        data=self.pointer.fetchall()
        for i in data:
            if i[4]=='HOD':
                query="select * from complaint_box where staff_id=%s;"
                self.pointer.execute(query,(sid,))
                cdata=self.pointer.fetchall()
                k=1
                for j in cdata:
                    if j[1]!=NULL:
                        print("Complain!","Serial no.=",k)
                        print("")
                        print(j[1])
                        print("")
                        k+=1
                staff.actions(self)
            else:
                print("Empty complaint box")
                staff.actions(self)
                break
        else:
            opt=int(input("1>Status of your complain 2>Exit : "))
            if opt==1:
                self.complain_status()
            else:
                exit()

    def actions(self):
        opt=int(input("1>Complain authentication 2>Status update 3>Delete complain 4>Exit : "))
        if opt==1:
            opt2=int(input("Complainer: 1>Student 2>Staff >>>"))
            if opt2==1:
                print("Enter following details correctly : ")
                dept=input("Department : ").upper()
                course=input("Course program : ").upper()
                senroll=input("Enrollment number : ").upper()
                name=input("Name : ").upper()
                query="select * from student"
                self.pointer.execute(query)
                deta=self.pointer.fetchall()
                for i in deta:
                    if (i[5]==dept and i[0]==senroll) or (i[2]==name and i[4]==course):
                        queryy="update complaint_box set status='Processsing' where complainer_id=%s"
                        self.pointer.execute(queryy,(senroll,))
                        self.mydb.commit()
                        print("Entered data is authentic!")
                        print("Status updated to Processing successfully!")
                        staff.actions(self)
                        break
                    else:
                        print("Entered data is not matched with any data in database")
                        self.actions()
            elif opt2==2:
                print("Enter following details correctly : ")
                dept=input("Enter department : ").upper()
                desg=input("Enter designation : ").upper()
                sid=input("Enter staff id : ")
                query="select * from staff where staff_id=%s"
                self.pointer.execute(query,(sid,))
                deeta=self.pointer.fetchall()
                for i in deeta:
                    if (i[5]==dept and i[0]==sid and i[4]==desg):
                        queryy="update complaint_box set status='Processsing' where complainer_id=%s"
                        self.pointer.execute(queryy,(sid,))
                        self.mydb.commit()
                        print("Entered data is authentic!")
                        print("Status updated to Processing successfully!")
                        staff.actions(self)
                        break
                    else:
                        print("Entered data is not matched with any data in database")
                        staff.actions(self)
            else:
                print("No such option available!")
                staff.actions(self)
        elif opt==2:
            print("Enter  status 'Taken' if any action is taken against the complain :")
            print("")
            print("Enter status 'Denied' if no action have to take against complain(in case of false complain) ;")
            status_update=input("1>Taken 2>Denied :--").capitalize()
            cid=input("Enter complainer id : ")
            queryy="update complaint_box set status=%s where complainer_id=%s"
            self.pointer.execute(queryy,(status_update,cid,))
            self.mydb.commit()
            print("Status updated to ",status_update,"successfully!")
            staff.actions(self)
        elif opt==3:
            ssid=input("Enter your id first : ")
            query="select * from complaint_box where staff_id=%s"
            self.pointer.execute(query,(ssid,))
            cdeta=self.pointer.fetchall()
            for i in cdeta:
                if i[2]=='Taken':
                    print("A successfull action is being taken against the complain!")
                    oppt=input("Enter yes to delete the complain from complain box : ").lower()
                    if oppt=="yes":
                        cid=input("Enter complainer id : ")
                        quer="delete from complaint_box where complainer_id=%s"
                        self.pointer.execute(quer,(cid,))
                        self.mydb.commit()
                        print("Complain deleted successfully!")
                    else:
                        staff.actions()
                elif i[2]=='Denied':
                    print("Denied false complain!")
                    oppt=input("Enter yes to delete the complain from complain box : ").lower()
                    if oppt=="yes":
                        cid=input("Enter complainer id : ")
                        quer="delete from complaint_box where complainer_id=%s"
                        self.pointer.execute(quer,(cid,))
                        self.mydb.commit()
                        print("Complain deleted successfully!")
                    else:
                        staff.actions(self)
                else:
                    exit()
        elif opt==4:
            exit()
        else:
            print("No such option is available!")
            staff.actions(self)
main=complain
main()