#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:06:53 2017

@author: Pir8
"""

def main_menu():
    print("This is a calculator program")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit the calculator program")

main_menu()

userQuestion = 0

while userQuestion != 5:
    userInput1 = float(input("Enter your first value: "))
    userInput2 = float(input("Enter your second value: "))
    userQuestion = input("Which number would you select (1-5)?: ")   
    
    if userQuestion == '1':
        answer = userInput1 + userInput2
        print(answer)
        main_menu()
    elif userQuestion == '2':
        answer = userInput1 - userInput2
        print(answer)
        main_menu()
    elif userQuestion == '3':
        answer = userInput1 * userInput2
        print(answer)
        main_menu()
    elif userQuestion == '4':
        if userInput2 == '0':
            print("This is an invalid answer!")
        else:
            answer = userInput1 / userInput2
        print(answer)
        main_menu()
    elif userQuestion == '5':
        print("goodbye\n")
    else:
        print("That is not a valid response. Select numbers 1 to 5")
        main_menu()