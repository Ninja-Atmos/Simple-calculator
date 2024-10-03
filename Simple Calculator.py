a = int(input("1 Addition,\n2 Subtraction,\n3 Multiplication,\n4 Division\nEnter your choice: "))





if a == 1:
    s1 = int(input("Enter 1st number: "))
    s2 = int(input("Enter 2nd number: "))
    print("The sum of two numbers is: ", (s1 + s2))
    
elif a == 2:
    s3 = int(input("Enter 1st number: "))
    s4 = int(input("Enter 2nd number: "))
    print(f"The subtraction between two numbers is: {s3 - s4} ")
    
elif a == 3:
    s5 = int(input("Enter 1st number: "))
    s6 = int(input("Enter 2nd number: "))
    print(f"The multiplication of two numbers is: {s5 * s6}")

elif a == 4:
    s7 = int(input("Enter 1st number: "))
    s8 = int(input("Enter 2nd number: "))
    print(f"The division of two numbers is: {s7 / s8}" )
    
else:
    print("You choose a wrong number")