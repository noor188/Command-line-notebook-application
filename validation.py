
def getValidInput(inputString, validOptions):
    inputString += '  ({}) '.format(', '.join(validOptions))
    response = input(inputString)
    while response not in validOptions:
        response = input(inputString)
    
    return response