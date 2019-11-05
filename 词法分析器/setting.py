nmax = 14
norw = 13       
txmax = 100     
al = 10         
maxerr = 30     
amax = 2048     
levmax = 3      
cxmax = 200     
stacksize = 500 

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