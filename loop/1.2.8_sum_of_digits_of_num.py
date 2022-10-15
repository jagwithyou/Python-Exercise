'''
WAP to print the sum of digits in a given number.

Input: 123
Expected output: 6

Pseudocode:
1) get the number
2) intialize a variable with 0 to store the result
3) loop with the condition num >0
    3.1) get the last digit of the number (num%10)
    3.2) update the result as result+digit
    3.3) update the num as num floor devide by 10
4) print result
'''

num = int(input("Enter the number"))
result = 0
while num > 0:
    digit = num%10
    result+=digit
    num=num//10
print(result)
