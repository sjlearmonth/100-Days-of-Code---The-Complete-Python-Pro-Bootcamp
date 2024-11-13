# Day 2 - Task 2 - Type Error, Checking and Conversion

The purpose of this task is to learn about data type errors, how to check the data type of any of the primary data types in Python and how to convert one daya type to another data type.

#### PAUSE 1. TypeError

When a value is passed to a function in Python and it is the incorrect data type for that function an error is generated in the console. This is illustrated by passing an integer value to the built-in function ```len(...)``` which accepts only string values. The following error message is generated in the console;

   ```TypeError: object of type 'int' has no len()```

Only when the integer value is surrounded by double quotes to make it a string does the ```len(...)``` function work as expected and no error is reported.

#### PAUSE 2. Write out 4 data type checks to print all 4 data types

Python has a built-in function called ```type(...)``` which accepts a value having one of the four primary data types and returns the data type of that value. This is ilustrated by calling the ```type(...)``` function with an example of each of the four data types and observing the output in the console as follows;

-    ```<class 'str> means the value passed is of the data type "string"```
-    ```<class 'int'> means the value passed is of the data type "integer"```
-    ```<class 'float'> means the value passed is of the data type "float"```
-    ```<class 'bool' means the value passed is of the data type "Boolean"```

#### PAUSE 3. Make this line of code run without errors.

Here I have to edit a line of code so that no type error is reported in the console. A type error is reported because the ```len(...)``` function returns an integer data type and string concatenation inside the ```print(...)``` function requires there to be only strings. So the built-in function ```str(...)``` is called with return value of the ```len(...)``` function to convert the integer value into a string value.

