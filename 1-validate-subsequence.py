def isValidSubsequence(array, sequence):
    previousIndex = 0
    currentIndex = 0
    for partOfSequence in sequence:
        isPartOfSequence = False
        for number in array:
            previousIndex = currentIndex
            if partOfSequence == number:
                print(currentIndex)
                currentIndex = array.index(number)
                if currentIndex >= previousIndex:
                    array.remove(number)
                    isPartOfSequence = True
        if isPartOfSequence == False:
            return False
    return True
    pass
