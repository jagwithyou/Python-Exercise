'''
WAP to print a ginven list in reverse order.

input : [1,2,3,4]
Expected Output : [4,3,2,1]

Hint: insert() is used to insert a perticular value to a perticular index of the list
eg: list_name.insert(index, value)

Sudo Code:
1) initialize the list
2) define a empty list to store the result
3) Loop through the list
    3.1) insert the element to the 0th index of the list
4) print the result list
'''

input_list = [1,2,3,4]
result=[]
for value in input_list:
    result.insert(0,value)
print(result)
