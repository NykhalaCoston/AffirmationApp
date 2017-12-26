# the first line of the program  makes the python file an executable script, that can be run from
# terminal, without the line below, it will need you to run like ($python3 filename), but with this
# line, you can simply run the file like ($./filename)

#!/usr/local/bin/python3

# start message
print ('''
        ===============================
        Welcome to the Affirmation App.
        ===============================''')

# functions that I can use later
def main_menu():
    print ('''
    Please choose an option
    1. Update
    2. Quit
    ''')

def quit_menu():
    return 0

def update_menu():
    print ('''
    1. Add email
    2. Delete email
    3. Add affirmation
    4. Delete affirmation    
    ''')

# call the functions

main_menu()
update_menu()

