# -*- coding: utf-8 -*-
#Cheating Hangman By: Ashley Wenz & Billy Reynolds
#CSC335A Spring 2020
import sys
insert = {}
insert.
file = open("dictionary.txt", "r")
guessAmt = 0
myWord = []
#create list of used letters to track
letters = []
table = [] 
def startup():
#get word length
    wordLen = input("Enter word length: ")
    wordLen = int(wordLen)
    while wordLen < 1:
        wordLen = input("Enter word length: ")
        wordLen = int(wordLen)
     
#create list to track current word (starts all -)
    for i in range (wordLen):
        myWord.append('-')
    
#get number of guesses
    guessAmt = input("Enter amount of guesses: ")
    guessAmt = int(guessAmt)
    while guessAmt < 1:
         guessAmt = input("Enter amount of guesses: ")
         guessAmt = int(guessAmt)
         
    #strips new lines from the .txt file        
    for line in file:
        if len(line)-1 == wordLen:
            table.append(line.strip("\n"))     
    givMeALet(table,guessAmt)
    
    #handles when wordFam's biggest family has 1 matching letter
def OnewordFam(let, theFam):
    oneFam = {}
    #loops through all the words and stores the index and word as key, value pair
    for thing in theFam:
        ind = thing.find(let)
        oneFam[thing] = ind
    #finds what index is most common 
    freq1 = {}
    for key,value in oneFam.items():
        if value not in freq1:
            freq1[value]=0
        else:
            freq1[value]+=1
    popInd = (max(freq1,key=freq1.get))
    #creates list of all the words with the matching most common index
    oneFinFam = []  
    for key,value in oneFam.items():
        if value is popInd:
            oneFinFam.append(key) 
    myWord.insert(popInd,let)
    myWord.pop(popInd+1)
    return oneFinFam

#handles when wordFam's biggest family has 2 matching letters
def TwowordFam(let, theFam):
    twoFam = {}
    #loops through all the words and stores (first index, second index) and word as key, value pair
    for thing in theFam:
        first = thing.index(let)
        ind = 0
        for letter in thing:
            if letter is let:
                if ind is not first:
                    twoFam[thing] = (first, ind)
            ind +=1
    #identifies which indices are the most common
    freq = {}
    for key,value in twoFam.items():
        if value not in freq:
            freq[value]=0
        else:
            freq[value]+=1
    popInd = (max(freq,key=freq.get))
    #creates list of all the words with the matching most common index
    twoFinFam = []  
    for key,value in twoFam.items():
        if value is popInd:
            twoFinFam.append(key)   
    #Gets first instance of the letter
    myWord.insert(value[0], let)
    myWord.pop(value[0]+1)
    #Gets second instance of the letter
    myWord.insert(value[1],let)
    myWord.pop(value[1]+1)

    return twoFinFam
#Method to deal with letters that appear more than twice          
def PolyWordFam(let, theFam):
    polyFam = []
    #Finds the first indices
    for thing in theFam:
        first = thing.index(let)
        ind = 0
        for letter in thing:
            if letter is let:
                if ind is not first:
                    #List all, but the first indices of the letter
                    polyFam.append(ind)
            ind +=1
    #Adds the first index of the letter
    polyFinFam = []  
    polyFinFam.append(first)
    myWord.insert(first, let)
    myWord.pop(first+1)
    #Loops through and adds the rest of the indices
    for value in polyFam:
        polyFinFam.append(value)  
        myWord.insert(value,let)
        myWord.pop(value+1)
    return theFam

#creates the word families and returns the largest one
def wordFamily(let, lis):
    # create as many arrays as there are letters in the word in addition to an array for 0
    family = {}
    freq = {}
    #look at each word in given list
    for obj in lis:
        count = 0
        #look at each letter in given word
        for letter in obj:
            if letter is let:
                count = count + 1
            family[obj] = count  
        #check which amount of times the letter appears is most common
        for key,value in family.items():
            if value not in freq:
                freq[value]=0
            else:
                freq[value]+=1
    most = (max(freq,key=freq.get))
    #create a list of the words with the most common amount of times the letter appears
    theFam = []
    for key,value in family.items():
        if value is most:
            theFam.append(key)

    if most == 1:
        oneLetter = OnewordFam(let, theFam)
        return oneLetter

    elif most == 2:
        twoLetter = TwowordFam(let, theFam)
        return twoLetter
    elif most > 2:
        polyLetter = PolyWordFam(let, theFam)
        return polyLetter
    else:
        return theFam
    
#loops through asking for letters till you win or lose
def givMeALet(words,guessAmt):
        #check to see if user wants to know amount of remaining words
    remain = input("Do you want to know the amount of words remaining? (y/n): ")
    while not(remain == 'y' or remain == 'n'):
         remain = input("Do you want to know the amount of words remaining? (y/n): ")
    if remain == 'y':
         print(len(words))
    guess = 0
    while len(words) > 1 and guessAmt > guess or '-' in myWord: #While loop to manage prompts while the word is still isn't guessed or the user hasn't used all the guesses
        letter = input("Choose a letter: ")
        while not(len(letter) == 1 and letter not in letters):
            letter = input("Letter already chosen, choose another letter: ")
        letters.append(letter)
        if(guess+1 != guessAmt or len(myWord)+1 != len(words[0])):          #If there are two or more choices left, with only one guess remaining, the loser will lose.
            nxtList = wordFamily(letter, words)
            words = nxtList
            if remain == 'y':
                print (len(words))
        print(myWord)
        if letter not in myWord:
            guess = guess + 1
        print("Guesses remaining: ", guessAmt - guess)
        check = ""
        for x in myWord:
            check+=x
        if check== words[0]: #The user won!
            print("You guessed the word! You won!!")
            again = input("Do you want to play again? ")
            while not(again =='y' or again == 'n'):
                again = input("Do you want to play again? (y/n) ")
            if again == "y":
                letters.clear()
                myWord.clear()
                startup()
            if again =="n":
                print("Goodbye!!")
                sys.exit()
        elif guess == guessAmt: #The user lost!
            print("You lost! Better luck next time!")
            again = input("Do you want to play again? ")
            while not(again =='y' or again == 'n'):
                again = input("Do you want to play again? (y/n) ")
            if again == "y":
                letters.clear()
                myWord.clear()
                startup()
            if again =="n":
                print("Goodbye!!")
                sys.exit()
    
startup()   