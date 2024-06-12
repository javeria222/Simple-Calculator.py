print("1 - Add")
print("2 - Substract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation: "))
result = 0

if(option in [1,2,3,4]):
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    if (option == 1):
        result = num1 + num2
    elif (option == 2):
        result = num1 - num2
    elif (option == 3):
        result = num1 * num2
    elif (option == 4):
        result = num1 / num2
    else:
      print("Invalid Option! Please enter a number between 1 and 4.")

print("The result of the operation is {}".format(result))