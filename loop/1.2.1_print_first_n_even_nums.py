'''
WAP to print the first n prime numbers

input 3:
Exoected output :
2
4
6

Pseudocode:
1) get the valur of n
2) initialize a counter variable to 0 who will count the even numbers
3) initialize a variable with 1 which will help us to check each numbers
4) loop with the condition count < no_of_output
    4.1)if num is even
        4.1.1) print the number
        4.1.2) increment the count by 1
    4.2)increment the num by 1
'''
no_of_output = int(input("Enter the value of n : "))
count = 0
num = 1
while count < no_of_output:
    if num%2 == 0:
        print(num)
        count += 1
    num += 1
        