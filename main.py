from os import system
import re
import mysql.connector

# con = mysql.connector.connect(host="localhost",user="root",password="")
# mycursor = con.cursor()
# mycursor.execute("CREATE DATABASE employee")

# con = mysql.connector.connect(host="localhost",user="root",password="",database="employee")
# mycursor = con.cursor()
# mycursor.execute("CREATE TABLE empdata(Id INT(11) PRIMARY KEY,Name VARCHAR(1000),Email_id TEXT(1000), Phone_no INT(11), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(20))")

con = mysql.connector.connect(host="localhost",user="root",password="",database="employee")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = re.compile("(0|91)?[7-9][0-9]{9}")

def Add_employee():
    print("{:>60}".format("-->> Add Employee Record <<--"))

    ID = input("Enter Employee ID: ")
    if(check_employee(ID)==True):
        print("Employee ID Already Exists \nTry Again With Another ID")
        press = input("Press Any Key To Continue..")
        Add_employee()

    Name = input("Enter Employee Name: ")
    if(check_employee_name(Name)==True):
        print("Employee Name Already Exists \nTry Again")
        press = input("Press Any Key To Continue..")
        Add_employee()

    Email_ID = input("Enter Employee Email Id: ")
    if(re.fullmatch(regex, Email_ID)):
        pass
    else:
        print("Invalid Email Or Employee Email Already Exists \nTry Again")
        press = input("Press Any Key To Continue..")
        Add_employee()
        
    Phone_No = input("Enter Employee Phone Number: ")
    if(pattern.match(Phone_No)):
       pass
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_employee()

    Address = input("Enter Employee Adress: ")

    Post = input("Enter Employee Post: ")

    Salary = input("Enter Employee Salary: ")

    data = (ID,Name,Email_ID,Phone_No,Address,Post,Salary)
    sql = "INSERT INTO Empdata VALUES(%s,%s,%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Successfully Added")
    press = input("Press Any Key To Continue..")
    menu()

def check_employee_name(employee_name):
    sql = "SELECT * FROM Empdata where Name=%s"
    c = con.cursor(buffered=True)
    data = (employee_name,)
    c.execute(sql,data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
    
def check_employee(employee_id):
    sql = "SELECT * FROM Empdata where ID=%s"
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql,data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def display_employee():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    sql = "SELECT * FROM empdata"
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email ID: ", i[2])
        print("Employee Phone Number: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any Key To Continue..")
    menu()

def update_employee():
    print("{:>60}".format("-->> Update Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if(check_employee(ID)==False):
        print("Employee ID Already Exists \n Try Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Email_ID = input("Enter Employee Email Id: ")
        if(re.fullmatch(regex, Email_ID)):
            print("Valid Email")
        else:
            print("Invalid Email Or Employee Email Already Exists \nTry Again")
            press = input("Press Any Key To Continue..")
            update_employee()
    Phone_No = input("Enter Employee Phone Number: ")
    if(pattern.match(Phone_No)):
        pass
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        update_employee()

    Address = input("Enter Employee Adress: ")
    sql = "UPDATE empdata set Email_ID = %s, Phone_No = %s, Address = %s where ID = %s"
    data = (Email_ID,Phone_No,Address,ID,)
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Updated Employee Record")
    press = input("Press Any Key To Continue..")
    menu()   

def promote_employee():
    print("{:>60}".format("-->> Promote Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if(check_employee(ID)==False):
        print("Employee Record Not Exists \n Try Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount = int(input("Enter Increase Salary: "))
        sql = "SELECT SALARY FROM empdata WHERE ID=%s"
        data = (ID,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0] + Amount
        sql = "UPDATE empdata set Salary = %s where ID = %s"
        d = (t,ID)
        c.execute(sql,d)
        con.commit()
        print("Employee Promoted")
        press = input("Press Any Key To Continue..")
        menu()

def remove_employee():
    print("{:>60}".format("-->> Remove Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if(check_employee(ID)==False):
        print("Employee Record Not Exists \n Try Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'DELETE FROM empdata WHERE ID = %s'
        data = (ID,)
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Employee Removed")
        press = input("Press Any Key To Continue..")
        menu()

def search_employee():
    print("{:>60}".format("-->> Search Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if(check_employee(ID)==False):
        print("Employee Record Not Exists \n Try Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = "SELECT * FROM empdata WHERE ID = %s"
        data = (ID,)
        c = con.cursor()
        c.execute(sql,data)
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email ID: ", i[2])
            print("Employee Phone Number: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any Key To Continue..")
        menu()

def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n") 
    print("{:>65}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<-- "))

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        system("cls")
        Add_employee()

    elif ch == 2:
        system("cls")
        display_employee()

    elif ch == 3:
        system("cls")
        update_employee()

    elif ch == 4:
        system("cls")
        promote_employee()

    elif ch == 5:
        system("cls")
        remove_employee()

    elif ch == 6:
        system("cls")
        search_employee()

    elif ch == 7:
        system("cls")
        print("{:>60}".format("--->>  Have a Nice Day :)  <<--- \n"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any Key To Continue..")
        menu()

menu()
