'''
WAP to count the no of given substrings in a given string

input: 
"abcd bcde"
"bcd"
Expected Output: 
2

Pseudocode:
1) Get the complete string
2) Get the substring
3) findout the length of the substring
4) initialize a counter to 0, which will iterate through the index of the string
5) initialize a output variable to 0, which will count the output
6) loop till the counter < len(string)
    6.1) if input_string[counter:substring_length] == substring
        6.1.1) increment the output by 1
    6.2) increment the counter by 1
7) print output
'''

input_string = input("Enter the string : ")
sub_string = input("Enter the substring : ")
substring_length = len(sub_string)
count = 0
output = 0
while count < len(input_string):
    if input_string[count:count+substring_length] == sub_string:
        output += 1
    count += 1
print(output)
