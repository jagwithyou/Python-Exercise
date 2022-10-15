'''
WAP to print the following pattern using while loop
*
**
***
****
*****

Pseudocode:
1. Get the no of line to print
2. Initialize a counter from 1 
3. Lopp with the condition while counter <= no of lines
4. print the counter no of *, i.e "*"*count
5. increment the counter by 1
'''

no_of_lines = int(input("Enter the number of lines you want in the pattern"))
count = 1
while count <= no_of_lines:
    print("*"*count)
    count = count+1
