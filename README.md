Catlang Compiler
The Catlang Compiler is a lightweight, educational programming language interpreter designed in Python. Inspired by cat-themed commands, it offers a unique and fun way to learn the basics of language parsing, tokenization, and AST evaluation.

Features
Custom Commands:
catspeak: Print a string or evaluate and print an expression.
catfor: Execute a block of code in a loop with a specified range.
catwhile: Execute a block of code while a condition is true.
catif: Execute a block of code conditionally.
Basic Arithmetic and Variables:
Support for variable assignments and basic arithmetic expressions.
Example Code
Here's an example of a Catlang program:

plaintext
Copy code
catspeak "Hello from Catlang!"

x = 1
y = 5

catif x < y then
    catspeak "x is less than y"
endcat

catfor i = 1 to 3
    catspeak i
endcat

catwhile x < 4 do
    catspeak "Hello "
    catspeak x
    x = x + 1
endcat

catspeak "Goodbye!"
Output:
csharp
Copy code
Hello from Catlang!
x is less than y
1
2
3
Hello 
1
Hello 
2
Hello 
3
Goodbye!
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/catlang-compiler.git
Navigate to the project directory:
bash
Copy code
cd catlang-compiler
Ensure you have Python 3.x installed.
Usage
Save your Catlang code in a .txt or .cat file.
Modify the code variable in CatlangCompiler to point to your program or paste the program as a string.
Run the script:
bash
Copy code
python catlang_compiler.py
Code Structure
tokenize: Converts the source code into tokens for parsing.
parse: Converts tokens into an Abstract Syntax Tree (AST).
evaluate: Executes the AST.
Supported Commands
catspeak: Prints a string or evaluates an expression.
plaintext
Copy code
catspeak "Hello!"
catfor: Executes a loop for a given range.
plaintext
Copy code
catfor i = 1 to 3
    catspeak i
endcat
catwhile: Executes a loop while a condition is true.
plaintext
Copy code
catwhile x < 5 do
    catspeak x
    x = x + 1
endcat
catif: Executes a block of code if a condition is true.
plaintext
Copy code
catif x < y then
    catspeak "Condition is true"
endcat
Contributing
Feel free to fork the repository and submit pull requests to add features or improve the code.

Fork the project.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add new feature"
Push to your branch:
bash
Copy code
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
