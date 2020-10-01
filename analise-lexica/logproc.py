# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
] 
t_ignore  = '\t\n'
def t_TIMESTAMP(t):
    # Regular expression for TIMESTAMP
    r'([0-9:.])+\s([0-9\-\+])+(?=\t)'
    return t

def t_PROC(t):
    # Regular expression for PROC
    r'[\w -\.]+(?=\t)'
    t.value = t.value[:len(t.value)]
    return t

def t_MESSAGE(t):
    # Regular expression for MESSAGE
    r'[^	]+(?=\n)'
    t.value = t.value[:len(t.value)]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0:100])
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None
    def __init__(self):
        fh = open("log", 'r')
        # fh = open("teste.txt", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def collect_messages(self):
        tokens = []
        current_proc=''
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            if tok.type == 'PROC':
                current_proc=tok.value
            if tok.type == 'MESSAGE' and current_proc =='kernel':
                tokens.append(tok)
        return tokens
        
if __name__ == '__main__':
#     f = open("demofile3.txt", "w")
# f.write(str(LogProcLexer().collect_messages()))
# f.close()
    print(LogProcLexer().collect_messages())
    
