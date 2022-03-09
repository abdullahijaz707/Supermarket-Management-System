from asyncio import windows_events
import tkinter
import csv
from tkinter import RIGHT, VERTICAL, Scrollbar, scrolledtext
from turtle import left


window = tkinter.Tk()
window.title("List of All Inventory")


with open("newinventory.csv", newline = "") as inventorydata:
   inventoryprint = csv.reader(inventorydata)

   # r and c tell us where to grid the labels
   r = 0
   for colum in inventoryprint:
      c = 0
      for row in colum:
         # i've added some styling
         label = tkinter.Label(window, width = 15, height = 3, text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c = c+1
      r = r+ 1

# open file




#frame_b.pack(side=tkinter.TOP, fill=tkinter.Y)

#frame_a.pack(side=tkinter.RIGHT)
B_employee = tkinter.Button(window, text ="Disply all Inventory", )
#B_employee.pack(side=tkinter.TOP)






window.mainloop()