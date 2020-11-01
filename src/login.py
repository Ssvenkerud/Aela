import sqlite3
import time
import sys

def login():
    while True:
        username = input('Please enter your username: ')
        password = input('please enter your pasword: ')
        with sqlite3.connect('aloy.db') as db:
            cursor = db.cursor()
        find_archer = ('SELECT * FROM archer WHERE username = ? AND password = ?')
        cursor.execute(find_archer, [(username), (password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print('Welcome '+i[2])
            #return('exit')
            break

        else:
            print('Username and password not recognised')
            again = input('do you want to try again? (y/n): ')
            if again.lower()== 'n':
                print('goodbye')
                time.sleep(2)
                #return ('exit')
                break

def newArcher():
    found = 0
    while found == 0:
        username = input('Please enter a username: ')
        with sqlite3.connect('aloy.db') as db:
            cursor = db.cursor()
        findArcher = "SELECT * FROM archer WHERE username = ?"
        cursor.execute(findArcher,[(username)])

        if cursor.fetchall():
            print('Sorry, That username is aleady taken, please try again')
        else:
            found = 1

    first_name = input('please enter your first name: ')
    middle_name = input('please enter your middel name (optional): ')
    last_name = input('please enter your last name: ')
    email = input('please enter your email adress (optional): ')
    password = input('please enter your password: ')
    password1 = input('please verify your password')
    while password != password1:
        print('Your passwords did not match, please try again')
        password = input('please enter your password: ')
        password1 = input('please verify your password: ')

    insertData = '''
    INSERT INTO archer(username, archer_first_name,archer_middel_name, archer_last_name, archer_email, password)
    VALUES(?,?,?,?,?,?)
    '''
    cursor.execute(insertData, [(username), (first_name), (middle_name), (last_name), (email), (password)])
    db.commit()

def menu():
    while True:
        print('Welcome to Ayloy')
        menu = ('''
        1 - Create new user
        2 - Login
        3 - Exit the system\n
        ''')
        userChoice = input(menu)

        if userChoice == '1':
            newArcher()
        elif userChoice == '2':
            login()
        elif userChoice == '3':
            print('Goodbye')
            sys.exit()
        else:
            print('Command not recognised')



menu()