#calculator project
def menu():
    print('''CALCULATOR
          1.ADDITION
          2. SUBTRACTION
          3. MULTIPLICATION
          4. DIVISION
          5.EXIT''')
    n=int(input("Enter an option[1-5]:"))
    if n == 1:
        n1=int(input("How many numbers do u want to enter:"))
        res=0
        for i in range(n1):
            num=int(input(f"THE {i+1} NUMBER IS:"))
            res=res+num
        print(res)
    elif n==2:
        n1=int(input("How many numbers do u want to enter:"))
        num=int(input("Please specify the initial number you want to subtract from:"))
        for i in range(n1):
            num1=int(input(f"THE {i+1} NUMBER IS:"))
            num=num-num1
        print(num)
    elif n==3:
        n1=int(input("How many numbers do u want to enter:"))
        res=1
        #num=int(input("Please specify the initial number you want to subtract from:"))
        for i in range(n1):
            num=int(input(f"THE {i+1} NUMBER IS:"))
            res=res*num
        print(res)
    elif n==4:
        n1=int(input("How many numbers do u want to enter:"))
        num=int(input("Please specify the initial number you want to subtract from:"))
        for i in range(n1):
            num1=int(input(f"THE {i+1} NUMBER IS:"))
            if num1==0:
                print("Cannot enter zero!")
            else:
                num=num/num1
        print(num)
    elif n==5:
        print("Bye! Have a nice day!")
    else:
        print("Wrong input.")

menu()
