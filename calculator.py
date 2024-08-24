def calculator():
    print("Welcome to the simple calculator !")

    #get user input for the first number 
    try:
        num1 = float(input("Enter the first number :"))
    except ValueError:
        print("Invalid input.Pleaseenter a valid number.")
        return
    #get user input for the second number 
    try:
        num2 = float(input("Enter the second number :"))
    except ValueError:
        print("Invalid input.Please enter a valid number. ")
        return  
    #get the user input for the operation choice
    print("Choose an operation :")
    print("1. Addition(+)")
    print("2. Substraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")

    operation=input("Enter the operation(+,-,*,/): ")

    #perform the calculation based on the chosen operation
    if operation == '+':
        result = num1+num2
        print(f"The result of{num1}+{num2}is{result}.")
    elif operation =='-':
        result=num1-num2
        print(f"The result of {num1}-{num2}is{result}.") 
    elif operation =='*':
        result = num1 *num2
        print(f"The result of {num1}*{num2}is{result}.")   
    elif operation =='/':
        if num2 == 0:
            print("Error :Division by zero is not allowed.")
        else:
            result = num1/num2
            print(f"The result of {num1}/{num2}is{result}.")
    else:
        print("Invalid operation.Please choose from +,-,*,/.") 

#Run the calculator function 
calculator()                       
    


    