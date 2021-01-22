class Dictionary(dict):
    '''
    In this kata, your job is to create a class Dictionary which you can add words to and their entries. 
    >>> d = Dictionary()

    >>> d.newentry('Apple', 'A fruit that grows on trees')

    >>> print(d.look('Apple'))
    A fruit that grows on trees

    >>> print(d.look('Banana'))
    Can't find entry for Banana
    '''
    def __init__(self):
        self.dict_ = {}
        
    def new_entry(self, word, definition):
        self.dict_[word] = definition
        
    def look(self, key):
        if key in self.dict_.keys():
            return self.dict_[key]
        return f"Can't find entry for {key}"
