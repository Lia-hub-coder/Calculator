#calculator project
from datetime import datetime
def menu():
    with open ("history.txt","a") as c:
        design='*'*30
        design2='-'*30
        print(design2)
        s=input("Enter Your name please:  ")
        print(design2)
        while True:
            print(design)
            print('          MAIN MENU      ')
            print(design)
            initial_contents='\n1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5. VIEW HISTORY\n6.EXIT'
            print(initial_contents)
            print(design)
            try:
                n=int(input("Enter an option[1-6]:"))
                print(design)
                now=datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
                numbers=[]
                if n == 1:
                    n1=int(input("How many numbers do u want to enter:"))
                    res=int(input("Please specify the initial number you want to ADD to:"))
                    numbers.append(res)
                    for i in range(n1-1):
                        num=int(input(f"THE {i+1} NUMBER IS:"))
                        res=res+num
                        numbers.append(num)
                    print('The answer is:',res)
                    c.write(f"[{now}] {s} chose Addition with numbers  {numbers}  and the answer is: {res}\n")
                elif n==2:
                    n1=int(input("How many numbers do u want to enter:"))
                    res=int(input("Please specify the initial number you want to subtract from:"))
                    numbers.append(res)
                    for i in range(n1-1):
                        num=int(input(f"THE {i+1} NUMBER IS:"))
                        res=res-num
                        numbers.append(num)
                    print('The answer is:',res)
                    c.write(f"[{now}] {s} chose Subtraction with numbers {numbers} and the answer is: {res}\n")
                elif n==3:
                    n1=int(input("How many numbers do u want to enter:"))
                    res=int(input("Please specify the initial number you want to MULTIPLY:"))
                    numbers.append(res)
                    for i in range(n1-1):
                        num=int(input(f"THE {i+1} NUMBER IS:"))
                        res=res*num
                        numbers.append(num)
                    print('The answer is:',res)
                    c.write(f"[{now}] {s} chose Multiplication with numbers {numbers} and the answer is: {res}\n")
                elif n==4:
                    n1=int(input("How many numbers do u want to enter:"))
                    res=int(input("Please specify the initial number you want to DIVIDE from:"))
                    numbers.append(res)
                    for i in range(n1-1):
                        num=int(input(f"THE {i+1} NUMBER IS:"))
                        if num==0:
                            print("Cannot enter zero! Zero won't be counted.")
                        else:
                            res=res/num
                        numbers.append(num)
                    print('The answer is:',res)
                    c.write(f"[{now}] {s} chose Division with numbers {numbers} and the answer is: {res}\n")
                elif n==5:
                    print("This is view history")
                    c.write(f"[{now}] {s} visited the history!\n")
                    c.flush()
                    with open ("history.txt","r") as history:
                        contents = history.read()
                        print(contents)
                elif n==6:
                    print("Bye! Have a nice day!")
                    c.write(f"[{now}] {s} chose to exit the program\n")
                    break
                else:
                    print("Wrong input.")
            except ValueError:
                print("Invalid input! sorry. Try again.")

menu()