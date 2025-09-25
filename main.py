import lexer
from parser import Parser

code = """
deerdeer food = "kwaychap";
tutu numberofdrinks = 2;
duckduck morning = True;
print(food);
"""

tokens = lexer.tokenise(code)
print(tokens)

p = Parser(tokens)

print(p.peek())
p.advance()
print(p.peek())
p.advance()
print(p.peek())
p.advance()
print(p.peek())
p.advance()
print(p.peek())
