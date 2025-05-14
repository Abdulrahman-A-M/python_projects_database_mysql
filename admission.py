import admission
import main_menu
import mysql.connector as co

mycon=co.connect(user='root',passwd='root',host='localhost',database='school')
cursor=mycon.cursor()

def ADM_MENU():

    while True:

        print("\t\t..........................................................")
        print("\t\t*****Welcome To School Management System*****")
        print("\t\t..........................................................")
        print("\n\t\t\t*****Mao Public School*****\n")
        print("\t\t\t1: Admission Details")
        print("\t\t\t2: Show admission details")
        print("\t\t\t3: Search")
        print("\t\t\t4: Deletion of records")
        print("\t\t\t5: Update Admission Details")
        print("\t\t\t6: Return")
        print("\t\t----------------------------------------------------------")
        choice=int(input("Enter your choice:"))
        if choice==1:
            admission.admn_details()

        elif choice==2:
            admission.show_admn_details()
        
        elif choice==3:
            admission.search_admn_details()
        
        elif choice==4:
            admission.delete_admn_details()
        
        elif choice==5:
            admission.edit_admn_details()

        



        
        


#-----------------------------------------------------------------------------------------------------------------
def admn_details():
    try:
       
        adno=input('Enter Admission number')
        rno=int(input('Enter Roll no'))
        sname=input('Enter student name')
        address=input('Enter address')
        phon=input('Enter phone')
        clas=input('Enter class')

        query="INSERT INTO admission VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')

    except Exception as error:
        print(f'There is error {error}')

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
def show_admn_details():

    cursor.execute('SELECT * FROM admission')
    data=cursor.fetchall()
    
    for row in data:
        print(row)

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

def search_admn_details():

    ac=input('Enter Admission Number')
    st="SELECT * FROM admission WHERE adno=%s" % (ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)

#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------

def delete_admn_details():

    ac=input('Enter Admission no')
    st="DELETE FROM admission WHERE adno=%s" % (ac)
    cursor.execute(st)
    mycon.commit()
    print('Data deleted successfully')

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
def edit_admn_details():
    
    print("1: Edit name")
    print("2: Edit Address")
    print("1: Phone number")
    print("1: Edit Return")
    print("\t\t----------------------------------------------------------")

    choice=int(input('Enter your choice'))
    
    if choice==1:
        admission.edit_name()

    elif choice==2:
        admission.edit_address()
    
    elif choice == 3:
        admission.edit_phno()
    
    elif choice == 4:
        return
    else:
        print('Error: Invalid Choice try again....')
        conti='Press any key to return to'


#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------

def edit_name():

    ac=input('Enter Addission Number')
    nm=input('Enter correct name')
    st="UPATE admission SET sname=%s" % (nm ,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

#-----------------------------------------------------------------------------------------------------------------
    

#-----------------------------------------------------------------------------------------------------------------

def edit_address():

    ac=input('Enter Admission Number')
    nm=input('Enter correct address')
    st="UPDATE admission SET address=%s WHERE adon=%s" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Update Successfully')

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
def edit_phno():

    ac=input('Enter Admission Number')
    nm=input('Enter correct phone number')
    st="UPDATE admission SET phon=%s WHERE adno=%s" % (nm, ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------




