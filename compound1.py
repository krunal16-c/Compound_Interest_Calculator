# importing all the required libraries
from tkinter import *


# function to clear all fields
def clear_all():
    principle_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)

    principle_field.focus_set()  # setting focus on principle_field

# function to calculate compound interest
def calculate_ci():
    principle = float(principle_field.get())
    rate = float(rate_field.get())
    time = float(time_field.get())

    # calculate compound interest
    CI = float(principle * (pow((1 + rate/100),time)))

    # inserting the value compound_field box
    compound_field.insert(10,CI)


# creating a GUI
root = Tk()
root.configure(background = 'lavender') # setting the background color of GUI window
root.geometry("500x350") # determining the size of GUI window
root.title("Compound Interest Calculator") # setting the title of the window

label1 = Label(root, text = "Principle Amount(Rs) :", fg = 'black', bg = '#e3f2fd') # principle amount label
label2 = Label(root, text = "Rate(%):", fg = 'black', bg = '#e3f2fd') # rate label
label3 = Label(root, text = "Time(Years):", fg = 'black', bg = '#e3f2fd') # creating a time label
label4 = Label(root, text = "Compound Interest:", fg = 'black', bg = '#e3f2fd') # compound interest label

# grid method is used to add widgets at respective positions in table like structure
# padx keyword for padding along x axis and pady for padding along y axis
label1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
label3.grid(row=3, column=0, padx=10, pady=10)
label4.grid(row=5, column=0, padx=10, pady=10)

# creating a entry field to enter filling info
principle_field = Entry(root)
rate_field = Entry(root)
time_field = Entry(root)
compound_field = Entry(root)

principle_field.grid(row=1, column=1, padx=10, pady=10)
rate_field.grid(row=2, column=1, padx=10, pady=10)
time_field.grid(row=3, column=1, padx=10, pady=10)
compound_field.grid(row=5, column=1, padx=10, pady=10)

# creating a submit button and attaching it to a function
button1 = Button(root, text="Submit", bg="light blue", fg="black", command = calculate_ci)

# creating a clear all button
button2 = Button(root, text="Clear all", bg="light blue", fg="black", command = clear_all)

button1.grid(row=4, column=1, pady=10)
button2.grid(row=6, column=1, pady=10)

root.mainloop() # starting the GUI
