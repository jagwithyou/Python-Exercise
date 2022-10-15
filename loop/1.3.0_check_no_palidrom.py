'''
WAP to check if a given number is a palindrom number or not. 

Input: 121
Expected output: True

Pseudocode:
1) get the number
2) get the backup of the given num
3) intialize a variable with 0 to store the reverse
4) loop with the condition num > 0
    4.1) get the last digit of the number (num%10)
    4.2) update the reverse as (reverse*10)+digit
    4.3) update the num as num floor devide by 10
5) check if num_backup is equals to reverse
    5.1) print the num is palindrom
6) Else
    6.1) print the num is not a palindrom num
'''

num = int(input("Enter the number: "))
num_backup = num
reverse = 0
while num > 0:
    digit = num%10
    reverse=(reverse*10)+digit
    num=num//10
if num_backup==reverse:
    print("The number is a palindrom number")
else:
    print("The number is not a palindrom number")
