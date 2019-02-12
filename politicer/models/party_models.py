import json

parties = {}

class Party():
    def __init__(self, name, hqAddress, logoUrl, id=0):
        '''Party create
        Arguments:
            name {[string]} 
            hqAddress {[string]} 
            logoUrl {[string]} 
        
        '''
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = self.create_id()

    ''' returns string string representations of the dictionary object '''
    def serialize(self):
        return {
            'id' : self.id,
            'name': self.name, 
            'hqAddress': self.hqAddress,
            'logoUrl': self.logoUrl,
        }

    ''' autogenerate id for new_party '''
    def create_id(self, id=0):
        if id == 0:
            id = len(parties)+1
        
        if id in parties:
            id = id+1
            return self.create_id(id)
        return id

    ''' returns a dict object '''
    def party_dict(self):
        return dict(id=self.id)

    def detail_list(self):
        '''get all attributes of the object '''
        return dict(id=self.id, name=self.name, hqAddress=self.hqAddress , logoUrl=self.logoUrl)
    
    def get_parties(self):
        return dict(id=self.id, name=self.name, logoUrl=self.logoUrl)

    ''' Insert the object into the list of parties  '''
    def save_party(self):
        parties[self.id] = self

    def update_name(self, name, hqAddress):
        ''' updates name and hqAddress of a party '''
        self.name = name
        self.hqAddress = hqAddress

    def delete_party(self):
        ''' remove the object from the list of parties '''
        del parties[self.id]
    
    def delete_parties(self):
        parties.clear()

    ''' function to be used to check for duplicates in the list '''
    def check_name(self, name=None):
        if name == None:
            name = self.name
        for x in parties:
            if parties[x].name == name:
                return x
        return False

