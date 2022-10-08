'''
WAP to get the list of numbers divisible by 5 from a given list

input = [10,22,35,46]
expected output:
[10,35]

Hint: 1. for lool can be used directly to iterate through a list, which will iterate through each value in the list.

Sudo Code:
1) Initialize the list
2) Initialize an empty list to store the result
3) loop through the list using for loop
    3.1) if value is divisible by 5
        3.1.1) append the value in the result list
4) Print the result list
'''
input_list = [10,22,35,46]
result = []
for value in input_list:
    if value%5==0:
        result.append(value)
print(result)
