# HRON

## Introduction
HRON is an interpreted programming language inspired by **'해로온'**, a member of the Korean indie idol group **'하라무코'**.

> &nbsp;
>
> HRON exists for 해로온.
>
> &nbsp;

## Key Features
- **Hangul-based syntax**: All commands and variables are composed solely of two Korean charancters, **'해'** and **'롱'**, except for the termination command, **'해로온이라'**.
- **Procedural programming support**: HRON follows a procedure programming style, similar to the C language.
- **Interpreted programming language**: HRON is an interpreted programming language, similar to Python, which interprets and executes code in real time.

## Getting Started
### Prerequisites
HRON requires Python to be installed in order to run.
- Python >= 3.11.10

### Instructions
1) Navigate to the **'src'** folder in your terminal\
\> cd src
2) Run the **'main.py'** file'\
\> python main.py

## Basic Syntax
### Core Rules
- Only **'해'**, **'롱'**, and **'해로온이라'** are allowed.
- All code must end with **'해로온이라'**
- Numbers and strings must be declared using variables, which are assigned and called later.
- Strings predefined as commands can also be used as variable names.

#### Example Codes
The example codes are located in the 'examples' folder with explanations.
- example_code_1.md\
Assigns variables and print the value of addition.
- example_code_2.md\
Prints 'Hello World!'.
- example_code_3.md\
Prints a tower using nested loops.

### Data Types
HRON requires you to specify the data type before assigning a value to a variable.

#### 해롱롱 (Integer)
- Represents integers.
- Binary numbers are entered using '해' for 1 and '롱' for 0.
- Examples:
    - 4 (100): 해롱롱
    - 17 (101110): 해롱해해해롱
    - 692 (1010110100): 해롱해롱해해롱해롱롱

#### 해해롱 (Character)
- Represents a character
- The ASCII value of the character to be assigned is entered as a binary number.
- To create a string, store each character in seperate variables and concatenate them using an addition operation.

### Variable Declaration and Initialization
#### Declaring a Variable
- After typing '해롱해롱', the next token will be declared as a variable.
- Variables must be composed solely of the two characters '해' and '롱'.
- You can specify the data type and assign a value when declaring the variable.

&nbsp;

> &nbsp;
>
> **Structure**\
> 해롱해롱 (variable) (data type) (value)
>
> &nbsp;
>
> **Example**\
> 해롱해롱 해롱 해롱롱 해롱\
> Declares the variable '해롱' and assigns an integer value (해롱롱) 2 (해롱, 10).
>
> &nbsp;

#### Initializing a Variable
- After typing '해롱', you can initialize the value of a variable.

&nbsp;

> &nbsp;
>
> **Structure**\
> 해롱 (variable) (data type) (value)
>
> &nbsp;
>
> **예시**\
> 해롱 해롱 해롱롱 해롱롱\
> Assigns the integer (해롱롱) 4 (해롱롱, 100) to the previously declared variable '해롱'.
>
> &nbsp;

### Input and Output
#### Input
- After typing '해해롱해롱', the value entered by the user will be stored in the following variable.
- If the variable is not declared, a new variable will be declared, and the value will be assigned

#### Output
- After typing '해롱해해롱', the value stored in the following variable will be printed.

### Operators
- After inputting an operator and three variables, the result of the operation on the first two variables is stored in the third variable.

&nbsp;

> &nbsp;
>
> **Structure**\
> 해롱해롱해 (variable 1) (variable 2) (variable 3)\
>
> &nbsp;
>

#### Arithmetic Operators
- '해롱해롱해': Addition (+)
- '해롱롱해': Subtraction (-)
- '해롱해롱해롱해': Multiplication (*)
- '해롱롱해롱롱해': Division (//)
- '해롱해롱해롱해롱해': Exponentation (**)
- '해롱롱해해롱해': Modulus (%)

#### Relational Operators
Relational Operators store the result as a boolean type ('True', 'False').
- '해해롱롱해해': Equal (==)
- '해해롱롱해롱': Not equal (!=)
- '해롱해롱롱해롱': Greater than (>)
- '해롱롱롱해롱해': Less than (<)
- '해롱해롱롱해해': Greater than or equal to (>=)
- '해해롱롱해롱해': Less than or equal to (<=)

### Conditional Statements
- After typing '해롱해롱롱해', if the value stored in the following variable is true, the next command will be executed.
- '해롱해롱롱해롱' evalates the next condition if the previous condition is false, and if ture, executes the next command.
- '해롱해롱롱해롱해롱' evalates the next condition if all previous conditions are false.
- Input '롱롱' to mark the end of the command block inside the conditional statement.

&nbsp;

> &nbsp;
>
> **Structure**\
> 해롱해롱롱해 (variable 1)\
> (command 1)\
> 해롱해롱롱해롱 (variable 2)(optional)\
> (command 2)\
> 해롱해롱롱해롱해롱 (variable 3)(optional)\
> (command 3)\
> 롱롱
>
> &nbsp;
>

### Loops
- After typing '해롱롱롱', enter four variables: index variable, start index, end index, and increment value.
- Repeat the commands entered before the '롱롱' termination command.

&nbsp;

> &nbsp;
>
> **Structure**\
> 해롱롱롱 (start index) (end index) (increment)\
> (command)\
> 롱롱
>
> &nbsp;
>

## Contributors
### 1) Shine Loi Lee
- Github: [https://github.com/Shine-Loi-Lee/]
- Blog: [https://shineloilee.wordpress.com/]

### 2) minhowow

## License
This project is licensed under the MIT License - see the LICENSE file for details.
