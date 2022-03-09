from asyncio import windows_events
import tkinter
import csv
from tkinter import NSEW, RIGHT, VERTICAL, Scrollbar, scrolledtext
from turtle import left
# new interface for equipment
window = tkinter.Tk()
window.title("List of All Equipments")

# frame
frame_a= tkinter.Frame(master=window)
frame_b=tkinter.Frame(master=window)
frame_a.grid(row=0, column=1)
frame_b.grid(row=0, column=0)

with open("newequipments.csv") as equipmentdata:
   equipmentprint = csv.reader(equipmentdata)

   # r and c tell us where to grid the labels
   r = 0
   for rw in equipmentprint:
      c = 0
      for colum in rw:
         # i've added some styling
        label = tkinter.Label(frame_b , width = 15, height = 2, text = colum, relief = tkinter.RIDGE)
        label.grid(row = r, column = c)
        c = c+1
      r = r+ 1

# open file




#frame_b.pack(side=tkinter.TOP, fill=tkinter.Y)

#frame_a.pack(side=tkinter.RIGHT)
B_employee = tkinter.Button(frame_a, text ="close",width=15, command=window.destroy)
B_employee.grid(row=0, column=0)
#B_employee.pack(side=tkinter.TOP)






window.mainloop()