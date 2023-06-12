import random
import string
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

def Welcome():
    print("Welcome to PassGen  \n")

passLength = 0

def GetPassLength():
    global passLength
    passLength = int(input("enter the length of the password: "))
    passLength = int(passLength)
    
    try:
        passLength = int(passLength)
        if passLength != type(int):
            print("Checkpoint 1")
    except ValueError:
        print("Please enter an integer...")
        GetPassLength()
        
    return passLength
    
def GenPassword(length):
    
    #Possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #generates password with defined characters 
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

Welcome()
GetPassLength()
password = GenPassword(passLength)
print('Your password is: ' + password)






# file io
# syntax - animals = open('animals.txt', 'a+')
# r = open for read (default)
# w = open for write, truncate
# r+ = open for read/write
# w+ = open for read/write, truncate
# a+ = open for read/append

#add GUI
# add database and database functionality for saved passwords and sites