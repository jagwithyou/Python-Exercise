'''
WAP to Accept a list of 5 float numbers as an input from the user

input: 
10.2
11.3
14.5
2.3
4.3
Expected output:
[10.2, 11.3, 14.5, 2.3, 4.3]

Hint: 
1. range(starting_point, Ending_point) you can use range to get a list iterator which 
iterates from starting_point to ending point with one increment in each iteration.
2. Default value of starting_point is 0

Sudo Code:
1) define a empty list to store the inputs
2) loop with the range(5)
    2.1) get the input from the user
    2.2) append to the results
3) print result
'''
result = []
for count in range(5):
    input_value=float(input("Enter number : "))
    result.append(input_value)
print(result)
