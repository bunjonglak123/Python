from tkinter import *
f=Tk()
f.title("loop")
f.minsize(600,600)
f.maxsize(600,600)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()

s21=StringVar()

l1 = Label (f,text="ชื่อ")
l1.place(x=100,y=100)

l2 = Label (f,text="คะแนน")
l2.place(x=300,y=100)

e1 = Entry (f,textvariable=s1)
e1.place(x=100,y=200)

e2 = Entry (f,textvariable=s2)
e2.place(x=300,y=200)

e3 = Entry (f,textvariable=s3)
e3.place(x=100,y=220)

e4 = Entry (f,textvariable=s4)
e4.place(x=300,y=220)





from csv import *

def xxx():
    with open ("b.csv",'w') as f:
            w = writer(f,lineterminator='\n')
            w.writerow([s1.get(),s2.get()])
            w.writerow([s3.get(),s4.get()])
    

            
def yyy():
    with open("b.csv",'r') as f:
        r = reader (f)
        l = list (r)
        s1.set(l[0][0])
        s2.set(l[0][1])
        s3.set(l[1][0])
        s4.set(l[1][1])

def zzz():
    with open ("b.csv",'r') as f:
        L=[]
        L.append(int(s2.get()))
        L.append(int(s4.get()))
        s5.set(str(sum(L) / len(L)))
l3 = Label (f,text="mean")
l3.place(x=150,y=420)

l4 = Label (f,textvariable=s5)
l4.place(x=300,y=420)

d1 = Button (f,text="save",command=xxx)
d1.place(x=100,y=500)

d2 = Button (f,text="load",command=yyy)
d2.place(x=200,y=500)

d3 = Button (f,text="cal",command=zzz)
d3.place(x=300,y=500)

f.mainloop