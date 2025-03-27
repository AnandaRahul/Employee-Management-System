Employee Management System

Overview

The Employee Management System is a Python-based application that uses MySQL (via XAMPP) as the database to manage employee records. It allows users to add, update, delete, and view employee details efficiently.

Features

- Add new employees
- Update existing employee details
- Delete employees from the system
- View all employees in a structured format
- Promote employees with salary increments
- Search employees by ID
- User-friendly interface with CLI-based interactions
- Secure database connectivity using MySQL

Technologies Used

- Programming Language: Python
- Database: MySQL (via XAMPP)
- **Libraries Used:**
  - mysql.connector` (for database connectivity)
  - re (for regex-based validations)
  - os (for system commands)

Installation

Prerequisites

1. Install Python (version 3.x recommended)
2. Install XAMPP and start the MySQL service
3. Install required Python packages:  pip install mysql-connector-python

To create the database:

1. Open XAMPP and start the Apache & MySQL modules.
2. Then, Using this Code Created the database.
	
	con = mysql.connector.connect(host="localhost",user="root",password="")
	mycursor = con.cursor()
	mycursor.execute("CREATE DATABASE employee")

3. To Create a table inside `employee` database:
   	
	con = mysql.connector.connect(host="localhost",user="root",password="",database="employee")
	mycursor = con.cursor()
	mycursor.execute("CREATE TABLE empdata(Id INT(11) PRIMARY KEY,Name VARCHAR(1000),Email_id TEXT(1000), 	Phone_no INT(11), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(20))")

Usage

1. Run the Python script:  python main.py
2. Follow the menu options to add, update, delete, promote, search, or view employees.
3. Ensure XAMPP's MySQL service is running before using the application.


Future Enhancements

- Add a graphical user interface (GUI) using Tkinter or Flask.
- Implement authentication for secure access.
- Generate reports in CSV or PDF formats.
- Improve input validation and error handling.
