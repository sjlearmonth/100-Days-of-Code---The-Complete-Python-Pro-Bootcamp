# Day 1 - Task 4 - Variables

## Introduction

The purpose of this task is to learn about variables in Python, how to use them and to practice using them in some example code.

Variables are like containers in a computer program and are used to hold many different types of information such as numbers and text. The programmer creates a variable by giving it a name using special rules. The information held in a variable can then be maniuplated by referencing that variable's name.

## PAUSE 1. Check the length of the user input.

Here I use the built-in function ```input(...)``` in Python to get the user input by prompting the user for his or her name. The user input is then stored in the variable ```name```.

Next I use string concatenation to join together several other strings to be printed to the console which include the length of the user input. The length of the user input is calculated by callng the built-in function ```len(...)``` with user input variable ```name``` as an argument which then returns with an integer as the number of characters in the variable ```name```. The length of the user input is an integer so it must be converted into a string by calling the built-in function ```str(...)``` before it can be concatenated with the other strings in the ```print(...)``` function.

## PAUSE 2. Split everything into variables.

Here, the code in PAUSE 1 is modified to use a variable name for the user input called ```username``` and another variable name ```length``` to hold the length of the user input in ```username```.

The final ```print(...)``` function is called with the same strings concatenated as before but with the new variables inserted between them. The resulting string is printed to the console.
 

