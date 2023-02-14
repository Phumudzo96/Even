number = int(input("Enter a number: ")) #Ask the user to enter a number
number1 = 1                             #Create a variable that the loop will start from
while  number1 <= number:                
    if number1 % 2 == 0:                #This will print all numbers divisable by 2 and have no remaineder
        print(number1)
    number1 += 1