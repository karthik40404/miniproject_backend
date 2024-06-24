print("1.add\n2.view\n3.update\n4.delete\n5.exit")
emp=[]
while True:
    choice=int(input("enter your choice :"))
    if choice==1:
        emp_id=int(input("ente your id :"))
        emp_name=str(input("enter your name :"))
        emp_age=int(input("enter your age :"))
        emp_salary=int(input("enter your salary :"))
        emp_exp=int(input("enter your experience :"))
        emp_email=input("enter your email :")
        emp_phno=int(input("enter your number :"))
        emp.append([emp_id,emp_name,emp_age,emp_salary,emp_exp,emp_email,emp_phno])
    elif choice==2:
        for i in emp:
            print("emp_id :",i[0])
            print("emp_name :",i[1])
            print("emp_age :",i[2])
            print("emp_salary :",i[3])
            print("emp_exp :",i[4])
            print("emp_email :",i[5])
            print("emp_phno :",i[6])
    elif choice==3:
        id=int(input("enter an id :"))
        f=0
        for i in emp:
            if id==i[0]:
                f=1
                print(i)
                emp_name=str(input("enter your name :"))
                emp_age=int(input("enter your age :"))
                emp_salary=int(input("enter your salary :"))
                emp_exp=int(input("enter your experience :"))
                emp_email=input("enter your email :")
                emp_phno=int(input("enter your number :"))  
                i[1]=emp_name
                i[2]=emp_age
                i[3]=emp_salary
                i[4]=emp_exp
                i[5]=emp_email
                i[6]=emp_phno  
        if f==0:
            print("invalid id")
    # elif choice==4:
