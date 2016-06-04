from random import *
number = list(str(choice(range(0, 9999999))))
print("----MASTERMIND----")
print("Guess the number in as few tries as possible")
print("'*' = Correct digit, correct position.")
print("'=' = Correct digit in number, incorect position.")
print("'-' = Incorrect digit.")
print("The number has " + str(len(number)) + " digits.")
print()
attempt = 1
index = 0
use = input(str(attempt) + "> ")
guess = list(use)
while use:
    guess = list(use)
    output = ""
    index = 0
    if len(guess) == len(number):
        for i in guess:
            if i == number[index]:
                output += "*"
            elif i in number:
                output += "="
            else:
                output += "-"
            index += 1
        print(output)
        if guess == number:
            break
        else:
            attempt += 1
    else:
        print("Error, but no extra attempt will be added.")
    use = input(str(attempt) + "> ")
print("Well done... That took you [%s] attempts!" % (str(attempt)))
    
                
    
    
