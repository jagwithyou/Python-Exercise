'''
WAP to Calculate the cube of all numbers from 1 to a given number.

input: 3
Expected Output:
1
8
27

Sudo Code:
1. Read the number
2. Initialize a iterator with 1
2. iterate the loop with the condition iterator <=num
3. calculate the result (result = iterator*iterator*iterator)
4. print result
5. increment the iterator by 1
'''

num = int(input("Enter the number"))
iterator=1
while iterator<=num:
    result = iterator*iterator*iterator
    print(result)
    iterator +=1
