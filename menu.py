import sys
from note import Note
from notebook import Notebook
from validation import getValidInput

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.searchNotes,
            '3': self.addNote,
            '4': self.modifyNote,
            '5': self.quit
        }
    
    def displayMenu(self):
        print("""
            Notebook Menu
              
              1. Show all Notes
              2. Search Notes
              3. Add Note
              4. Modify Note
              5. Quit
                """)
    
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.displayMenu()
            choice = getValidInput('Enter an option: ', self.choices.keys())
            action = self.choices.get(choice)
            if action :
                action()
            else:
                print('{0} is not a valid choice'.format(choice))

    def show_notes(self, notes= None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print('{0}: {1}\n{2}'.format(note.id, note.tags, note.memo))    
    
    def searchNotes(self):
        filter = input('Search for: ')
        if filter:
            notes = self.notebook.search(filter)
            self.show_notes(notes)
        else:
            print('You did not enter a keyword, try again an enter a keyword')

    def addNote(self):        
        initArgs = Note.promptInit()
        if initArgs['memo']:
            self.notebook.newNote(**initArgs)
            print('Your note has been added')
        else:
            print('You did not enter a memo, try again an type a memo text')
                
    def modifyNote(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input('Enter tags: ')
        if memo :
            if not self.notebook.modifyMemo(id, memo):
                print('You entered an invalid Id')
        if tags:
            if not self.notebook.modifyTags(id, tags):
                print('You entered an invalid Id')
        
    def quit(self):
        print('Thank you for using your notebook today.')
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()    



