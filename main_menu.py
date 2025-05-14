import mysql.connector as co
mycon=co.connect(user='root',passwd='root',host='localhost',database='school')
cursor=mycon.cursor()



def STU_MENU():
    while True:
        print("\t\t..........................................................")
        print("\t\t\tWelcome To School Management System")
        print("\t\t..........................................................")
        print("\n\t\t\tMao Public School\n")
        print("\t\t\t1: Add Student Record")
        print("\t\t\t2: Show student Details")
        print("\t\t\t3: Search Student records")
        print("\t\t\t4: Delete student records")
        print("\t\t\t5: Edit student records")
        print("\t\t\t6: Exit")
        print("\t\t----------------------------------------------------------")
        
        choice =int(input('Enter your choice: '))
        
        if choice ==1:
            Add_Records()
        
        elif choice == 2:
             Show_Stu_Details()
        
        elif choice == 3:
            Search_Stu_Details()
        
        elif choice == 4:
            Delete_Stu_Details()
        
        elif choice == 5:
            Edit_Stu_Details()
        
        elif choice == 6:
            return
        
        else:
            print('Error : Invalid choice. Try again.....')
            conti="Press any Key to return to Main Menu"



def Add_Records():
    
    try:

        session=input('Enter academic session (e.g., 2023-10):')
        stname=input('Enter Student Name:')
        stclass=input('Enter class:')
        stsec=input('Enter section:')
        stroll=input('Enter roll no:')
        sub1=input('Enter subject1')
        sub2=input('Enter subject2')
        sub3=input('Enter subject3')
        val=(session,stname,stclass,stsec,stroll,sub1,sub2,sub3)
        query="INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,val)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in the student table')
        
    except Exception as error:
        print(f'erro the type error {error}')
        



def Show_Stu_Details():
    cursor.execute("SELECT * FROM student")     
    data=cursor.fetchall()

    for row in data:
        print(row) 




def Search_Stu_Details():
    ac=input('Enter Roll Number')
    st="SELECT * FROM student WHERE stroll=%s" 
    val=(ac,)
    cursor.execute(st,val)
    data=cursor.fetchall()
    print(data)




def Delete_Stu_Details():
    ac=input('Enter Roll Number')
    st="DELETE FROM student WHERE stroll=%s" 
    
    cursor.execute(st,(ac,))
    mycon.commit()
    print('Data delete successfully')



def Edit_Stu_Details():
    print("1: Edit session")
    print("2: Edit name")
    print("3: Edit class")
    print("4: Edit section")
    print("5: Edit Roll no")
    print("6: Edit sub1")
    print("7: Edit sub2")
    print("8: Edit sub3")
    print("9: Return")
    print("\t\t----------------------------------------------------------")
    
    choice=int(input('Enter your choice'))
    
    if choice==1:
        edit_session()
    
    elif choice==2:
        edit_name()
    
    elif choice==3:
        edit_class()
    
    elif choice==4:
        edit_section()
    
    elif choice==5:
        edit_Rollon()
    
    elif choice==6:
        edit_sub1()
    
    elif choice==7:
        edit_sub2()

    elif choice==8:
        edit_sub3()
    
    elif choice==9:
        return
    
    else:
        print('Error: Invalid Choice. Try again.....')
        conti="Press any Key to return to "



def edit_session():
    ac=input('Enter Roll no')
    nm=input('Enter correct session')

    st="UPDATE student SET session=%s WHERE stroll =%s" 
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data Updated successfully')



def edit_name():
    ac=input('Enter Roll no')
    nm=input('Enter correct name')
    st="UPDATE student SET stname=%s WHERE stroll=%s " 
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully')



def edit_class():
    ac=input('Enter Roll no')
    nm=input('Enter correct class')
    st="UPDATE student SET stclass=%s WHERE stroll=%s"
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully')





def edit_section():
    ac=input('Enter Roll no')
    nm=input('Enter correct section')
    st="UPDATE student SET stsec=%s WHERE  stroll=%s"
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully')




def edit_Rollon():
    ac=input('Enter Roll no')
    nm=input('Enter correct Roll no.')
    st="UPDATE student SET stroll=%s WHERE stroll=%s" 
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully.')




def edit_sub1():
    ac=input('Enter Roll no')
    nm=input('Enter correct subject1.')
    st="UPDATE student SET sub1=%s WHERE stroll=%s"
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully.')



def edit_sub2():
    ac=input('Enter Roll no')
    nm=input('Enter correct subject2')
    st="UPDATE student SET sub2=%s WHERE stroll=%s" 
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully.')



def edit_sub3():
    ac=input('Enter Roll no')
    nm=input('Enter correct subject3.')
    st="UPDATE student SET sub3=%s WHERE stroll=%s" 
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully.')




#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#                       Now this is admission
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
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
             admn_details()

        elif choice==2:
             show_admn_details()
        
        elif choice==3:
            search_admn_details()
        
        elif choice==4:
           delete_admn_details()
        
        elif choice==5:
          edit_admn_details()

        elif choice==6:
            return
        
        else:
            print('Error : Invalid choice. Try again.....')
            conti="Press any Key to return to Main Menu"

        



        
        


#-----------------------------------------------------------------------------------------------------------------
def admn_details():
    try:
       
        adno=input('Enter Admission number')
        rno=input('Enter Roll no')
        sname=input('Enter student name')
        address=input('Enter address')
        phon=input('Enter phone')
        clas=input('Enter class')
        val=(adno,rno,sname,address,phon,clas)
        query="INSERT INTO admission VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,val)
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
    st="SELECT * FROM admission WHERE adno=%s" 
    cursor.execute(st,(ac,))
    data=cursor.fetchall()
    print(data)

#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------

def delete_admn_details():

    ac=input('Enter Admission no')
    st="DELETE FROM admission WHERE adno=%s" 
    cursor.execute(st,(ac,))
    mycon.commit()
    print('Data deleted successfully')

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
def edit_admn_details():
    
    print("1: Edit name")
    print("2: Edit Address")
    print("3: Phone number")
    print("4: Edit Return")
    print("\t\t----------------------------------------------------------")

    choice=int(input('Enter your choice'))
    
    if choice==1:
        edit_name_a()

    elif choice==2:
        edit_address_a()
    
    elif choice == 3:
        edit_phno_a()
    
    elif choice == 4:
        return
    else:
        print('Error: Invalid Choice try again....')
        conti='Press any key to return to'


#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------

def edit_name_a():

    ac=input('Enter Addission Number')
    nm=input('Enter correct name')
    st="UPDATE admission SET sname=%s WHERE adno=%s" 
    val=(nm,ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully')

#-----------------------------------------------------------------------------------------------------------------
    

#-----------------------------------------------------------------------------------------------------------------

def edit_address_a():

    ac=input('Enter Admission Number')
    nm=input('Enter correct address')
    st="UPDATE admission SET address=%s WHERE adno=%s"
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data Update Successfully')

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
def edit_phno_a():

    ac=input('Enter Admission Number')
    nm=input('Enter correct phone number')
    st="UPDATE admission SET phon=%s WHERE adno=%s" 
    val=(nm, ac)
    cursor.execute(st,val)
    mycon.commit()
    print('Data updated successfully')
#-----------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------



while True:
    print("\t\t..........................................................")
    print("\t\t\tWelcome To School Management System")
    print("\t\t..........................................................")
    print("\n\t\t\t\tMao Public School\n")
    print("\t\t\t\t1:Admission")
    print("\t\t\t\t2:Student Data")
    print("\t\t\t\t3:Exit")
    print("\t\t----------------------------------------------------------")

    choice=int(input('Enter your choice:'))
    
    if choice==1:
       ADM_MENU()
    
    elif choice==2:
        STU_MENU()
    
    elif choice ==3:
        break

    else:
        print('Error:Invalid Choice try again.....')
        conti=input('Press any Key to continue')    