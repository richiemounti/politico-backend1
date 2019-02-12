import json

offices = {}
officeTypes = ['federal', 'legislative', 'state', 'local government']

class Office():
    '''Office create
    Arguments:
        name {[string]} 
        type {[string]}  
    
    '''
    def __init__(self, name, type, id=0):
        self.name = name
        self.type = type
        self.id = self.create_id()

    ''' returns string string representations of the dictionary object '''
    def serialize(self):
        return {
            'id' : self.id,
            'name': self.name, 
            'type': self.type,
        }
    ''' autogenerate id for new_office '''
    def create_id(self, id=0):
        if id == 0:
            id = len(offices)+1
        
        if id in offices:
            id = id+1
            return self.create_id(id)
        return id

    '''get all attributes of the object '''
    def office_list(self):
        return dict(id=self.id, name=self.name, type=self.type)

    ''' returns a dict object '''
    def office_dict(self):
        return dict(id=self.id)
    
    ''' Insert the object into the list of offices  '''
    def save_office(self):
        offices[self.id] = self

    ''' updates name and type of office '''
    def update_name(self, name, type):
        self.name = name
        self.type = type
    ''' function to be used to check for duplicates in the list '''
    def check_name(self, name=None):
        if name == None:
            name = self.name
        for x in offices:
            if offices[x].name == name:
                return x
        return False
