import sqlite3
from google.colab import drive
drive.mount('/content/drive')
con=sqlite3.connect('/content/drive/MyDrive/Student Mangement/ hello1.db')
cur=con.cursor()


def Phone(a):
  while(1):
        pho=str(a)
        while len(pho)!=10:
          print("Enter phone no. of 10 digits.")
          b=int(input("Enter the phone no. here:- "))
          pho=str(b)
        pho=int(pho)
        return(pho)
        break

def Marks(a):
  while(1):
    marks=a
    while marks<0 or marks>100:
      print("Enter marks between 0 to 100.")
      b=int(input("Enter the marks (Out of 100) here:- "))
      marks=b
    return(marks)
    break

def  rollnu():
  cur.execute(f"select count(*) from {table}")
  c=cur.fetchall()
  con.commit()
  a=c[0][0]  
  
  b=1
  b=b+a
  return b
  
def searchroll():
  while(1):
    r=int(input("Enter the roll number here:- "))
    cur.execute("select * from studenty where rollno=?",(r,))
    a=cur.fetchall()
    con.commit
    b=len(a)
    if b==0:
      print("No such roll number in the list.")
    else:
      return r
      break

def add():
    while(1):
        cur.execute(f"insert into {table} values(?,?,?,?,?,?,?,?,?,?)",(name,
        age,rollno,gender,phoneno,Eng_marks,Chem_marks,Phy_marks,Math_marks,
        Cs_marks))
        con.commit()
        
        print("Records are entered successfully.")
        break

def show():
    cur.execute(f"select * from {table}")
    rows=cur.fetchall()
    con.commit()
    print("{:<15}{:<5}{:<5}{:<8}{:<13}{:<7}{:<7}{:<7}{:<7}{:<7}".format(
        "Name","Age","Rno","Gender","Phone No","Eng","Chem","Phy","Math","CS"))
    print("_"*80)
    return rows

def modifyall():
    cur.execute('''update studenty set name=?,age=?,gender=?,phoneno=?,
                English_marks=?,Chemistry_marks=?,Physics_marks=?,Maths_marks=?,
                Computer_Science_marks=? where rollno=?''',(
                    name,age,gender,phoneno,Eng_marks,Chem_marks,Phy_marks,
                    Math_marks,Cs_marks,rollno))
    con.commit()
    
    print("success","information has been updated successfully")

def modify():
  cur.execute(f"update studenty set {field}=? where rollno=?",(updated,rollno))
  con.commit()
  
  print("success","information has been updated successfully")

def search(s):
    cur.execute("select * from studenty where rollno=?",(s,))
    rows=cur.fetchall()
    return rows
  

def delete(d):
    cur.execute("delete from studenty where rollno=?",(d,))
    con.commit()
    
    print("success","information has been deleted successfully")



try:
    cur.execute('''CREATE TABLE studenty (
                      name varchar(25),
                      age int(7), 
                      rollno int(6) primary key, 
                      gender varchar(10) ,
                      phoneno int(10),
                      English_marks int(3),
                      Chemistry_marks int(3),
                      Physics_marks int(3),
                      Maths_marks int(3),
                      Computer_Science_marks int(3)
                        );''')
except:
    print("Table already created")
con.commit()

try:
    cur.execute('''CREATE TABLE SLC (
                      name varchar(25),
                      age int(7), 
                      rollno int(6) primary key, 
                      gender varchar(10) ,
                      phoneno int(10),
                      English_marks int(3),
                      Chemistry_marks int(3),
                      Physics_marks int(3),
                      Maths_marks int(3),
                      Computer_Science_marks int(3)
                        );''')
except:
    print("Table already created")
con.commit()


while(1):
    print("\n*******************STUDENT MANAGEMENT SYSTEM********************")
    print("1. Insert Record")
    print("2. Display Record")
    print("3. Modify Record")
    print("4. Search Record")
    print("5. Delete Record")
    print("6. Display deleted Record")
    print("7. Exit")
    choice=input("Enter choice (1-7) ")
 
    if choice=="1":
      table="studenty"
      
      rollno=rollnu()
      name=input("Enter name : ")
      age=int(input("Enter age : "))
      
      gender=input("Enter gender (M/F) : ")
      while  gender!="M" and gender!="F":
        print("Enter either M or F.")
        gender=input("Enter gender (M/F): ")

      mobi=int(input("Enter phone no. here:- "))
      phoneno=Phone(mobi)   
      
      eng=int(input("Entert the English marks (Out of 100) here:- "))
      Eng_marks=Marks(eng)
                 
      chem=int(input("Entert the Chemistry marks (Out of 100) here:- "))
      Chem_marks=Marks(chem)
                 
      phy=int(input("Entert the Physics marks (Out of 100) here:- "))
      Phy_marks=Marks(phy)
                 
      math=int(input("Entert the Maths marks (Out of 100) here:- "))
      Math_marks=Marks(math) 
       
      cs=int(input("Entert the Computer Science marks (Out of 100) here:- "))
      Cs_marks=Marks(cs)
        
      add()
       
    elif choice=="2":
        table="studenty"
        L2=show()
        for i in L2:
          print("{:<15}{:<5}{:<5}{:<8}{:<13}{:<7}{:<7}{:<7}{:<7}{:<7}".format(
              i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
 
    
    elif choice=="3":
      rollno=searchroll()
      
      while(1):
        op=input("Do you want to modify all the data? (y/n)")

        if op=='y':
          name=input("Enter name : ")
          age=int(input("Enter age : "))
          gender=input("Enter gender : ")
          while  gender!="M" and gender!="F":
            print("Enter either M or F.")
            gender=input("Enter gender (M/F): ")
          mobi=int(input("Enter phone no. here:- "))
          phoneno=Phone(mobi)   
          
          eng=int(input("Entert the English marks (Out of 100) here:- "))
          Eng_marks=Marks(eng)
                    
          chem=int(input("Entert the Chemistry marks (Out of 100) here:- "))
          Chem_marks=Marks(chem)
                    
          phy=int(input("Entert the Physics marks (Out of 100) here:- "))
          Phy_marks=Marks(phy)
                    
          math=int(input("Entert the Maths marks (Out of 100) here:- "))
          Math_marks=Marks(math) 
          
          cs=int(input("Enter the Computer Science marks (Out of 100) here:- "))
          Cs_marks=Marks(cs)
          
          modifyall()
          break
        
        elif op=='n':
          L1=["name","age","gender","phoneno","English_marks","Chemistry_marks",
              "Physics_marks","Maths_marks","Computer_Science_marks"]
          print("The fields are:- ",L1)
          field=input("Enter the field you want to modify:- ")
          if field not in L1:
            print("Enter the correct field.")
          else:
            updated=input(f"Enter {field} to be updated : ")
            if field!="name" and field!="gender":
              updated=int(updated)
              if field=="phoneno":
                p=Phone(updated)
                updated=p
              elif field!="phoneno" and field!="age":
                m=Marks(updated)
                updated=m
            
            modify()
            break
        else:
          print("Enter the correct choice.")  
 
    elif choice=="4":
        a=searchroll()
        L4=search(a)
        print("{:<15}{:<5}{:<5}{:<8}{:<13}{:<7}{:<7}{:<7}{:<7}{:<7}".format(
        "Name","Age","Rno","Gender","Phone No","Eng","Chem","Phy","Math","CS"))
        print("_"*80)
        for i in L4:
          print("{:<15}{:<5}{:<5}{:<8}{:<13}{:<7}{:<7}{:<7}{:<7}{:<7}".format(
              i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))

    elif choice=="5":
        d=searchroll()
        table="studenty"
        total=rollnu()-1
        s=search(d)
        m=1
        while m>0:
          imp=input("Do you really want to delete the data? (y/n)")
          if imp=="y":
            delete(d)
            n=total-d
            field="rollno"
            rollno=d+1
            updated=d
            
            while n>0: 
              modify()
              rollno=rollno+1
              updated=updated+1
              n=n-1
            
            table="SLC"
            name=s[0][0]
            age=s[0][1]
            rollno=rollnu()
            gender=s[0][3]
            phoneno=s[0][4]
            Eng_marks=s[0][5]
            Chem_marks=s[0][6]
            Phy_marks=s[0][7]
            Math_marks=s[0][8]
            Cs_marks=s[0][9]
            add()

            m=0
          elif imp=="n":
            m=0
          else:
            print("Invalid Choice.")


    elif choice=="6":
        table="SLC"
        L3=show()
        for i in L3:
          print("{:<15}{:<5}{:<5}{:<8}{:<13}{:<7}{:<7}{:<7}{:<7}{:<7}".format(
              i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))

    elif choice=="7":
        break

    else:
        print("Invalid choice !!!")
