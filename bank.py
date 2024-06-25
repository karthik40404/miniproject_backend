bank=[["kart",56,'jhgjh','jhj',898765,'88h8hyguh',0]]
while True:
    print("1.registration\n2.login\n")
    choice=int(input("enter your choice :"))
    if choice==1:
        emp_name=str(input("enter your name :"))
        emp_age=int(input("enter your age :"))
        emp_location=input("enter your location :")
        emp_email=input("enter your email :")
        emp_phno=int(input("enter your number :"))
        emp_pass=str(input("enter your password :"))
        bank.append([emp_name, emp_age,emp_location,emp_email,emp_phno,emp_pass,0])
    elif choice == 2:
        emp_email = input("Enter your email: ")
        emp_pass = input("Enter your password: ")
        found = False
        for i in bank:
            if i[3] == emp_email and i[5] == emp_pass:
                print("Login successful! Welcome",i[0])
                found = True
                while True:
                    print("1.balance\n 2.deposit\n 3.withdraw\n 4.logout\n")
                    choice=int(input("enter your choice :"))  
                    if choice==1:
                        print("balance",i[6])
                    elif choice==2:
                        amount=int(input("enter your amount :"))
                        i[6]+=amount
                        print("currentbalance :",i[6])
                    elif choice==3:
                        amount=int(input("enter your amount :"))
                        if i[6]>amount:
                            i[6]-=amount
                            print("transaction succussfull")
                        else:
                            print("insufficiant amount")
                    elif choice==4:
                        break
        if not found:
            print("Invalid email or password. Please try again.\n")
    else:
        print("Invalid choice. Please try again.\n")