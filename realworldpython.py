# -*- coding: utf-8 -*-
"""
@author: priyanka
"""
print("Sample Commented Script showing usage of Python in Real World Programming")
print("----------------------")
print("Database Connections - Sample Commented Code")
print("1. Python Module for Database Connection")
#import MySQLdb

print("2. Opening a database connection")
#database = MySQLdb.connect  ("localhost","test","UserName","DatabaseName")

print("3. define a cursor object")
#cur = conn.cursor

print("4. Run the query")
#sqlQuery = "CREATE TABLE EMPLOYEE (NAME CHAR(30) NOT NULL, AGE INT, GENDER CHAR(10), SSN INT"
#cur.execute(sqlQuery)

print("5. Close the object after execution is done")
#cur.close()
#conn.close()

print("----------------------")
print("Network Programming - Sample Commented Code")
print("1. Python Module for Network Connection")
#import socket
print("2. Entering host details")
#HOST = '0.0.0.0'  
#PORT = 1234       
print("3. Socket Connection, Listening")
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    #soc.bind((HOST, PORT))
    #soc.listen()
    #conn, addr = soc.accept()
    #with conn:
        #while True:
            #data = conn.recv()
            #if not data:
                #break
           #conn.sendall(data)
print("4. Socket Connection Ends")
print("----------------------")
print("GUI Flask Programming - Sample Commented Code")
print("1. Python Module for MVC Framework")
#from flask import Flask
#app = Flask(__name__)
print("2. Declare routes in route.py for rendering HTML files or transfering data around template files")
#@app.route('/')
#def hello():
    #return render_template( 'a.html')
print("----------------------")
print("System Programming - Sample Commented Code")
print("1. Python Module for Making System Calls")
#import os 
print("2. Get current working directory")
#print(os.getcwd()) 
print("----------------------")