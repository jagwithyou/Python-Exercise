'''
WAP to print fibonacci series upto n-terms

Input: 5
Expected output:
0
1
1
2
3

Hint: 
1. fibonacci series is a series where the third element is sum of first two
2. starting two elements are 0 & 1

Pseudocode:
1) Get the no of terms
2) initialize the first_num as 0
3) initialize the second_num as 1
4) initalize a loop_count with 0
5) loop with the condition loop_count < no_terms
    5.1) print(first_no)
    5.2) update n1 and n2 with n2 and sum(n1,n2)
    5.3) increment the loop_count with 1

'''

no_terms = int(input("Enter no of terms: "))
n1 = 0
n2 = 1
loop_count = 0
while loop_count < no_terms:
    print(n1)
    n1,n2 = n2,n1+n2
    loop_count+=1