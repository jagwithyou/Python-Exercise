'''
WAP that will help a self drive car to take decission in a traffic signal

Input: Red
Expected output: Stop

Pseudocode:
1) get the light color
2) check if the color is Red
    2.1) print Stop
3) check the color is Orange
    3.1) print Be Ready
4) check the color is Green
    4.1) print Go
'''
light_color = input("Enter the color of the traffic light - ")

if light_color == "Red":
    print("Stop")
if light_color == "Orange":
    print("Be Ready")
if light_color == "Green":
    print("Go")
