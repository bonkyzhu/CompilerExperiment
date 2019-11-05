import string 

word = [
	"begin", "call", "const", "do",
	"end", "if", "odd", "procedure",
	"read", "then", "var", "while", "write", 
]

symbol = {
    '+': "plus", '-': "minus", '*': "times", '/': "slash",
	'(': "lparen", ')': "rparen", '=': "eql", ',': "comma",
	'.': "period", '#': "neq", ';': "semicolon"
}

code = open('in.txt').read()

ch = ' '
i = 0
line = 1
index = 0
length = len(code)
ascii_letters, digits = list(string.ascii_letters), list(string.digits)
save = ''