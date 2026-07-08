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
        for i in range(n1):
            num=int(input("THE NUMBER IS:"))
            print(num)
menu()
