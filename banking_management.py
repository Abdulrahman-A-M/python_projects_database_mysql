import os
import mysql.connector
import pandas as pd
import platform

banking_connection=mysql.connector.connect(user='root',passwd='root',host='localhost',database='projects')

mycursor=banking_connection.cursor()



def AccInsert():
    L=[]
    accnum=int(input('Enter the Account number:'))
    L.append(accnum)
    nameuser=input('Enter Customer Name:')
    L.append(nameuser)
    ageuser=int(input('Enter Age customer:'))
    L.append(ageuser)
    occupation=input('Enter customer Occupation:')
    L.append(occupation)
    addr=int(input('Enter address of customer:'))
    L.append(addr)
    mobileuser=int(input('Enter customer mobile number:'))
    L.append(mobileuser)
    nationaladdress=input('Enter National address:')
    L.append(nationaladdress)
    mony_deposited=int(input('Enter the money deposited:'))
    L.append(mony_deposited)
    AccType=input("Enter the Account Type (Saving/RD/PPF/Current):")
    L.append(AccType)

    cust=(L)

    sql="""INSERT INTO ACCOUNT(accnum,nameuser,ageuser,occupation,addr,mobileuser,nationaladdress,mony_deposited,AccType)
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""#########################

    mycursor.execute(sql,cust)
    banking_connection.commit()

def AccView():

    print('Select the search criteria')
    print('1.Acc no')
    print('2.name')
    print('3.Mobile')
    print('4.national address')
    print('5.view all')
    
    ch=int(input("Enter the choice:"))

    if ch==1:
      accno=int(input("Enter Account number:"))
      a=(accno,)###########################
      sql="SELECT * FROM ACCOUNT WHERE accnum=%s"
      mycursor.execute(sql,a)
      f=mycursor.fetchall()
      print(f)

    elif ch==2:
       name=input('Eenter name customer:')
       n=(name,)
       sql="SELECT * FROM ACCOUNT WHERE nameuser=%s"
       mycursor.execute(sql,n)
       f=mycursor.fetchall()
       print(f)

    elif ch==3:
       mobile=int(input("Enter Mobile Number of customer:"))
       m=(mobile,)
       sql="SELECT * FROM ACCOUNT WHERE mobileuser=%s"
       mycursor.execute(sql,m)
       f=mycursor.fetchall()
       print(f)
    
    elif ch==4:
       national=input("Enter National Address:")
       n=(national,)
       sql="SELECT * FROM ACCOUNT WHERE nationaladdress=%s"
       mycursor.execute(sql,n)
       f=mycursor.fetchall()
       print(f)

    elif ch==5:
       sql='SELECT * FROM ACCOUNT'
       mycursor.execute(sql)

       res=mycursor.fetchall()

       k=pd.DataFrame(res,columns=['accnum','nameuser','ageuser','occupation','addr','mobileuser','nationaladdress','mony_deposited','AccType'])
        
       print(k)



def AccDeposit():
   L=[]
   accno=int(input("Enter account number of costomer:"))
   L.append(accno,)

   Amtedposit=eval(input("Eenter the Amount to be deposited:"))
   L.append(Amtedposit,)

   month=input("Enter month of salary:")
   L.append(month,)

   cust=(L)

   sql="INSERT INTO amt(aacno,Amtedposit,month) VALUES (%s,%s,%s)"
   mycursor.execute(sql,cust)
   banking_connection.commit()

def accView():
   
  
    
   sql="SELECT account.accnum,account.nameuser,account.ageuser,account.occupation,account.addr,account.mobileuser,account.nationaladdress,account.mony_deposited,account.AccType,amt.aacno,amt.Amtedposit,amt.month FROM account INNER JOIN amt ON account.accnum=amt.aacno"


   mycursor.execute(sql)
   res=mycursor.fetchall()

   for x in res:
      print(x)

def closeAcc():
    
    Accno=int(input("Enter the Account number of the Customer to be closed:"))
    rl=(Accno,)
    sql="DELETE FROM amt WHERE aacno=%s"
    mycursor.execute(sql,rl)
    banking_connection.commit()

    sql="DELETE FROM account WHERE accnum=%s"
    mycursor.execute(sql,rl)
    banking_connection.commit()

def MenuSet():
   print("Enter 1:To Add Customer")
   print("Enter 2:To View Customer")
   print("Enter 3:To Deposit Money")
   print("Enter 4:To Close Account")
   print("Enter 5:To View All Customer Details")
   
   try:
      userinput=int(input("Select An Above Option:"))

   except ValueError:
      exit("\n Hy!That's Not A Number")
    
   else:
      print("\n")

      if userinput==1:
         AccInsert()
      
      elif userinput==2:
         AccView()

      elif userinput==3:
        AccDeposit()
      elif userinput==4:
         closeAcc()

      elif userinput==5:
         accView()
      else:
         print("Enter correct choice...")
    
MenuSet()

def runAgain():
    runAgain=input("\nwant To Run Again Y/n:")

    while(runAgain.lower()=='y'):
 
          MenuSet()
          runAgain=input("\nWant To Run Again Y/n:")

runAgain()
    
          

    



       
   



