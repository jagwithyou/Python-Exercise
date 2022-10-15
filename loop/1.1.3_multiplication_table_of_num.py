'''
WAP to print the multiplication table of a given number

input = 2
Expected Output:
2*1=2
2*2=4
2*3=6
...
2*10=20

Hint:
You can print multiple valus in a print statement.

Pseudocode:
1. Read the number
2. Initialize a iterator with 1
2. iterate the loop with the condition iterator <=10
3. calculate the result (result = num*iterator)
4. print - 2*iterator = result
5. increment the iterator by 1
'''
num = int(input("Enter the number"))
iterator=1
while iterator<=10:
    result = num*iterator
    print(num,"*",iterator,"=",result)
    iterator +=1
