'''
WAP to find the factorial of anyy given number
Input: 3
Expected output: 6

Sudo Code:
1. Read the number
2. Initialize result variable to 1 to store the multiplications
2. iterate the loop with the condition num > 0
3. update result = result*num
4. decrement the num by 1
5. Print the result
'''
num = int(input("Enter the number"))
result=1
while num>0:
    result=result*num
    num = num-1
print("Factorial is : ", result)
