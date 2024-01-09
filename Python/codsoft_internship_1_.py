#Calculator

def calculator():
    try:
        Number_1 = float(input("Enter first number: "))

        Arth_Oper = input("Enter your arithmetic operation: ")

        Number_2 = float(input("Enter 2nd number: "))
        
        if Arth_Oper == '+':
            print("Answer is: ", Number_1+Number_2)
        elif Arth_Oper == '-':
            print("Answer is: ", Number_1-Number_2)
        elif Arth_Oper == '*':
            print("Answer is: ", Number_1*Number_2)
        elif Arth_Oper == '/':
            print("Anwer is: ", Number_1/Number_2)
        else:
            print("Invalid selection please choose a valid arithmetic operater like +,-,* and /.")
        
    except ValueError:
        print("Invalid Input. Please enter onlu numeric values.")

calculator()


        