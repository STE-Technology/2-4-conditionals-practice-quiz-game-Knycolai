"""
File: quiz.py
Author: Name
Date: YYYY-MM-DD
Description: A brief explanation of what this program does.
"""
correctanswers = 0
print ("Multiple-Choice Quiz Game") 
print ("")
print ("1. Which of these agents role is a Duelist?")
print ("(a) iso")
print ("(b) Killjoy")
print ("(c) Omen")
print ("")
answer1 = input("> ")
if answer1 == "a" or answer1 == "A":
    print("Correct!")
else:
    print("Incorrect.")
#Sir, how do I add a counter to add wether the user got the question right or wrong    
print ("")
print ("2. Who is the God of Wind and Time?")
print ("(a) Narzissenkreuz")
print ("(b) Rhinedottir")
print ("(c) Istaroth")
print ("")
answer2 = input("> ")
if answer2 == "c" or answer2 == "C":
    print("Correct!")
else:
    print("Incorrect.")
print ("")
print ("3. Who is Known as the 'God of War' or 'The Ghost of Sparta' ")
print ("(a) Ares")
print ("(b) Kratos")
print ("(c) Athena")
print ("")
answer3 = input("> ")
if answer3 == "b" or "B":
    print("Correct!")
else:
    print("Incorrect.")
correctanswers = answer3 + answer2 + answer1
print ("")
print ("Quiz Complete!")
print ("You answered " + correctanswers + "of 3 questions correctly. Your score is " )