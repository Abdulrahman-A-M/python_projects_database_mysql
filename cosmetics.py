import os 
import platform
import mysql.connector 
mydb=mysql.connector.connect(user='root',passwd='root',host='localhost',database='cosmetics')
cursor=mydb.cursor()
space=print('-'*10)
def cosmeticsInsert():
    l=[]
    code=int(input("Enter the cosmetic ID number : "))
    l.append(code)
    name=input("Enter the Cosmetics Name : ")
    l.append(name)
    company=input("Enter company ot Cosmetics : ")
    l.append(company)
    cost=int(input('Enter the Cost : '))
    l.append(cost)
    manudate=input('Enter the Date of Manufacture : ')
    l.append(manudate)
    expdate=input('Enter the Date of Expiry : ')
    l.append(expdate)
    val=(l)
    sql="INSERT INTO product(code,name,company,cost,manudate,expdate) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,val)
    mydb.commit()


def customerInsert():
    l=[]
    cust_id=input('Enter the Customer number : ')
    l.append(cust_id)
    cname=input('Enter the Customer Name : ')
    l.append(cname)
    c_phoneno=input('Enter Phone no. of Customer : ')
    l.append(c_phoneno)
    c_address=input('Enter Address : ')
    l.append(c_address)
    gender=input('Enter gender of customer : ')
    l.append(gender)
    membership=input('Enter the membership : ')
    l.append(membership)
    val=(l)

    sql='INSERT INTO customer(cust_id,cname,c_phoneno,c_address,gender,membership) VALUES(%s,%s,%s,%s,%s,%s)'

    cursor.execute(sql,val)
    mydb.commit()


def cosmeticsView():
    print("Select the search criteria : ")
    print("1. Product Id")
    print("2. Product Name")
    print("3. All")
    
    ch=int(input('Enter the choice : '))

    if ch==1:
        s=int(input('Enter Product ID : '))
        rl=(s,)
        sql='SELECT * FROM product WHERE code=%s'

        cursor.execute(sql,rl)
        res=cursor.fetchall()
        for x in res:
            print(x)

    elif ch==2:

        s=input('Enter Product Name : ')
        rl=(s,)
        sql="SELECT * FROM product WHERE name=%s"

        cursor.execute(sql,rl)
        res=cursor.fetchall()
        for x in res:
            print(x)

    elif ch==3:
        sql="SELECT * FROM product"
        cursor.execute(sql)
        res=cursor.fetchall()
        print("The Cosmetics Stock details are as follows : ")
        print("(Cosmetics ID, Cosmetics Name, Cost,Date of Manufacture, Date of Expiry)")
        for x in res:
            print(x)



def viewCustomer():
    print("Select the search criteria : ")
    print("1. Customer ID")
    print("2. Customer Name")
    print("3. All")
    
    ch=int(input('Enter the choice : '))

    if ch==1:
        s=int(input('Enter Customer ID : '))
        rl=(s,)
        sql='SELECT * FROM customer WHERE cust_id=%s'

        cursor.execute(sql,rl)
        res=cursor.fetchall()
        for x in res:
            print(x)

    elif ch==2:

        s=input('Enter Customer Name : ')
        rl=(s,)
        sql="SELECT * FROM customer WHERE cname=%s"

        cursor.execute(sql,rl)
        res=cursor.fetchall()
        for x in res:
            print(x)

    elif ch==3:
        sql="SELECT * FROM customer"
        cursor.execute(sql)
        res=cursor.fetchall()
        print("The Cosmetics Stock details are as follows : ")
        print("(Customer ID, Costomer Name, Cost ,Date of Manufacture, Date of Expiry)")

        for x in res:
            print(x)


def   CustomerPurchase():
    print("Please enter the details to purchase cosmetics product")

    sql='SELECT * FROM product'
    cursor.execute(sql)
    res=cursor.fetchall()
    print('The Cosmetics Stock details are as follows : ')
    print('(Cosmetics ID, Cosmetics Name, Cost, Date of Manufacture, Date of Expiry)')

# WHAT IS HAPPEND HERE.
    for x in res:
        print(x)
        cost=0.0
        ch='y'

    while (ch!='n'):
        c1=input('Enter the items to be purchased : ')       
        r1=(c1,)
        sql="SELECT cost FROM product WHERE name=%s"
        cursor.execute(sql,r1)
        res=cursor.fetchall()
        tsum=0
        
        for x in res:
            cost=float(x[0])
            print(cost)
            q1=int(input('Enter the item quantity : '))
            cc=q1*cost
            print(cc)
            tsum=tsum+cc
            ch=input("Want to purchase more items y/n : ")
            print("Total cost of item purchased is Rs,",tsum)
######################################################################

def removeCosmetics():
    name=input("Enter the cosmetics name to be deleted : ")
    rl=(name,)
    sql="DELETE FROM product WHERE name=%s"
    cursor.execute(sql,rl)

    sql="DELETE FROM customer WHERE cname=%s"
    cursor.execute(sql,rl)
    mydb.commit()


def MenuSet():#Function For The order Management System.
    print("Enter 1 : To Add cosmetics product")
    space
    print("Enter 2 : To View Complete Cosmetics Stock")
    space
    print("Enter 3 : To Purchase any cosmetics Product ")
    space
    print("Enter 4 : To Remove any Cosmetic product")
    space
    print("Enter 5 : To Add Customer Details")
    space
    print("Enter 6 : To View Customer Details")

    try:
        #Using Exceptions For Validation
       userInput=int(input("Please Select An Above Options: "))

    except ValueError:
        exit("\nHy! That's Not A Number ")
    else:
        if userInput == 1:
            cosmeticsInsert()

        elif (userInput == 2):
             cosmeticsView()

        elif (userInput == 3):
             CustomerPurchase()
        
        elif (userInput == 4):
             removeCosmetics()
        
        elif (userInput == 5):
            customerInsert()
        
        elif (userInput == 6):
             viewCustomer()
        
        else:
            print('Enter Correct choice. . . ')

MenuSet()

def runAgain():
    runAgn=input('\nwant To Run Again Y/n: ')
    while runAgn.lower()=='y':
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))

        MenuSet()  
        runAgn=input('\want To Run Again Yes|NO ?: ')
    print('Good Bye')

runAgain()
