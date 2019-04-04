
'''
    A class that represents a person who has purchased a ticket
'''

class Person():

    def __init__(self, ID, name, email):
        '''
            Init function for person class
        '''
        self.ID = str(ID)
        self.name = name
        self.email_address = email

    def toString(self):
        '''
            Method that returns user information seperated by commas
        '''
        return self.ID + "," + self.name + "," + self.email_address