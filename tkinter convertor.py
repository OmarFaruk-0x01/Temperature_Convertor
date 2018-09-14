from tkinter import *
root=Tk()
root.geometry("690x450")
root.title("Temperature Convertor")
l=Label(root,text='Convertor',font=('arial',10,'bold')).grid(row=0,column=1)
def main():
    c=cles.get()
    f=ferh.get()
    k=klv.get()
    if c:
        f_total=(160+(float(c)*9))/5
        k_total=float(c)+273.15
        ferh.set(str(f_total))
        klv.set(str(k_total))
    elif f:
        c_total=5/9*(float(f)-32.0)
        ke_total=5/9*(float(f)-32.0)+273
        cles.set(str(c_total))
        klv.set(str(ke_total))
    elif k:
        c_total=float(k)-273
        f_total=9 / 5 * (float(k) - 273) + 32
        cles.set(str(c_total))
        ferh.set(str(f_total))
def clear():
	cles.set("")
	ferh.set("")
	klv.set("")
	c=""
	k=''
	f=""
def q():
	root.quit()
opareto=''
l1=Label(root,text='Degree Centigrade:',font=('arial',8,'bold')).grid(row=2,column=0)
cles=StringVar()
en1=Entry(root,textvariable=cles,width=20,bd=10,font=('arial',8,'bold')).grid(row=2,column=1,columnspan=2)

l2=Label(root,text='Degree Fahrenheit:',font=('arial',8,'bold')).grid(row=3,column=0)
ferh=StringVar()
en2=Entry(root,textvariable=ferh,width=20,bd=10,font=('arial',8,'bold')).grid(row=3,column=1,columnspan=2)
l3=Label(root,text='Kalvin:',font=('arial',8,'bold')).grid(row=4,column=0)
klv=StringVar()
en3=Entry(root,textvariable=klv,width=20,bd=10,font=('arial',8,'bold')).grid(row=4,column=1,columnspan=2)

b=Button(root,text='convert',padx=20,command=lambda:main()).grid(row=5,column=1)
b1=Button(root,text='clear',padx=20,command=clear).grid(row=5,column=2)
b2=Button(root,text='Exit',padx=20,command=q).grid(row=7,column=2)
lab=Label(root,text="Help: Input temperature in any scale \nclick convert\nIt will convert All scale",font=('arial',8,'bold')).grid(row=6,column=0,columnspan=3)
root.mainloop()