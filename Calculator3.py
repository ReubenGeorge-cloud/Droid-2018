#calculator is the name of the function
def calculator():
    
    def add(a,b):
        return(a+b)
    def sub(a,b):
        return(a-b)
    def mul(a,b):
        return(a*b)
    def div(a,b):
        return(a/b)
    def menu():

        choice=(input("What do you want to do?: "))

        # the use of the math module would make the code shorter as defining the operations would not be required....
        # but the developer of this code is too stupid to know how to use the math module....
        if choice=='1':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The sum of ",a,"and",b,"is: ",add(a,b))

        elif choice=='2':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The difference between ",a,"and",b,"is: ",sub(a,b))

        elif choice=='3':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The product of ",a,"and",b,"is: ",mul(a,b))

        elif choice=='4':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The quotient of ",a,"and",b,"is: ",div(a,b))

        elif choice=='5':
            c=str(input("Are you sure you want to quit Reuben's Calculator?"))
            if c=='Yes' or c=='yes' or c=='yeah' or c=='yep' or c=='oh yeah' or c=='definitely' or c=='yes please' or c=='y':
                print("Thank you for using Reuben's Calculator")
            elif c=='no' or c=='No' or c=='Nope' or c=='nope' or c=='nah' or c=='nada' or c=='n':
                print("")
                return menu()

        else:
            print("ERROR CODE 605: INVALID INPUT")

    print("Welcome to Reuben's Calculator")

    print("")
    print("Your options are:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Quit")
    print("")

    menu()
    
