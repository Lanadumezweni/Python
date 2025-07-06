#Variables

my_variable =10
total_count =0
user = 'john'

#invaild
second_variable =10
user_name = 20

#Operators

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# division (/)
# Modulus (%)
# Exponent (**)

x = 5
y = 10

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(5%2)

print(x**y)

#Operators with Strings
 
str1 = 'Hello'
str2 = 'world'

print(str1 + " " + str2 + " "+ str2)
print(str1 * 3)

#Control Statements

num = -1

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")
 
#Control statements

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
    
    #Loops
    
    #Using awhile loop to count from 1 to 5
    count = 1
    
    while count <= 5:
        print(count)
        count += 1 # Increments the count by 1
        
        
    #Loop Control Statements
    
    fruits = ["apple","banana", "cherry", "date"]
    
    for fruit in fruits:
        if fruit == "cherry":
            break # Exits the loop if cherry is found
        print(fruit)
        
        print()
    
    for fruit in fruits:
        if fruit == "cherry":
            continue # Skips cherry and moves to the iteration
        print(fruit)
        
        print()
    
    for fruit in fruits:
        if fruit == "cherry":
            pass # Placeholder, no action is needed for cherry
        print(fruit)
        
        
        #Loop Control Statements
        
        count = 0
        
        while count < 5:
            print(count)
            count +=1
            if count == 3:
                break # Exits the loop when the count is reached -3
            