class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search
        value in their name.'''
        matchContacts = []
        for contact in self:
            if name in contact.name:
                matchContacts.append(contact)
        return matchContacts
    
class Contact:
    allContacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.allContacts.append(self)