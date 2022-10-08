'''
WAP to calculate the sum of first n positive integers
n - int
Test Case:
Input : 3
Expected output : 6

Hint: 1+2+3=6 (you should use a variable to store this pattern before the loop)

Pseudocode:
1. Read the number
2. Initialize result variable to 0 to store the sum
2. iterate the loop with the condition num > 0
3. update result = result+num
4. decrement the num by 1
5. Print the result
'''
num = int(input("Enter the number"))
result=0
while num>0:
    result=result+num
    num = num-1
print(result)
