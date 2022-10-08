'''
WAP to print the following pattern

Input: 5
Expected output:
*
**
***
**
*

Pseudocode:
1) get the num of rows in the pattern
2) calculate the absolute half of the rows given
3) initialize a print_counter to 0, which will help us to print the no of stars
4) loop through the range of rows
    4.1) if row count < half of rows
        4.1.1) increment the print_counter
    4.2) else if row count > half of rows
        4.2.1) decrement the print_counter
    4.3) print the print_counter number of *
6)
'''

num_of_rows = int(input("Enter the number of rows : "))
half_value = abs(num_of_rows/2)
print_counter = 0
for row_count in range(num_of_rows):
    if row_count <half_value:
        print_counter +=1
    elif row_count>half_value:
        print_counter-=1
    print("*"*print_counter)
