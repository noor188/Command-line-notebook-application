class Contact:
    allContacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.allContacts.append(self)

class Supplier(Contact):

    def order(self, order):
        print('if this were a real system we would send {} order to {}'.format(order, self.name))


class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class longestNameDict(dict):
    def longest_key(self):
        longest = None 
        for key in self:
            if not longest or len(key)> len(longest):
                longest = key
        return longest
    
class SecretString:
    '''A not-at-all secure way to store a secret string'''

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase  = pass_phrase
    
    def decrypt(self, pass_Phrase):
        '''Only show the string if the pass_phrase is correct.'''

        if pass_Phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return 'jhg'


