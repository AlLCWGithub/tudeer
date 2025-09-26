import lexer
from parser import Parser
import cProfile,pstats,io

code = """
deerdeer food = "kwaychap";
tutu numberofdrinks = 2;
duckduck morning = True;
print(food);
"""

profiler = cProfile.Profile() # Comment out if don't need profiling
profiler.enable() # Comment out if don't need profiling
tokens = lexer.tokenise(code)
profiler.disable() # Comment out if don't need profiling
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

# If you want to print profiling stats use this below (comment it out if not checking for function speed)

s = io.StringIO()
ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
ps.print_stats()
print(s.getvalue())
