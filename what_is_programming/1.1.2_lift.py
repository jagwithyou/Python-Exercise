'''
WAP that will help a lift to take decission where to stop

Hint: Suppose the lift is starting from Ground floor and going till top floor

Input: 
Get switch 1 status Active/Inactive: Active
Get switch 2 status Active/Inactive: Inactive
Get switch 3 status Active/Inactive: Active
Get switch 4 status Active/Inactive: Inactive

Expected output: 
Stop at first floor
Stop at third floor

Pseudocode:
1) get the switch one status
2) get the switch two status
3) get the switch three status
4) get the switch four status
5) check if the switch one is Active
    5.1) print Stop at first floor
6) check if the switch two is Active
    6.1) print Stop at second floor
7) check if the switch three is Active
    7.1) print Stop at third floor
8) check if the switch four is Active
    8.1) print Stop at fourth floor

'''
switch_1 = input("Get switch 1 status Active/Inactive: ")
switch_2 = input("Get switch 2 status Active/Inactive: ")
switch_3 = input("Get switch 3 status Active/Inactive: ")
switch_4 = input("Get switch 4 status Active/Inactive: ")

if switch_1 == "Active":
    print("Stop at first floor")
if switch_2 == "Active":
    print("Stop at second floor")
if switch_3 == "Active":
    print("Stop at third floor")
if switch_4 == "Active":
    print("Stop at fourth floor")
