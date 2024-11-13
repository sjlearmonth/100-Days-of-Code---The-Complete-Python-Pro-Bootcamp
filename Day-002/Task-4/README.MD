# Day 2 - Task 4 - Number Manipulation

The purpose of this task is to learn about how I can manipulate numbers converting float values to an integer value after discarding the fractional part after the decimal point and rounding float values to the nearest whole number or integer.

I also learned how to use the "assignment operators" to manipulate the contents of variables by performing a mathematical operation on the contents and overwirting that content with the new result.

Learning about ```f-Strings``` is also included in this task which allows the contents of a variable to be inserted directly into a string without performing any conversion to a string data type first.

#### PAUSE 1. Flooring a number.

Flooring a number like a float value means truncating it so that the fractional part to the right of the decimal point is removed. This leaves the integer part. This is done by calling the built-in function ```int(...)``` with a float value and an integer value is returned.

#### PAUSE 2. Rounding a number.

Rounding a number like a float value means converting the number to the whole number or integer that it is closest to. This done by calling the built-in function ```round(...)``` with the float value and a whole number or integer is returned.

#### PAUSE 3. Assignment Operators.

There are four assignment opoerators in the Python programming language.

-    ```+=```
-    ```-=```
-    ```*=```
-    ```/=```

The ```+=``` assignment operator fetches the contents of the variable on its left-hand side, adds the value on its right-hand side to those contents and stores the result back into the same variable.

The ```-=``` assignment operator fetches the contents of the variable on its left-hand side, subtracts the value on its right-hand side from those contents and stores the result back into the same variable.

The ```*=``` assignment operator fetches the contents of the variable on its left-hand side, multiplies the value on its right-hand side with those contents and stores the result back into the same variable.

The ```/=``` assignment operator fetches the contents of the variable on its left-hand side, divides the value on its lts right-hand side into those contents and stores the result back into the same variable.

#### PAUSE 4. f-Strings.

f-Strings are strings which are prepended with the ```f``` character and contain the name of a variable in the string surrounded by braces ```{``` and ```}```, for example ```{my_variable}```. When the string is printed to the console, the value of the variable is included in the output to the console, without the need to perform any type conversion on the variable's contents.

 
