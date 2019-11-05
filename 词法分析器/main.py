import sys
from setting import *

def savestr(sentence):
    global save
    save += sentence
    save += '\n'

def getch():
    global i, ch, line, index
    if i == length:
        savestr("complete")
        with open('out.txt', 'w') as f:
            f.write(save)
        print("词法分析完成")
        sys.exit()
    if ch == '\n':
        line += 1
    ch = code[i]
    i += 1

def getsym():
    while ch == ' ' or ch == '\n' or ch == '\t':
        getch()
    a = ''
    if ch in ascii_letters:
        while True:
            a += ch
            getch()

            if ch not in ascii_letters and ch not in digits:
                break
        if a in word:
            sym = a + 'sym'
            savestr(f"保留字  {a} {sym}")
        else:
            sym = "ident"
            savestr(f"标识符 {a} ")
    else:
        if ch in digits:
            a = ''
            while True:
                a += ch
                getch()

                if ch not in ascii_letters and ch not in digits:
                    break
            if set(list(a)) - set(digits):
                error()
            else:
                sym ='number'
                savestr(f"数字 {int(a)}")
        else:
            if ch == ':':
                getch() 
                if ch =='=':
                    sym ='becomes'
                    getch()
                    savestr("赋值符号 :=")
                else:
                    sym ='nul'
            else:
                if ch == '<':
                    getch()
                    if ch == '=':
                        sym = 'leq'
                        getch()
                        savestr("小于等于号 <=")
                    else:
                        sym = 'lss'
                        getch()
                        savestr("小于号 <")
                else:
                    if ch == '>':
                        getch()
                        if ch == '=':
                            sym = 'geq'
                            getch()
                            savestr("大于等于号 >=")
                        else:
                            sym = 'gtr'
                            getch()
                            savestr("大于号 >")
                    else:
                        sym = symbol[ch]
                        savestr(f"{sym} {ch}")
                        if sym != 'period':
                            getch()

def error():
    print(f"error in line {line}")
    savestr(f"error in line {line}")
    # sys.exit()

if __name__ == "__main__":
    while True:
        getsym()
    print()