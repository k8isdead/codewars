import re

def validate_pin(pin):
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    return False
    
