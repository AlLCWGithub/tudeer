KEYWORDS = {
"tutu", "deerdeer", "pikachu", "duckduck", "cookiemonster", "bluedrink", "return", "if", "else", "elif", "while", "for", "print", "True", "False"
}

SYMBOLS = {
"(", ")", "{", "}", ";", ","
}

OPERATORS = {
'==', '!=', '<=', '>=', '&&', '||', '+', '-', '*', '/', '<', '>', '='
}

def tokenise(source):
	tokens = []
	i = 0
	while i < len(source):
		c = source[i]
		if c.isspace():
			i += 1
			continue
		elif c.isdigit():
			num = c
			i += 1
			while i < len(source) and (source[i].isdigit() or source[i] == '.'):
				num += source[i]
				i += 1
			tokens.append(('NUMBER', float(num) if '.' in num else int(num)))
			continue
		elif c.isalpha():
			ident = c
			i += 1
			while i < len(source) and (source[i].isalnum() or source[i] == "_"):
				ident += source[i]
				i += 1
			if ident in KEYWORDS:
				tokens.append(("KEYWORD", ident))
			else:
				tokens.append(("IDENT", ident))
			continue
		matched = False
		for op in sorted(OPERATORS, key=len, reverse=True):
			if source.startswith(op, i):
				tokens.append(("OPERATOR", op))
				i += len(op)
				matched = True
		if matched:
			continue
		if c in SYMBOLS:
			tokens.append(("SYMBOL", c))
			i += 1
			continue
		elif c == '"' or c == "'":
			quote = c
			i += 1
			stringval = ""
			while i < len(source) and source[i] != quote:
				stringval += source[i]
				i += 1
			if i >= len(source):
				raise ValueError("Unterminatd string")
			i += 1
			tokens.append(("STRING", stringval))
			continue
		raise ValueError(f"Unknown charcter: {c}")
	return tokens
