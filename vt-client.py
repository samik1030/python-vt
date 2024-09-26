import mysql.connector    # connector for MySQL
import time               # time library module 
import math               # math library module 
from os import system, name  # system library module

# Database credentials will be changed once after completion of the project
# Demo db is used for production 
mydb = mysql.connector.connect(
    host="103.211.216.137",
    user="kivaabip_stocks",
    password="hdepl@2020",
    database="kivaabip_stockmarket"
)

# Cursor object for running the SQL queries
mycursor = mydb.cursor()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def mainmenu(username):
    print("Main Menu")
    print("1: View Balance")
    print("2: Trade")
    print("0: Exit")
    opt = int(input("Choose an Option : "))

    match opt:
        case 1:
            balance(username)
        case 2:
            trade(username)
        case 0:
            exit()
        case _:
            print("Error: Select a valid Option.")
            mainmenu(username)

def balance(username):
    sql1 = "SELECT * FROM account WHERE username = %s"
    val1 = (username, )
    mycursor.execute(sql1, val1)
    row1 = mycursor.fetchall()
    
    if row1:
        for x in row1:
            cashbal = x[2]
            holdingbal = x[3]
            overallbal = x[4]
        print("Dashboard")
        print("Cash Balance    : ₹", cashbal)
        print("Holding Balance : ₹", holdingbal)
        print("Overall Balance : ₹", overallbal)
    else:
        print("No account information found.")

def trade(username):
    print("Trade")
    print("1: Buy / Sell ")
    print("2: View Holdings")
    print("3: View Orders ")
    print("4: View All Stocks")
    print("9: Main Menu")
    print("0: Exit")
    opt = int(input("Choose an Option : "))
    match opt:
        case 1:
            print("1: Buy Stocks")
            print("2: Sell Stocks")
            opt3 = int(input("Choose an Option : "))
            match opt3:
                case 1:
                    buy()
                case 2:
                    sell()
                case _:
                    print("Invalid Option!")
                    mainmenu(username)
        case 2:
            holdings(username)
        case 3:
            orders()        
        case 4:
            viewallstocks(username)
        case 9:
            mainmenu(username)
        case 0:
            exit()
        case _:
            print("Invalid Option")
            mainmenu(username)

def buy():
    print("Buy Stocks")

def sell():
    print("Sell Stocks")

def holdings(username):
    print("Holdings")

def orders():
    print("View Orders")

def viewallstocks(username):
    print("View All Stocks")
    sql = "SELECT * FROM holdings WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    row = mycursor.fetchall()
    if not row:
        print("You have not bought any stocks")
        trade(username)
    else:
        for x in row:
            print(x[2], " - ", x[3])

def start():
    print("1 : Login")
    print("2 : Sign Up")
    opt1 = int(input("Select an Option : "))
    match opt1:
        case 1:
            login()
        case 2:
            signup()
        case _:
            exit()

def login():
    username = int(input("Enter your Mobile Number : "))
    password = input("Enter the password : ")

    sql = "SELECT * FROM customers WHERE username = %s"
    value = (username, )
    mycursor.execute(sql, value)

    row = mycursor.fetchone()

    if row is None:
        print("User Doesn't exist")
        print("")
        login()
    elif password == row[2]:
        print("Login Verified")
        mainmenu(username)
    else:
        print("Invalid Username or Password!")
        print("Relaunch the application")

def signup():
    username = int(input("Enter your mobile number : ")) 
    sql2 = "SELECT * FROM customers WHERE username = %s"
    val2 = (username, )
    mycursor.execute(sql2, val2)
    row2 = mycursor.fetchone()
    print(row2)
    if row2 is not None:
        print("Username already exists")
        print("Choose another username or Login if already Signed Up")
        signup()
    password = input("Enter the Password (a-z, A-Z, 0-9, !@#$& ) : ")
    
    sql3 = "INSERT INTO customers (username, password) VALUES (%s, %s)"
    val3 = (username, password)
    mycursor.execute(sql3, val3)
    mydb.commit()

    sql4 = "INSERT INTO account (username, cashbal, holdingbal, overallbal) VALUES (%s, %s, %s, %s)"
    val4 = (username, 100000, 0, 100000)
    mycursor.execute(sql4, val4)
    mydb.commit()

    print("User Account Created, login to your account.")
    login()

clear()
start()
