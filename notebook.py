import datetime

# Store the next available id for all new notes
lastId = 0

class Note:
    '''Represents a note in a notebook. Store tags for each note.
    Match against a string in searches'''

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional space-separated tags. 
        Automatically set the note's creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creationDate = datetime.date.today()
        global lastId
        lastId += 1
        self.id = lastId

    def match(self,filter):
        '''Determine if this note matches the filter text.
        Return True if it matchs, False otherwise.
        
        Search is case sensitive and matches both text and tags'''
        return filter in self.memo or filter in self.tags
    
    


    




