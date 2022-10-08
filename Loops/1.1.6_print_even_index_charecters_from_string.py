'''
WAP to Print characters from a string that are present at an even index number using for loop

input : "Welcome"
Expected Output : loe

Sudo Code:
1) Read the string
2) Initialize a empty string variable to store result
3) Loop through the string
    3.1) Find the index of the iterated carecter
    3.2) If the index of the charecter is even
        3.2.1) Add the charecter to the result (result+=char)
4. Print the result
'''
input_string = input("Enter the string : ")
result=""
for char in input_string:
    index=input_string.index(char)
    if index%2==0:
        result+=char
print(result)
