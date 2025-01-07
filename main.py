import re

class CatlangCompiler:
    def __init__(self):
        self.variables = {}

    def tokenize(self, code):
        return re.findall(r'"[^"]*"|[a-zA-Z_][a-zA-Z_0-9]*|[0-9]+|\S', code)

    def parse(self, tokens):
        ast = []
        i = 0
        while i < len(tokens):
            token = tokens[i]

            # -----------------------
            # catfor i = 1 to 5
            # -----------------------
            if token == 'catfor':
                # Example: catfor i = 1 to 5
                # tokens structure: [catfor, i, =, 1, to, 5, ...]
                var = tokens[i + 1]         # 'i'
                # tokens[i + 2] should be '='
                start = int(tokens[i + 3])  # 1
                # tokens[i + 4] should be 'to'
                end = int(tokens[i + 5])    # 5

                i += 6

                # Gather loop body tokens until 'endcat'
                body_tokens = []
                while tokens[i] != 'endcat':
                    body_tokens.append(tokens[i])
                    i += 1

                # Recursively parse the loop body
                ast.append(('catfor', var, start, end, self.parse(body_tokens)))

            # -----------------------
            # catwhile x < 10 do ... endcat
            # -----------------------
            elif token == 'catwhile':
                i += 1  # skip the 'catwhile' token
                condition_tokens = []
                while tokens[i] != 'do':
                    condition_tokens.append(tokens[i])
                    i += 1

                i += 1  # skip 'do'

                # Gather body tokens until 'endcat'
                body_tokens = []
                while tokens[i] != 'endcat':
                    body_tokens.append(tokens[i])
                    i += 1

                # Recursively parse the while-loop body
                ast.append(('catwhile', condition_tokens, self.parse(body_tokens)))

            # -----------------------
            # catif x < y then ... endcat
            # -----------------------
            elif token == 'catif':
                i += 1  # skip 'catif'
                condition_tokens = []
                while tokens[i] != 'then':
                    condition_tokens.append(tokens[i])
                    i += 1

                i += 1  # skip 'then'

                # Gather body tokens until 'endcat'
                body_tokens = []
                while i < len(tokens) and tokens[i] != 'endcat':
                    body_tokens.append(tokens[i])
                    i += 1

                # Recursively parse the if-body
                ast.append(('catif', condition_tokens, self.parse(body_tokens)))

            # -----------------------
            # catspeak "something"
            # -----------------------
            elif token == 'catspeak':
                # Next token should be the message (string or expression)
                message = tokens[i + 1]
                ast.append(('catspeak', message))
                i += 1

            # -----------------------
            # x = some_expression
            # -----------------------
            elif (
                re.match(r'[a-zA-Z_][a-zA-Z_0-9]*', token) and
                i + 1 < len(tokens) and
                tokens[i + 1] == '='
            ):
                var_name = token
                i += 2  # skip over var_name and '='

                # Gather expression tokens until a "stop token" or new assignment
                expr_tokens = []
                stop_tokens = {
                    'catspeak', 'catif', 'catfor',
                    'catwhile', 'endcat', 'do', 'then'
                }

                while i < len(tokens):
                    # If we hit a known stop token, break
                    if tokens[i] in stop_tokens:
                        break
                    # If the next token looks like a new var=, break
                    if (
                        re.match(r'[a-zA-Z_][a-zA-Z_0-9]*', tokens[i]) and
                        (i + 1) < len(tokens) and
                        tokens[i + 1] == '='
                    ):
                        break

                    expr_tokens.append(tokens[i])
                    i += 1

                expr_str = " ".join(expr_tokens)
                ast.append(('assign', var_name, expr_str))

                # Step back so the while-loop doesn't skip a token
                i -= 1

            else:
                # Could be 'endcat', a comment, or unknown token
                pass

            i += 1

        return ast

    def evaluate(self, ast):
        """Evaluate the parsed AST."""
        for node in ast:
            ntype = node[0]

            if ntype == 'catfor':
                # node = ('catfor', var, start, end, body_ast)
                var_name, start, end, body_ast = node[1], node[2], node[3], node[4]
                for loop_index in range(start, end + 1):
                    self.variables[var_name] = loop_index
                    self.evaluate(body_ast)

            elif ntype == 'catwhile':
                # node = ('catwhile', condition_tokens, body_ast)
                condition_tokens, body_ast = node[1], node[2]
                while self.evaluate_expression(" ".join(condition_tokens)):
                    self.evaluate(body_ast)

            elif ntype == 'catif':
                # node = ('catif', condition_tokens, body_ast)
                condition_str = " ".join(node[1])
                if self.evaluate_expression(condition_str):
                    self.evaluate(node[2])

            elif ntype == 'catspeak':
                # node = ('catspeak', message)
                message = node[1]
                if message.startswith('"') and message.endswith('"'):
                    # If it's a quoted string like "Hello"
                    print(message.strip('"'))
                else:
                    # Otherwise, evaluate as an expression
                    print(self.evaluate_expression(message))

            elif ntype == 'assign':
                # node = ('assign', var_name, expr_str)
                var_name, expr_str = node[1], node[2]
                self.variables[var_name] = self.evaluate_expression(expr_str)
    
    def evaluate_expression(self, expr):
        """Safely evaluate expressions using Python's eval with a restricted namespace."""
        try:
            # If the entire expr is just digits, return int
            if expr.isdigit():
                return int(expr)
            # If expr is exactly a known variable
            elif expr in self.variables:
                return self.variables[expr]
            else:
                # Otherwise, treat it as a Python expression
                return eval(expr, {}, self.variables)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expr}': {e}")

if __name__ == '__main__':
            # -----------------------
            # C A T L A N G  C O D E
            # -----------------------
    code = """
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
    compiler = CatlangCompiler()
    tokens = compiler.tokenize(code)
    ast = compiler.parse(tokens)
    compiler.evaluate(ast)
