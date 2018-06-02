import random
import string

WORDLIST_FILENAME = "palavras.txt"

# This method load the words avaliable from a txt file. It returns how many words
#were loaded.
def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)

# Alalyses if the letter choosed by user is in the word.Returns true in case the
#letter is in the word or false if doesn't.
def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True

# Get all the avaliable letters from the ascii . Returns a string containing all
#the letters
def getAvailableLetters():
    import string

    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available

# Print the sotfware initial message to user.
def printInitialMessage(secretWord):
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

#Print the answer in the console.
def printAnswer(letter,lettersGuessed,secretWord,guessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed


# Main method.
def hangman(secretWord):

    guesses = 8
    lettersGuessed = []

    printInitialMessage(secretWord)

    #main loop
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        available = getAvailableLetters()

        print 'You have ', guesses, 'guesses left.'
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        guessed = ''
        if letter in lettersGuessed:

            guessed = printAnswer(letter,lettersGuessed,secretWord,guessed)

            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = printAnswer(letter,lettersGuessed,secretWord,guessed)

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = printAnswer(letter,lettersGuessed,secretWord,guessed)

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'




secretWord = loadWords().lower()
hangman(secretWord)
