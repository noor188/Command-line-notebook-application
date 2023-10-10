
import note

class Notebook:
    '''Represents a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
    
    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [noteMemo for noteMemo in self.notes if noteMemo.match(filter)]

    def newNote(self, memo, tags =''):
        '''Create a new note and add it ti the list.'''
        self.notes.append(note.Note(memo,tags))

    def _findNote(self, noteId):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if note.id == noteId:
                return note
        return None
    
    def modifyMemo(self, noteId, memo):
        '''Find the note with the given id and change its memo to the given value.'''
        self._findNote(noteId).memo = memo
    
    def modifyTags(self, noteId, tags):
        '''Find the note with the given id and change its tag to the given tags.'''
        self._findNote(noteId).tags = tags