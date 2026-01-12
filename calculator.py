def calculator():
    try:
        
        num1 = float(input("enter first number:"))

        #now iam prompting for second number
        num2 = float(input("enter second number:"))

        operation = input("enter the operations-(+,-,*,/)").strip()

        if operation =='+':
            result= num1+num2
        elif operation =='-':
            result= num1-num2
        elif operation =='*':
            result = num1*num2
        elif operation =='/':
            if num2 == 0:
                print("Error: div by zero is not allowed")
                return
            result= num1 / num2
        else:
            print("error invalid operation please choose the +,-,*,/")
            return
        

        print(f"the result of  {num1}   {operation}   {num2}   is:  {result}")
    except ValueError:
        print("error please enter valid numbers")

        #call the calculator function 
calculator()
