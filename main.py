from tkinter import *
from datetime import date

root = Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calcultor")

mylabel = Label(text="Write Details")
mylabel.pack(padx=15,pady=15)

def calculateage():
    today = date.today()
    birthdate = date(int(yearentry.get()),int(monthentry.get()),int(dayentry.get()))
    age = today.year - birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    Label(text=f"{namevalue.get()} your age is {age}",font=30).place(x=300,y=500)



Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)


namevalue = StringVar()
yearvalue = StringVar()
monthvalue = StringVar()
dayvalue = StringVar()

nameentry = Entry(root,textvariable=namevalue,width=30,bd=3,font=20)
nameentry.place(x=300,y=250)

yearentry = Entry(root,textvariable=yearvalue,width=30,bd=3,font=20)
yearentry.place(x=300,y=300)

monthentry = Entry(root,textvariable=monthvalue,width=30,bd=3,font=20)
monthentry.place(x=300,y=350)

dayentry = Entry(root,textvariable=dayvalue,width=30,bd=3,font=20)
dayentry.place(x=300,y=400)

Button(text="Calculate Age",font=20,bg="black",fg="white",width=11,height=2,command=calculateage).place(x=300,y=450)


mainloop()