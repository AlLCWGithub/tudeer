class Parser:
	def __init__(self, tokens):
		self.tokens = tokens + [("EOF", '')]
		self.i = 0
		self.cached_token = None
	def peek(self):
		return self.tokens[self.i]
	def advance(self):
		token = self.tokens[self.i]
		self.i += 1
		return token
	def match(self, type_, value=None):
		t = self.peek() 
		if t[0] != type_: # Renamed type to prevent overshadowing of native function 'type' 
			return False
		if value is not None and t[1] != value: 
			return False
		self.advance()
		return True
	def expect(self, type_, value=None):
		if not self.match(type_, value):
			raise SyntaxError(f"Expected {type_} {value}, got {self.peek()}")
	def parseprogram(self):
		statements = []
		match_,parsestatement = self.match,self.parsestatement # Micro optimisation that prevents many function calls
		while not match_("EOF"):
			statements.append(parsestatement())
		return ("program", statements)
