print("."*50)
print("                 BU RESTAURANT")
print("                      MENU")
print("."*50)
print(" MENU  ID           MENU                               PRICE ")
print(" F01                pan fried egg                       125 ")
print(" F02                grill sanwqndwich                   145 ")
print(" F03                spaghetti olio                      169 ")
print(" F04.               caesar salad                        139 ")
print(" D01                coffe                               120 ")
print(" D02                sofe drink                           90 ")
print("."*50)
con="N"
qtylist=[]
orderlist=[]
foodprice=0
pricelist=[]
drinkprice=0
total=0
menulist = ["F01","F02","F03","F04","D01","D02"]
mb=""
while con != "Y":
  menu =input("Enter Menu ID : ").upper()
  if menu in menulist:
    qty =int(input("enter quantuty : "))
    qtylist.append(qty)
    if menu == "F01" :
      price=125*qty
      foodprice=foodprice+price
      orderlist.append("pan fried egg")
    elif menu == "F02" :
      price=145*qty
      foodprice =foodprice+price
      orderlist.append("grilled sandwich")
    elif menu == "F03" :
      price=169*qty
      foodprice=foodprice+price
      orderlist.append("spaghetti olio")
    elif menu == "F04" :
      price=139*qty
      foodprice=foodprice+price
      orderlist.append("caesar salad")
    elif menu == "D01" :
      price=120*qty
      drinkprice=drinkprice+price
      orderlist.append("coffee")
    elif menu =="D02" :
      price=90*qty
      drinkprice=drinkprice+price
      orderlist.append("sofe drink")
    pricelist.append(price)
  con=input("Quit Y/N : ").upper()
  mb=str(input("BU MEMBER Y/N : ")).upper()
print("."*50)
print("                      BU RESTAURANT")
print("                         receipt")
print("."*50)
print("menu                            QTY                           price " )
i = 0

while i < len(orderlist):
  print("%-30s %-20d %d"%(orderlist[i],qtylist[i],pricelist[i]))
  i=i+1
bu=foodprice*7/100
total=foodprice+drinkprice
print("."*50)
print("Price                                                             %.2f"%total)
if mb == 'Y':
    print("Discount (only member ) %.2f"%bu)
