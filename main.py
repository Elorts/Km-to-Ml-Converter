from tkinter import *

# Calculate clicked
def calculate_clicked():
    miles = float(miles_entered.get())
    km = round(miles * 1.609)
    r_label.config(text=f"{km}")

# Window
window = Tk()
window.title("mile to Km Converter")
window.minsize(width=60, height=30)
window.config(padx=20, pady=20)

# Entry
miles_entered = Entry(width=7)
miles_entered.grid(column=1, row=0)

# ML Label
ml_label = Label(text="Miles")
ml_label.grid(column=2, row=0)

# Is Equil Label
ie_label = Label(text="is equal to")
ie_label.grid(column=0, row=1)

# Result Label
r_label = Label(text="0")
r_label.grid(column=1, row=1)

# KM Label
km_label = Label(text="0")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate_clicked)
button.grid(column=1, row=2)

window.mainloop()