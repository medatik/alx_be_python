def perform_operation (num1, num2, operation) :
    match operation :
        case 'add':
            print(f"the addition of the two numbers is {num1 + num2}")
        case 'subtract':
            print(f"the substruction is : {num1 - num2}")
        case 'multiply':
            print(f"the multiplication is : {num1 * num2}")
        case 'divide' :
            if num2 != 0 : 
                print(f" the division is : {num1 / num2}")
            else :
                print("can't divide by 0")
        case _ :
            print("operation must be add, substract, multiply or divide")
            

