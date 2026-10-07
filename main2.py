#Weight converter
from tkinter import *
import tkinter.font as font

#Set up
root = Tk()
root.geometry("500x250")
root.title("Weight Convertor")

#Label
kg_to_lb = Label(root, text = "Kilograms to Pounds Converter", fg = "blue")
kg_to_lb.pack(pady = 10)

#Frame
frame = Frame(root)
frame.pack(pady = 10)

#Label
enter_weight = Label(frame, text = "Enter kilograms", fg = "green")
enter_weight.grid(row = 0, column = 0)

#Entry
weight_entry = Entry(frame, width = 15)
weight_entry.grid(row = 0, column = 1)

#Label
error_msg = Label(frame, text = "Invalid Input !", fg = "red")

#Label
lbs = Label(frame, font = font.Font(size = 8))
lbs.grid(row = 2, column = 0)

#Function
def check_value():
    weight = weight_entry.get()
    if(weight.replace(".","").isnumeric()):
        error_msg.grid_forget()

        pounds = float(weight) * 2.2046
        lbs.config(text = "Weight in Pounds : " + str(pounds))

    else:
        error_msg.grid(row = 1, column = 0)

#Button
convert = Button(frame, text = "Convert", bg = "light pink", command = check_value)
convert.grid(row = 3, column = 0)

root.mainloop()