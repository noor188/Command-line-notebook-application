from note import Note

class Notebook:
    '''Represents a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
    
    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [noteMemo for noteMemo in self.notes if noteMemo.match(filter)]

    def newNote(self, **kwargs):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(**kwargs))
       
    def _findNote(self, noteId):
        '''Locate the note with the given id.'''        
        for note in self.notes:
            if str(note.id) == str(noteId):
                return note
        return None        
    
    def modifyMemo(self, noteId, memo):
        '''Find the note with the given id and change its memo to the given value.'''
        note = self._findNote(noteId)
        if note:
            note.memo = memo 
            return True
        return False
    
    def modifyTags(self, noteId, tags):
        '''Find the note with the given id and change its tag to the given tags.'''
        note = self._findNote(noteId)
        if note :
            note.tags = tags
            return True
        return False