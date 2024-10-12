import re;

class Parser():
    def _parse_type(type): # Return the type of the variable
        if type == '해롱롱':
            return 'number'
        elif type == '해해롱':
            return 'string'
        else:
            raise RuntimeError(f"Unexpected type: {type}")

    TYPEMAPPING = {
        'string': lambda x: chr(int(x.replace('해', '1').replace('롱', '0'), 2)),
        'number': lambda x: int(x.replace('해', '1').replace('롱', '0'), 2),
        'command': lambda x: x,
        'variable': lambda x: x,
        'type': _parse_type
    }

    def __init__(self, cmd: str):
        self.tokens = cmd.split(' ')
        self.pos = 0
    
    def has_next(self): # Check if there is a next token
        return self.pos < len(self.tokens)
    
    def assert_end(self): # Check if there are no more tokens
        if self.pos < len(self.tokens):
            raise RuntimeError(f"Unexpected token: {self.tokens[self.pos]}")

    def next_token(self, type): # Get the next token
        if self.pos >= len(self.tokens):
            raise RuntimeError("Unexpected end of input")
        token = self.tokens[self.pos]
        
        if(not re.match(r'^[해롱]+$', token)):
            raise RuntimeError(f"Unexpected token: {token}")
        
        self.pos += 1
        
        return Parser.TYPEMAPPING[type](token)
