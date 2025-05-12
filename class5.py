'''
1. Outline:
write a program to check whether the given number is positive?
'''
num = 12
#int(input("Enter a Number: "))
if num>0:
    print("It is a positive number.")
elif num < 0:
    print("It is a negative number.")
else:
    print("The number is neither positive nor negative. ")

'''
2. Profit loss
Outline:
Write to check if a person is buying oranges at 100 rs and later selling 1 at 120 rs. Find that he has profit or loss?
'''
CP = 100#int(input("Enter the actual price of oranges: "))
SP = 100#int(input("Enter the selling price of oranges: "))
if SP>CP:
    Pro = SP - CP
    print("You have got a profit of",Pro)
elif SP<CP:
    Loss = CP - SP
    print("You have got a Loss of",Loss)
else:
    print("You have neither Lost nor Gained any Money")

'''
3. Checking the number greater or smaller
Outline:
Write a program to check whether the given number is greater than 15 or smaller than 15.
'''
num = 15#int(input("Enter a Number: "))
if num<15:
    print("The number is less than 15")
elif num>15:
    print("The number is greater than 15")
else:
    print("The number is equal to 15")

'''
4. Odd-even
Outline:
Write a program to check whether the given number is even or odd?
'''
while True:
    num = int(input("Enter a number: "))
    if num%2 == 0:
        print("The Number is even")
    else:
        print("The Number is Odd")