class Parser:
	def __init__(self, tokens):
		self.tokens = tokens + [("EOF", '')]
		self.i = 0
	def peek(self):
		return self.tokens[self.i]
	def advance(self):
		token = self.tokens[self.i]
		self.i += 1
		return token
	def match(self, type, value=None):
		t = self.peek()
		if t[0] != type:
			return False
		if value is not None and t[1] != value:
			return False
		self.advance()
		return True
	def expect(self, type, value=None):
		if not self.match(type, value):
			raise SyntaxError(f"Expected {type} {value}, got {self.peek()}")
	def parseprogram(self):
		statements = []
		while not self.match("EOF"):
			statements.append(self.parsestatement())
		return ("program", statements)
