========================================
CATLANG COMPILER - README
========================================

1. INTRODUCTION
---------------
The Catlang Compiler is a small, experimental language processor that interprets 
and executes "Catlang" code. Catlang is a toy language with basic control-flow 
constructs, such as:

- catfor loops
- catwhile loops
- catif conditionals
- catspeak statements (for printing)
- Variable assignments

2. FEATURES
-----------
- **Tokenization**: Splits the source code into a list of tokens.
- **Parsing**: Builds an Abstract Syntax Tree (AST) from the tokens, understanding
  Catlang constructs like `catfor`, `catwhile`, `catif`, `catspeak`, and 
  variable assignments.
- **Evaluation**: Walks through the AST, interpreting the program logic:
  - Loops (`catfor`, `catwhile`)
  - Conditionals (`catif`)
  - Output (`catspeak`)
  - Assignments (`x = expression`)

3. HOW IT WORKS
---------------
a) **Tokenize**  
The `tokenize` method uses a regular expression to break down the code into 
strings, keywords, numbers, and symbols.  

b) **Parse**  
The `parse` method walks through the token list, building an AST for each 
Catlang construct:
- `catfor i = 1 to 5`: A for-loop node with a start and end value.
- `catwhile x < 10 do ... endcat`: A while-loop node with a condition and body.
- `catif x < y then ... endcat`: An if-statement node with a condition and body.
- `catspeak "Hello"`: A print statement.
- `x = 5 + 10`: An assignment node, storing the result of an expression in a variable.

c) **Evaluate**  
The `evaluate` method recursively processes the AST:
- For loops: Executes the body from start to end.
- While loops: Repeatedly checks the condition, executing the body while true.
- If statements: Executes the body if the condition is true.
- Print statements: Prints strings or expressions to standard output.
- Assignments: Evaluates the expression and stores the result in a dictionary of variables.

4. EXAMPLE CODE
---------------
Here is a sample Catlang program:
"""
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
"""

5. USAGE
--------
a) **Prerequisites**  
- Python 3.x

b) **Running the Compiler**  
1. Save the Catlang code into a file, for example: `program.cat`.
2. Place the `CatlangCompiler` code into `catlang_compiler.py`.
3. At the bottom of `catlang_compiler.py`, replace the test `code` string with 
   the contents of your `program.cat`, or read from a file if you wish.
4. Run the script:
This will tokenize, parse, and evaluate the Catlang code, printing the results 
to your console.

6. CUSTOMIZATION
----------------
- You can enhance the Catlang language by adding more features in the `parse` 
method. For instance, new keywords or data types.
- Update the `evaluate_expression` method if you need more robust or restricted 
evaluation logic (for example, to disallow certain Python built-ins).

7. TROUBLESHOOTING
------------------
- If you see `Error evaluating expression`: This likely means there is a syntax 
issue or an undefined variable in your Catlang code.
- Make sure that each control-flow construct (`catfor`, `catwhile`, `catif`) is 
properly closed with `endcat` or `do ... endcat`.

8. LICENSE
----------
This project is provided as-is for educational and experimental purposes. Feel free
to modify and use it in any way you see fit.

9. CONTRIBUTIONS
----------------
Pull requests or suggestions are welcome to improve the grammar, error handling,
and feature set of Catlang.

========================================
Thank you for using the Catlang Compiler!
