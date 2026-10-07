#Temperature App
from tkinter import *
import tkinter.font as font

#Set up
root = Tk()
root.geometry("500x250")
root.title("Celsius to Farenheit Converter")

#Label
c_to_f = Label(root, text = "Celsius to Farenheit", fg = "purple", font = font.Font(size = 20))
c_to_f.pack(pady = 10)

#Frame
frame = Frame(root)
frame.pack(pady = 10)

#Label
enter_temp = Label(frame, text = "Enter in Celsius: ", font = font.Font(size = 10))
enter_temp.grid(row = 0, column = 0)

#Entry
c_temp = Entry(frame, width = 15)
c_temp.grid(row = 0, column = 1)

#Label
error_message = Label(frame, text = "Please enter valid input...", font = font.Font(size = 8), fg = "red")

#Label
f_temp = Label(frame, font = font.Font(size = 10))
f_temp.grid(row = 2, column = 0, columnspan = 2, pady = 10)

#Function
def transfer():
    celsius = c_temp.get()
    if(celsius.replace(".","").isnumeric()):
        error_message.grid_forget()

        farenheit = (float(celsius) * 9/5) + 32
        f_temp.config(text = "Temperature in Farenheit : " + str(farenheit))

    else:
        error_message.grid(row = 1, column = 1)

#Button
convert = Button(frame, text = "Convert", bg = "light green", fg = "blue", command = transfer)
convert.grid(row = 3, column = 0)

root.mainloop()