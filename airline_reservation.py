import os
import platform
import mysql.connector
import datetime

mydb=mysql.connector.connect(user='root',password='root',host='localhost',database='projects')
mycursor=mydb.cursor()
def registecust():
    L=[]
    custno=int(input('Enter customer no='))
    L.append(custno)
    name=input('Enter customer name:')
    L.append(name)
    addr=input('Enter address:')
    L.append(addr)
    jr_date=input('Enter date of journey:')
    L.append(jr_date)
    source=input('Enter source:')
    L.append(source)
    destination=input('Enter destination:')
    L.append(destination)
    cust=L
    #mycursor.execute("CREATE TABLE pdata(custno INT, custname CHAR(20),addr CHAR(10),jrdate CHAR(10),source CHAR(10),destination CHAR(10))")
    
    sql="INSERT INTO pdata(custno,custname,addr,jrdate,source,destination)VALUE(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)

    mydb.commit()

def ticketprice():
    L=[]
    cno= int(input("Eenter custoner on="))
    L.append(cno)
    print('We havethe ticket price for you:-')
    print('1. type First class-->riyal 6000 PN')
    print('2. type Business class--->riyal 4000 PN')
    print('3. type Economy class --->riyal 2000 PN')
    x=int(input('Enter your choice:'))
    L.append(x)
    y=int(input('Enter ON. of passengers:'))
    
    if x==1:
        print('you have opted First class.')
        s=6000*y

    elif x==2:
        print('you have opted Business class.')
        s=4000*y

    elif x==3:
        print('you have opted Economy class.')
        s=2000*y

    else:
        print('Please select a class type.')

    print('you ticker charge is=',s,'\n')
    print('Extra luggage charge 100 riyal per kg')

    y=int(input('Enter weight,of extra luggage:'))
    lug_tot=y*100
    L.append(lug_tot)
    

    print('Your totalbill:',s+lug_tot,'\n')
    g_tot=s+lug_tot
    L.append(g_tot)

    tkt=(L)
    #c_sql="""CREATE TABLE tkt(custon INT,tkt_tot INT,lug_tot INT,g_tot INT)"""
    #mycursor.execute(c_sql)
    
    sql="INSERT INTO tkt(custon,tkt_tot,lug_tot,g_tot)VALUE(%s,%s,%s,%s)"
    mycursor.execute(sql,tkt)
    mydb.commit()


def dis():
    custon=int(input("Enter the custmer number whose bill to be viewed : "))

    sql="SELECT * FROM pdata INNER JOIN tkt ON pdata.custno=tkt.custon AND tkt.custon =%s"
    rl=(custon,)
    mycursor.execute(sql,rl)
    result=mycursor.fetchall()

    for i in result:
        print(i)

def dispall():
    sql="SELECT pdata.custno,pdata.custname,pdata.addr,pdata.jrdate,pdata.source,pdata.destination,tkt.custon,tkt.tkt_tot,tkt.lug_tot,tkt.g_tot FROM pdata INNER JOIN tkt ON pdata.custno=tkt.custon "
    mycursor.execute(sql)
    res=mycursor.fetchall()
    
    print("The customer details are as follows: ")

    for x in res:
        print(x)


def Menuset():
    print("Enter 1: To enter customer data.")
    print("Enter 2: For ticketamount.")
    print("Enter 3: Display customerwise Details.")
    print("Enter 4: Display All Details.")
    print("Enter 5: To Exit.")
   
    user=int(input("Enter your choice:"))

    if user==1:
        registecust()
    elif user==2:
        ticketprice()
    elif user==3:
        dis()
    elif user==4:
        dispall()
    elif user==5:
        quit()

    else:
        print("Enter correct choice.")

Menuset()

def runagain():
    runagn=input('\nWant to run again? y/n:')
    while runagn=='y':
        if platform.system=='windows':
            print(os.system('cls)'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input('\nWant to run again? y/n:')

runagain()