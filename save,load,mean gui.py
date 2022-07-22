from tkinter import*
f = Tk()
f.title("คำนวนคะแนน")
f.minsize(600,600)
f.maxsize(600,600)


s1 = StringVar()

s2 = StringVar()

s3 = StringVar()

s4 = StringVar()

s5 = StringVar()

l1 = Label(f,text="ชื่อ")
l1.place(x=50,y=20)

l2 = Label(f,text="คะแนน")
l2.place(x=200,y=20)

e1 = Entry(f,textvariable=s1)
e1.place(x=50,y=50)

e2 = Entry(f,textvariable=s2)
e2.place(x=200,y=50)

e3 = Entry(f,textvariable=s3)
e3.place(x=50,y=100)

e4 = Entry(f,textvariable=s4)
e4.place(x=200,y=100)

l4 = Label(f,text="ค่าเฉลี่ย =",font=500)
l4.place(x=100,y=200)


from csv import*
def xxx():
   with open("b.csv",'w') as  f:
      w = writer(f,lineterminator='\n')
      w.writerow([s1.get(),s2.get()])
      w.writerow([s3.get(),s4.get()])
d = Button(f,text="SAVE",command=xxx)
d.place(x=100,y=350)

def yyy():
   with open("b.csv",'r') as f:
      r = reader(f)
      l = list(r)
      s1.set(l[0][0])
      s2.set(l[0][1])
      s3.set(l[1][0])
      s4.set(l[1][1])
d1 = Button(f,text="LOAD",command=yyy)
d1.place(x=150,y=350)

def zzz():
   with open("b.csv",'r') as f:
      L = []
      L.append(int(s2.get()) )
      L.append(int(s4.get()) )
      s5.set( str ( sum(L) / len(L) ) )
      
l3 = Label(f,textvariable=s5,font=500)
l3.place(x=200,y=200)

d1 = Button(f,text="CALCULATOR",command=zzz)
d1.place(x=250,y=350)

f.mainloop