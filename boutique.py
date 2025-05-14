import mysql.connector

mycon=mysql.connector.connect(user='root',passwd='root',host='localhost',database='sboutique')

mycur=mycon.cursor()

def space():  
    for i in range(1):
        print()

"""
This function is being used to return a list of IDs of all the customers in the boutique. At the time of a customer 
login or new customer, it is used to check if the customer with this ID already exists or not."""

def Check():

    sql='SELECT c_ID FROM customer'

    mycur.execute(sql)
    
    d=mycur.fetchall()

    list_of_ids=[]                      
    for ids in d:                      
        list_of_ids.append(ids[0])    
                                      
    return list_of_ids                  


"""
The customer account function asks customers to enter their customer ID and it checks if a customer with this ID already exists or not because customer ID is a primary key in the customer table in the database and the values entered in these columns must be unique. If the customer exists it displays a message, 
else it takes the customer’s details and inserts the record in the customer table of the database."""
def cust_ac():
    ask='Y'
    list_of_ids=Check()

    while ask in 'Y':
        cusid= int(input('Enter your customer ID...'))
        #To check if a customer already exists with this ID.
        if cusid in list_of_ids:
            print('This Customer Id alreay exists...\nTry creating a new one')
            
        else:
            c_det=()
            cnam=input('First Name: ')
            clnam=input('Last Name: ')
            cphno=input('phone Number: ')
            cadrs=input('Your Address:')
            c_det=(cusid,cnam,clnam,cphno,cadrs)
       
            sql='INSERT INTO customer values(%s,%s,%s,%s,%s,NULL)'
            val=c_det
            mycur.execute(sql,val)
            mycon.commit()
            print('Customer details entered')
            ask=input('Do you want to continue (Y/N)')
            if ask not in ('Y'):
                space()
                break

"""
This function returns a list of products booked by a customer using the customer’s ID. 
It is used in other functions to view or delete the booked orders of the customer."""
            
def get_bkd_pro(c_id):
    qry='SELECT pkd_pro FROM customer WHERE c_ID=%s'
    mycur.execute(qry, (c_id,))
    pd=mycur.fetchone()
    bkd_pro=pd[0]
    return bkd_pro

"""
This function allows the customer to log in to their accounts. It first checks if a customer with entered ID exists or not, and then asks for the customer’s choice to :

View their booked products
    To view the products booked by customers, the get booked product function is used where customer ID is passed as an argument.
    It then checks if the customer has any bookings or not and then displays the result accordingly.
    If more than one product is booked, the product IDs are stored as a single value in the table separated by '_'. The fetched values are then split and printed.
 
Book a new product  
    To book a new product, the function asks the customer to enter the product ID and then checks if the product with the given ID exists in the products table or not. It then adds the product to the booked products column of the customer’s table.
    If the customer already has a booked product, the new product ID is concatenated with the existing ID and again stored in the table.     
Update their existing details
    For the customer to update their account, the function displays the existing customer details and then asks them to enter the fields they want to update.

Cancel booked products     
    To cancel booked products the function asks for product ID and checks if it is booked or not and then deletes it accordingly. """

def sign_in():
   try:
        ask = int(input('Enter customer ID to sign in : '))

        list_of_ids=Check()

        if ask in list_of_ids:
           while True:
               print('''Do you want to: 
                     1) View Bookings
                     2) Book a product
                     3) Update Self Details
                     4) Cancel booked products
                     enter 'back' to exits''')
               
               ccc=input('Enter choice - ')

               if ccc=='1':
                   
                   s=get_bkd_pro(ask)

                   if s is None or s==' ':
                       print('You have not booked products yet')

                   else:
                       
                       d=s.split('_')

                       print('Booked products')
                       for bikitems in d:
                           print(bikitems)


               if ccc=='2':
                   sql='SELECT pro_id FROM products'
                   mycur.execute(sql)
                   pro_list=mycur.fetchall()
                  #We call the product's ID and then put them in a variable called pro_list.
                   list_of_products=[]
                   #This list for append the variables fetched from table PRODUCTS.

                   for i in pro_list:
                       list_of_products.append(i[0])
                        #this is fro append to the list_of_products

                   pro_id=input('Enter the product ID to book products :')
                   #Enter the product_id to book products! 
                    
                   if pro_id in list_of_products:
                    #here if pro_id that is your entered is in list_of_products enter in the code program.

                       qry="SELECT pkd_pro FROM customer WHERE c_ID=%s"
                       mycur.execute(qry,(ask,))
                       pr =mycur.fetchone()
                       # the query he say choice the bkb_pro from table customer where it is mean if cust_ID=%s this mean the varlube i send you replace with %s 
                       #Note when the query fetched is just fetched one is bkb_pro and the bkb_pro is the products of customer 
                       prl=pr[0]
                       #this is store in varuble name is prl after your fetched

                       if prl is None or prl==' ' :
                           qry="UPDATE customer SET pkd_pro=%s WHERE c_ID=%s"
                           val=(pro_id+'_',ask)
                           mycur.execute(qry,val)
                           mycon.commit()
                           print("Your Product is booked !!")
                           #Here if prl is not has any values or data do the code is what is do!
                           #Is do update table customer and send set bkd_pro=%s where is mean for cust_id=%s
                         
                       else:
                           prl1=prl+pro_id
                           qry2=("UPDATE customer SET pkd_pro=%s WHERE c_ID=%s")

                           val2=(prl1+'_',ask)
                           mycur.execute(qry2,val2)
                           mycon.commit()
                           print('Your Product is boooked !!')

                   else:
                       
                        print('This product does not exists.Please write the correct product ID!')

               if ccc=='3':
                   qry='SELECT c_ID,c_name,c_lname,c_phone,c_address FROM customer WHERE c_ID=%s'
                   mycur.execute(qry,(ask,))
                   # clist contains list of all values fetched
                   # in the form of a tuple for this customer ID
                   clist=mycur.fetchone()

                   flds=['Name','Last Name','Ph.No','Address']
                   dic={}
                   print('Your existing record is:')

                    #The fetched details are stored in the form of key
                    # value pair in a dictionary
                   for i in range(4):
                       dic[flds[i]] = clist[i+1]
                       #dic={Name:Abdulrahman,Last Name:aa,Ph.No:0202,Address:asser}################# 
                       print(i+1, '   ',flds[i],' : ',clist[i+1])
                       

                   for i in range(len(clist)):
                       updtc=int(input('Enter choice to update '))
                       upval=input('Enter '+flds[updtc-1]+'  ')
                       
                       # Change the value corresponding to the required field
                       
                       dic[flds[updtc-1]]=upval

                       yes_no=input('Do you want to update other details? y or n:')

                       if yes_no in 'N' or yes_no =='n':
                           break
                  
                   qry="UPDATE customer SET c_name=%s,c_lname=%s,c_phone=%s,c_address=%s WHERE c_ID=%s"
                 
                   updtl=tuple(dic.values())+(ask,)
                            # The value to be passed along with the query is a tuple
                            # containing updated details of the given customer ID
            
                   val=(updtl)
                   
                   mycur.execute(qry, val)
                   
                   mycon.commit()
                   print('Your details are update')

                           

                
               if ccc=='4':
                   try:
                        bkd_pro=get_bkd_pro(ask)
                        print('Your Booking (s) \n', bkd_pro)
                        if bkd_pro is None or bkd_pro=='':
                            print('You have no bookings to cancle')

                        else:
                            c_p=input("To cancle all products, enter A \nOR enter the products code to cancel: ")
                            if c_p in 'A':
                                qry="UPDATE customer SET pkd_pro=NULL WHERE c_ID=%s"
                                    
                                mycur.execute(qry,(ask,))
                                mycon.commit()

                                print("All bookings deleted")
                            elif c_p in bkd_pro:
                                # If more than one products entered,
                                # split them on the basis of '_'
                             
                                # x is a list containing all booked products

                                x=(bkd_pro[0:-1]).split('_')
                                #after bkb_pro is split x has exmaple [a,dkjf,dkjdf,kljdfj,jsf]
                                #and cw=a
                                #Delete the required product ID
                                x.remove(c_p)
                                # x.remove(cw) like x.remove(a) 
                                #Now x has[dkjf,dkjdf,kljdfj,jsf]
                                
                                updt_pro=''
                                # Again concatenate each product ID
                                # in the list to store in the table

                                for item in x:
                                    updt_pro=updt_pro+item+'_'
                                    
                                qry='UPDATE customer SET pkd_pro=%s WHERE c_ID=%s'
                                val=(updt_pro,ask)
                                mycur.execute(qry,val)
                                mycon.commit()
                                print('Booking Cancelled')
                            else:
                                print('Please enter the code products or the correct choice!')
                   except Exception:
                       print('Some problem in updateing details. Try again')

               if ccc.lower()=='back':
                   print("Successfully logged out")
                   space()
        
                   break
        else:
            print('This Account does not exist. ')

   except Exception:
        print('Some error occurred. Try Again')


# To fetch values from all columns of product table to get product details.
"""This function fetches all existing products from the database and then displays them in the form of a table."""
def view_pro():
    qry='SELECT * FROM products'
    mycur.execute(qry)
    d=mycur.fetchall()
    #contains list of all records
    dic={}
    #each record fetched is separated into a key value pair 
    #and stored in the dictionary where product ID is the key
    for i in d:
        dic[i[0] ]= i[1:]
    print('_'*80)
      # Printing the dictionary in the form of a table
      #
      #
    print("{:<17} {:<22} {:<23} {:<19}".format('Procuct id','Product','Price','Stock'))
    print('_'*80)
    

    for key,values in dic.items():
        name,price,stocke=values

        print("{:<17} {:<22} {:<23} {:<19}".format(key,name,price,stocke))
    print('_'*80)

# To add a new product in Products tabl       

"""Add products function is used by the employees of the boutique to add new product details. 
   It asks for a product number, product ID, price, and 
   stock from the employee and enters a new record in the products table of the database.""" 

def addpro():
    # Display list of products
    view_pro()
    num=int(input('Enter no of items to insert '))
        # Initialize tuple to store
        # product details.

    

    for j in range(num):
        t=()
        pronum=input('Product No. ')
        proid=input('Product ID :')
        pprice=int(input('Price : '))
        pstk=int(input('Stock : '))
    
        t=(pronum,proid,pprice,pstk)
        qry='INSERT INTO products VALUES(%s,%s,%s,%s)'
            
        
        val=t
        mycur.execute(qry,val)
        mycon.commit()
        print('Product Added')


# To delete a product from the table.

"""This function is used by the employees of the boutique to delete product details.
   It asks for the product ID and then deletes the record from the products table of the database."""

def delpro():
    delt=input('Enter ID of product to be deleted')
    qry='DELETE FROM  products WHERE pro_id=%s'
    mycur.execute(qry,(delt,))
    mycon.commit()
    print('Product is deleted')

# For Employee Login

"""This function is used for employees to login into their accounts. It allows employees to :
   Update the records of delivered products.
   Add a new product to the database
   Deletes a product from the database"""

def emp_sign_in():
    try:
        ask=input('Enter ID to sign in to the account : ')
        #To check if the employee with this ID exists or not.
        qry='SELECT emp_id FROM employee'
        mycur.execute(qry)
        d=mycur.fetchall()
        lis=[]
        
        for i in d:
            lis.append(i[0])
        if ask not in lis:
            print('Enter the correct ID')

        else:
            while True:
                space()
                ccc=input("1. Update delivered records\n2. Add a New Product \n3. Delete a product \nEnter 'Back' to logout: ")
                
                if ccc=='1':
                    cust_id=input('Enter customer ID')

                    # Check if the customer has bookings or not
                    bkd_pro=get_bkd_pro(cust_id)
                    if bkd_pro is None or bkd_pro ==' ':
                         print('This customer has no bookings ')

                    else:     
                        print('All booking(s): ', bkd_pro)
                        pro_id=input('Enter product code to remove the delivered product: ')
                         # The product IDs are stored in the form of a
                         # single value separated by '_'.
                        
                        if pro_id in bkd_pro:
                            
                            x=(bkd_pro[0:-1]).split('_')
                            # Returns a list of all booked products,
                            # then remove the delivered product from list

                            x.remove(pro_id)
                            # Concatenate the existing products using '_'
                            updt_pro=''
                            
                            for i in x:
                                updt_pro=updt_pro+i+'_'
                                
                            qry='UPDATE customer SET pkd_pro=%s WHERE c_ID=%s'
                            
                            val=(updt_pro, cust_id)
                            mycur.execute(qry,val)
                            mycon.commit()
                            print('Delivered product is removed from the database. ')
                        else:
                            print('enter the correct code')
                elif ccc=='2':
                    addpro()

                elif ccc=='3':
                    delpro()

                elif ccc=='back':
                     print('Successfull logged out ')
                     break
                
    except Exception:
        print('Give the correct input')




# To add employee details
"""Add employee function allows the employer to add a new employee to the boutique and 
   insert the records into the employee table of the database.
"""
def addemp():
    qry='SELECT * FROM employee'
    mycur.execute(qry)
    emp_list=mycur.fetchall()
    print('List of Employees ')
    for emp in emp_list:
        print("Emp Id : ", emp[0] , " Name : ", emp[1], " Last Name : ", emp[2]," Phone No : ",emp[3])
    
    
    n=int(input('Enter the no. of employees to add '))
    
    for i in range(1,n+1):
        ne=[]
        print(f'Enter details for Employee {i}:')
        
        idd = int(input(f'{i}) Employee ID: '))

        name = input(f'{i}) Name: ')
        
        lname = input(f'{i}) Last Name: ')
        
        conno = int(input(f'{i}) Contact No: '))

        adrs = input(f'{i}) Address: ')

        # A tuple containing details of an employee
        t=(idd,name,lname,conno,adrs)
        # List containing details of n number
        # of employees to be added
        ne.append(t)
         
        qry='INSERT INTO employee VALUES (%s,%s,%s,%s,%s)'
          # A list containing details of each employee
          # in the form of a tuple is to be passed along with the query
        for emp in ne: 
          
                mycur.execute(qry,emp)
                mycon.commit()
                print(f'Succesfully inserted: {emp}')
         
        print('All Employee details added. ')
        space()


# For employer login.                 
"""
This function is used for employer login and allows the employer to :

View all products
Add a new employee"""

def employer():
    
    while True:
        print()
        print('''Enter Your Choice
                    1)View Produc Details
                    2)Add a New Employee
                       enter 'back' to exit''')
        ccc = input('Enter _____  ')
        
        if ccc=='1':
              
              view_pro()

        if ccc=='2':
              addemp()

        if ccc.lower() =='back':
              break
    



"""
The program first asks for a choice of the user to enter as a customer, employee, 
or employer and calls the respective functions for the functioning of the program."""


print('WELCOME !')     
#Running  a infinite loop

while True:
    print('''Are you a :                                                   
   (A). Customer
   (B). Employee
   (C). Employer
   enter e to exit ''')
    
    choice=input('Enter -  ')
    try:
        if choice=='A':
            print(" 1. Create Account\n 2.Sign In into existing account")
            ch=input('enter - ')
            if ch =='1':
                cust_ac()
            elif ch=='2':
                sign_in()
            else:
                print('Enter correct choice')

        if choice=='B':
            emp_sign_in()

        if choice=='C':
            employer()

        if choice =="e":
            print('Thank you for visiting !')
            break
    except Exception:
        print('Give the right input')
    space()

                           
