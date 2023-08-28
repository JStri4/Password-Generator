import random
import string
import os
from tkinter import *
from tkinter import messagebox

#widget
#root = Tk()
#
#label1 = Label(root, text = "Welcome", font = ('Arial', 18))
#label1.place(relx = 0.43, rely = 0.01)
#
#root.geometry("800x500")
#root.title("PassGen Ver. 0.0 Dev Build")
#
##Specify the Grid
##Grid.rowconfigure(root, 0, weight = 1)
##Grid.columnconfigure(root, 0, weight = 1)
##Grid.rowconfigure(root, 1, weight = 1)
#
##textbox = Text(root, height = 3, font = ('Arial', 16))
##textbox.pack(padx = 10, pady = 10)
#
#button1 = Button(root, text = "Generate Password", font = ('Arial', 18))
#button1.place(relx = 0.15, rely = 0.5)
##button1.grid(row = 0, column = 0)
#
#button2 = Button(root, text = "Manage Passwords", font = ('Arial', 18))
#button2.place(relx = 0.55, rely = 0.5)
##button2.grid(row = 1, column = 0)
#
#root.mainloop()

passLength = 0
#passwordID = 0
#site = None
#username = None
filePath = os.path.dirname(os.path.realpath(__file__))

def Welcome():
    print("Welcome to PassGen  \n")

#Make a condition to limit the amount of characters, like 24 characters
def GetPassLength():
    while True:
        try:    
            global passLength
            passLength = int(input("enter the length of the password: "))
            return passLength
        except ValueError:
            print("Please enter an integer...")
    
def GenPassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def Output():
    global password
    password = GenPassword(passLength)
    print('Your password is: ' + password + '\n')
  
def SavePassword(password):
    ynRewind = input("Would you like to save this password? (y/n): ")
    if ynRewind == 'y':
        script_dir = filePath
        file_path = os.path.join(script_dir, 'Passwords.txt')
        print('Your password is: ' + password + '\n')
        print("Password has been saved as: " + password)
        with open('Passwords.txt', 'a') as file:
            file.write(f'{password}\n')
        MainMenu()
        
    elif ynRewind == 'n':
        Output()
        SavePassword(password)
        print("Password has been regenerated as: " + password)
    else:
        print("Invalid input. Please enter y or n... \n")
        SavePassword(password)

def ViewPasswords():
    script_dir = filePath
    file_path = os.path.join(script_dir, 'Passwords.txt')
    
    if not os.path.exists(file_path):
        print("Passwords file does not exist, check again or create Passwords.txt...")
        return

    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip().split(':')
            print(f'Password: {password}')
            
def DeletePasswords(index):
    script_dir = filePath
    with open("passwords.txt", "r") as file:
        passwords = file.readlines()
    
    if 1 <= index <= len(passwords):
        deleted_password = passwords.pop(index - 1)
        with open("Passwords.txt", "w") as file:
            file.writelines(passwords)
        print(f"Deleted password: {deleted_password.strip()}")
    else:
        print("Invalid index.") 
    
def Skeleton():
    GetPassLength()
    Output()
    SavePassword(password)

def MainMenu():
    print("----Main Menu----\n",
          "1. Generate new password\n",
          "2. View passwords\n",
          "3. Delete old password\n",
          "4. Quit\n")
    
    choice = input("Choose: ")
    if choice == '1':
        Skeleton()
    elif choice == '2':
        ViewPasswords()
    elif choice == '3':
        DeletePasswords()
    elif choice == '4':
        exit()
    else:
        print("Invalid choice. Please select again.")
        MainMenu()
        
    
def Main():
    Welcome()
    MainMenu()
    
Main()

# add an update password function
# add a generate new password function
# tie certain functions/actions to numbered inputs







#class PasswordClass:
#    global PasswordID 
#    PassActual = password
#    Website = site
#    name = username


# file io
# syntax - animals = open('animals.txt', 'a+')
# r = open for read (default)
# w = open for write, truncate (wipes existing contents)
# r+ = open for read/write
# w+ = open for read/write, truncate
# a+ = open for read/append

#add GUI
# add database and database functionality for saved passwords and sites