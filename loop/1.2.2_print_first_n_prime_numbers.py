'''
WAP to print the first n prime numbers

input 5:
Exoected output :
1
2
3
5
7
11

Hint:
Split the problem statement into two pieces, 
1. first you will iterate through a list till the count < no_of_outputs
2. check if a no is prime or not
finally put the code os step 2 in the loop of step 1

Pseudocode:
1) get the valur of n
2) initialize a counter variable to 0 who will count the even numbers
3) initialize a variable with 1 which will help us to check each numbers
4) loop with the condition count < no_of_output
    4.1)initialize a varible is_prime, which will hold the is prime status as True
    4.2)loop through the range(2,num)
        4.2.1) if num is divisible by the iter 
            4.2.1.1)update is_prime as false
    4.3)if is_prime is true
        4.3.1) print the num
        4.3.2) increment the count by 1
    4.4)increment the num by 1

'''
no_of_output = int(input("Enter the value of n : "))
count = 0
num = 1
while count <=no_of_output:
    is_prime=True
    for i in range(2,num):
        if num%i == 0:
            is_prime=False
    if is_prime:
        print(num)
        count=count+1
    num=num+1
        