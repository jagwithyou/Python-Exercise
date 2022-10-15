'''
WAP to count the no of digits in a given number.

Input: 415
Expected output: 3

Pseudocode:
1) get the number
2) intialize a variable with 0 to store the result
3) loop with the condition num >0
    3.1) increment the result with one
    3.2) Update the num as num//10
4) Print result
'''

num = int(input("Enter the number"))
result = 0
while num > 0:
    result+=1
    num=num//10
print(result)
