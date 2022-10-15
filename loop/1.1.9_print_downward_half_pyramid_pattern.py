'''
WAP to print the downward half pyramid pattern with * using for looop

input: 5
Expected output:
*****
****
***
**
*

Hint : You can pass a step function to the range function which will be used for the increment
range(1,6,2) => [1,4]

Pseudocode:
1) Take the number of rows to be printed
2) iterate the for loop with the range(num_of_rows,0,-1)
    2.1) print the "*" to count number of time
'''

num_of_rows = int(input("Enter number of rows to be printed : "))
for count in range(num_of_rows,0,-1):
    print("*"*count)
