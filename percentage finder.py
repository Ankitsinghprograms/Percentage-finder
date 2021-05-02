"""
Percentage Finder (Python)

A simple / basic application written in python programming language, which serves the feature of calculating percentage. You can use this application (script file) to calculate your percentage of marks, or even anything ranging from the percentage of any elements in a compound to your body fat percentage. Just in simple words, this application is designed to calculate the mathematical percentage.

Author : 
Created on : 

Last modified on : May 2, 2021
Done by : Rishav Das (https://github.com/rdofficial/)

Contributors on this project (Add your name if you ever gave something to this script file, do it honestly) :
1.
2. Rishav Das (github:https://github.com/rdofficial, email:rdofficial192@gmail.com)

## ----
# Update by : Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
#
# Changes made :
# [1] Added more comments and also improvised the previous commenting + added the commented documentation for the program / script file.
# [2] Changed the old way of asking user input to a better and more attractive way + still the while loop is implemented.
# [3] Changed the way of defining the 'percentage' function + added more commented documentation to it + changed some variable names, but still the way and the purpose of this application is served.
## ----
"""

# Defining the function to find the percentage. The function is defined as an one-liner anonymous function. The function takes two input arguments (parameters), they are the 'score' and 'total'. The function then returns the percentage using those input values. The mathematical formula of finding percentage is : (score / total) * 100
percentage = lambda score, total: (score / total) * 100

def main():
    while True:
        # Asking the user for inputs continously until he/she wants to exit, thus implementing the while loop here

        print('[ Note : To exit the application, press CTRL+C key ]\n------------------------------------------')

        # Asking for the user input
        score = int(input('Enter the marks obtained : '))
        total = int(input('Enter the total marks : '))

        # Calculating the percentage and displaying it on the console screen
        result = percentage(score, total)
        print('\n[ Percentage : {} ]'.format(result))
        print('\n---------------------[]---------------------\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses the CTRL+C key combo, then we exit the script

        print('\n[ Quiting the application ]')
        input('Press enter key to continue...')
        quit()
    except Exception as e:
        # If we encounter any error in the process, then we display the error message to the user and quit the script

        print('\n[ Error : {} ]'.format(e))
        input('Press enter key to continue...')
        quit()

## ----
#  THE OLDER VERSION OF THE CODE [ BEFORE MAY 2, 2021 ]
## ----
# def percent():
#     """ This is used to find percentage by getting full marks
#     Make this function to be applicable to find pecentage of every subject"""
#     percentage=(int(marks)/int(total))*100
#     print("\nYour percentage is",percentage)

# print("Percentage Finder\n")
# while True:
#     print("Enter ! for quit\n")
#     marks=input("Enter total marks you obtained\n")

#     if marks == '!':
#         break
    
#     total=input("\nEnter Total marks of exam\n")
    
#     percent()
## ----
