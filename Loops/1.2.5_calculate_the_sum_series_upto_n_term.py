'''
WAP to calculate the sum of series up to n term. 
For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Input 5
Expected output:
24690 (i.e 2+22+222+2222+22222) 

Pseudocode:
1) get the num
2) initalize a variable to store the result
3) loop through the range (1 to num+1)
    3.1) formatted_no="2"*loop_counter
    3.2) update the result = result + int(formatted_no)
4) Print result
'''

num = int(input("Enter the number of series: "))
result = 0
for loop_count in range(1,num+1):
    formatted_no = "2"*loop_count
    result = result + int(formatted_no)
print(result)
