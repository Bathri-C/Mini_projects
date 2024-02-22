# from tkinter import *
# window=Tk()
# window.title("My first GUI Programm")
# window.minsize(500,300)

# my_label=Label(text="Shivaji the boss")
# my_label.grid(column=0,row=0)

# button_1=Button(text="press")
# button_1.grid(column=1,row=1)

# button_2=Button(text="Cilck me")
# button_2.grid(column=2,row=0)

# entry_1=Entry()
# entry_1.grid(column=10,row=10)

# window.mainloop()
def mile_to_km():
    miles=float(input_1.get())
    km=miles*1.609
    my_label4.config(text=f"{km}")

from tkinter import *

window=Tk()
window.title("Mile to KM convertor")
window.minsize(100,100)
window.config(padx=30,pady=30)

my_label1=Label(text="is equal to")
my_label1.grid(column=0,row=1)

my_label2=Label(text="Miles")
my_label2.grid(column=2,row=0)

my_label3=Label(text="Km")
my_label3.grid(column=2,row=1)

input_1=Entry(width=10)
input_1.grid(column=1,row=0)

my_label4=Label(text="0")
my_label4.grid(column=1,row=1)

button=Button(text="Calculate",command=mile_to_km)
button.grid(column=1,row=2)




window.mainloop()



