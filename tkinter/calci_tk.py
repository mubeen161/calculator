from ast import Add, operator
from tkinter import * 
cal=Tk()
cal.geometry("354x460")
cal.title("Calculator")
callable=Label(cal,text="Calculator",width=13, bg="salmon",font=("Times",30,"bold"))
callable.pack(side=TOP)
cal.config(background="light blue")
textin=StringVar()
operator=""

def clkbt(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)
def eqlbt():
    global operator
    add=str(eval (operator))
    textin.set(add)
    operator=""
def eqlbt():
    global operator
    sub=str(eval (operator))
    textin.set(sub)
    operator=""
def eqlbt():
    global operator
    mul=str(eval (operator))
    textin.set(mul)
    operator=""
def eqlbt():
    global operator
    div=str(eval (operator))
    textin.set(div)
    operator=""
def clrbt():
    textin.set("")
caltext=Entry(cal,font=("Axial",18,"bold"),textvar=textin,width=25, bg="wheat")
caltext.pack()

but1=Button(cal,padx=14,pady=14,bd=4,bg="beige",command=lambda:clkbt(1),text="1",font=("Verdana",16,"bold"))
but1.place(x=10,y=100)
but1=Button(cal,padx=14,pady=14,bd=4,bg="silver",command=lambda:clkbt(2),text="2",font=("Verdana",16,"bold"))
but1.place(x=10,y=170)
but1=Button(cal,padx=14,pady=14,bd=4,bg="light pink",command=lambda:clkbt(3),text="3",font=("Verdana",16,"bold"))
but1.place(x=10,y=240)
but1=Button(cal,padx=14,pady=14,bd=4,bg="beige",command=lambda:clkbt(4),text="4",font=("Verdana",16,"bold"))
but1.place(x=75,y=100)
but1=Button(cal,padx=14,pady=14,bd=4,bg="silver",command=lambda:clkbt(5),text="5",font=("Verdana",16,"bold"))
but1.place(x=75,y=170)
but1=Button(cal,padx=14,pady=14,bd=4,bg="light pink",command=lambda:clkbt(6),text="6",font=("Verdana",16,"bold"))
but1.place(x=75,y=240)
but1=Button(cal,padx=14,pady=14,bd=4,bg="beige",command=lambda:clkbt(7),text="7",font=("Verdana",16,"bold"))
but1.place(x=140,y=100)
but1=Button(cal,padx=14,pady=14,bd=4,bg="silver",command=lambda:clkbt(8),text="8",font=("Verdana",16,"bold"))
but1.place(x=140,y=170)
but1=Button(cal,padx=14,pady=14,bd=4,bg="light pink",command=lambda:clkbt(9),text="9",font=("Verdana",16,"bold"))
but1.place(x=140,y=240)
but1=Button(cal,padx=14,pady=14,bd=4,bg="wheat",command=lambda:clkbt("/"),text="/",font=("Verdana",16,"bold"))
but1.place(x=205,y=100)
but1=Button(cal,padx=15,pady=14,bd=4,bg="grey",command=lambda:clkbt("-"),text="-",font=("Verdana",16,"bold"))
but1.place(x=206,y=170)
but1=Button(cal,padx=14,pady=14,bd=4,bg="salmon",command=lambda:clkbt("*"),text="*",font=("Verdana",16,"bold"))
but1.place(x=205,y=240)
but1=Button(cal,padx=48,pady=14,bd=4,bg="tan",command=lambda:clkbt(0),text="0",font=("Verdana",16,"bold"))
but1.place(x=10,y=310)
but1=Button(cal,padx=15,pady=14,bd=4,bg="tan",command=lambda:clkbt(")"),text=")",font=("Verdana",16,"bold"))
but1.place(x=205,y=310)
but1=Button(cal,padx=18,pady=14,bd=4,bg="tan",command=lambda:clkbt("("),text="(",font=("Verdana",16,"bold"))
but1.place(x=140,y=310)
but1=Button(cal,padx=48,pady=14,bd=4,bg="sky blue",command=eqlbt,text="=",font=("Verdana",16,"bold"))
but1.place(x=70,y=370)
but1=Button(cal,padx=15,pady=14,bd=4,bg="teal",command=lambda:clkbt("%"),text="%",font=("Verdana",16,"bold"))
but1.place(x=205,y=370)
but1=Button(cal,padx=18,pady=14,bd=4,bg="light green",command=lambda:clkbt("00"),text="00",font=("Verdana",16,"bold"))
but1.place(x=10,y=370)
but1=Button(cal,padx=9,pady=48,bd=4,bg="dark khaki",command=clrbt,text="AC",font=("Verdana",16,"bold"))
but1.place(x=270,y=100)
but1=Button(cal,padx=15,pady=42,bd=4,bg="coral",command=lambda:clkbt("+"),text="+",font=("Verdana",16,"bold"))
but1.place(x=270,y=240)
but1=Button(cal,padx=19,pady=14,bd=4,bg="sea green",command=lambda:clkbt("."),text=".",font=("Verdana",16,"bold"))
but1.place(x=270,y=370)
mainloop()