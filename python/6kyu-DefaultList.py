class DefaultList:
    '''
    The collections module has defaultdict, which gives you a default value for trying to get the value of a key 
    which does not exist in the dictionary instead of raising an error. 
    Why not do this for a list?

    Your job is to create a class (or a function which returns an object) called DefaultList. 
    The class will have two parameters to be given: a list, and a default value. 
    The list will obviously be the list that corresponds to that object. 
    The default value will be returned any time an index of the list is called in the code that 
    would normally raise an error (i.e. i > len(list) - 1 or i < -len(list)). 
    This class must also support the regular list functions extend, append, insert, remove, and pop.

    Because slicing a list never raises an error (slicing a list between two indexes that are not a part of the list returns [], slicing will not be tested for.
    '''
    def __init__(self, list, default):
        self.list = list
        self.default = default
        
    def check_index(self, value):
        if value > len(self.list) - 1 or value < -len(self.list):
            return False
        return True
    
    def __getitem__(self, index):
        if not self.list:
            return self.default
        return self.list[index] if self.check_index(index) == True else self.default
    
    def extend(self, extension):
        self.list = self.list + extension
    
    def append(self, value):
        self.list.append(value)
       
"""
Another solution using super()

class DefaultList(list):

    def __init__(self, lst, default):
        self.default = default
        super().__init__(lst)

    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            return self.default
"""
        
    def remove(self, value):
        if value in self.list:
            self.list.remove(value)
    
    def insert(self, index, value):
        self.list.insert(index, value)
    
    def pop(self, index):
        if self.check_index(index) == False:
            return self.default
        else:
            del self.list[index]
