from asyncio import windows_events
import tkinter
import csv
from tkinter import RIGHT, VERTICAL, Scrollbar, scrolledtext
from turtle import left

window = tkinter.Tk()
window.title("List of All Staff Members")
   
 
 

with open("newstaff.csv", newline = "") as staffdata:
   staffprint = csv.reader(staffdata)

   # r and c tell us where to grid the labels
   r = 0
   for colum in staffprint:
      c = 0
      for row in colum:
         # i've added some styling
         label = tkinter.Label(window, width = 15, height = 3, text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c = c+1
      r = r+ 1


window.mainloop()