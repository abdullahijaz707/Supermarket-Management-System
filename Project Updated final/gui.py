
from cProfile import label
from cgitb import text
from doctest import master
from tkinter import BOTTOM, GROOVE, RAISED, RIGHT, font

from turtle import bgcolor, color, left, right
import tkinter
import tkinter.messagebox
import csv

from numpy import size

# for opening csv file

with open("newstaff.csv") as file:
   reader = csv.reader(file)

# new gui window
topwindow = tkinter.Tk()

#function  for new window
def openNewWindow():
     
    newWindow = tkinter.Toplevel(topwindow)
    newWindow.title("New Window")
    
    n_w_button=tkinter.Button(newWindow, text="close", command=newWindow.destroy)
    n_w_button.pack()
    
   


# Code to add widgets will go here...
#title.
topwindow.title("Super Market Management system")

#frame for welcome note

frame_welcome= tkinter.Frame(master=topwindow, height=300, pady=3)
frame_welcome.pack(side=tkinter.TOP) # pack is for completion of item

# welcome note is label

w_lable= tkinter.Label(master=frame_welcome, text="Welcome to the Super Market Management system", font=("georgia", 25), width = 150, height = 5, bg='black',fg='yellow')
w_lable.pack() 

# frame for button

frame_button= tkinter.Frame(master=topwindow )
frame_button.pack(side = tkinter.TOP, pady=6)

# label for button
i_label= tkinter.Label(frame_welcome, text="What would you like to see?", font=("georgia", 25),pady=30)
i_label.pack()

#buttons

B_inventry = tkinter.Button(frame_button, text ="Display all Inventory",command= openNewWindow,width = 20, height = 5, bg='#266694')
B_employee = tkinter.Button(frame_button, text ="Display all Employees", command= openNewWindow,width = 20, height = 5, bg='#266694' )
B_equipment = tkinter.Button(frame_button, text ="Display all Equipment",command= openNewWindow,width = 20, height = 5, bg='#266694')

B_inventry.grid(row=0 , column=1) # grid for arrangment
B_employee.grid(row=0, column=2)  #  grid for arrangment
B_equipment.grid(row=0, column=3) # grid for arrangment

# choice frame
ch_frame= tkinter.Frame(master=topwindow)
ch_frame.pack()
t_label= tkinter.Label(ch_frame, text="How would you like to search?", font=("georgia", 25))
t_label.grid(row=0,column=0, pady=5)


# Text box frame
frame_box = tkinter.Frame(master=topwindow)
frame_box.pack(side = tkinter.TOP)

l_name= tkinter.Label(frame_box, text="Enter Name")
l_name.grid(row=1, column=0 ) # grid for arrangment

# creating text box and labels
s_name= tkinter.Entry(frame_box)
s_name.grid( row=1 , column=1) # grid for arrangment

n_s_button= tkinter.Button(frame_box ,text="search", command=openNewWindow) # name search button
n_s_button.grid(row=1, column=2, padx=20) # grid for arrangment

id_label= tkinter.Label(frame_box, text="Enter ID") #Id label
id_label.grid(row=2,column=0, padx=20) # grid for arrangment

s_id= tkinter.Entry(frame_box) # id entry box
s_id.grid(row=2,column=1,  padx=20) # grid for arrangment

id_s_button= tkinter.Button(frame_box ,text="search", command=openNewWindow) # id serach button
id_s_button.grid(row=2, column=2) # grid for arrangment


#Frame for closing window 
close_frame= tkinter.Frame(master=topwindow)
close_frame.pack(side=RIGHT)
cl_button= tkinter.Button(master=close_frame, text="Close" , padx=50, command=topwindow.destroy) # for close button
cl_button.pack(side=RIGHT)


topwindow.geometry("900x600+20+20")
topwindow.mainloop()
