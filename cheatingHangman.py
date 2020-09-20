# -*- coding: utf-8 -*-
import sys

file = open("polyTest.txt", "r")
guessAmt = 0
myWord = []
#create list of used letters to track
letters = []
table = [] 
def startup():
#get word length
    wordLen = input("enter word length: ")
    wordLen = int(wordLen)
    while wordLen < 1:
        wordLen = input("enter word length: ")
        wordLen = int(wordLen)
     
#create list to track current word (starts all -)
    for i in range (wordLen):
        myWord.append('-')
    
#get number of guesses
    guessAmt = input("enter amount of guesses: ")
    guessAmt = int(guessAmt)
    while guessAmt < 1:
         guessAmt = input("enter amount of guesses: ")
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
        #print(value[1])
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
    #Get first instance of the letter, only works when first instance is 0
    if(value[0] == 0):
        myWord.insert(value[0], let)
        myWord.pop(value[0]+1)
        myWord.insert(value[1],let)
        myWord.pop(value[1]+1)
    else:
        myWord.insert(value[0]+1,let)
        myWord.pop(value[1]+2)
        myWord.insert(value[1]+1,let)
        myWord.pop(value[1]+2)

    #Get second index of the letter, only works when first instance is 0
    #print(value[0])  

    #NEED TO CHANGE WHAT MY WORD IS
    return twoFinFam



#    rows, cols = (len(theFam), 2)
#    arr = [[0 for i in range (cols)]for j in range (rows)]
#    count = 0
#    for word in theFam:
#        arr[count][0] = str(word.index('let'))
#        arr[count][2] = word
#        ind = 0
#        for letter in word:
#            if letter is let:
#                if arr[count][0] is not ind:
#                    arr[count][1] = str(ind)
#            ind += 1
            
def PolyWordFam(let, theFam):
    polyFam = {}
    for thing in theFam:
        first = thing.index(let)
        ind = 0
        for letter in thing:
            if letter is let:
                if ind is not first:
                    #adds the number of indices n times to the previous lsit of values. Creates a dict_values object sadly, not ints nor a list
                    polyFam[thing] = (polyFam.values(),ind)
            ind +=1
      #identifies which indices are the most common
    freq = {}
    for key,value in polyFam.items():
        #print(value[1])
        if value not in freq:
            freq[value]=0
        else:
            freq[value]+=1
    popInd = (max(freq,key=freq.get))
    #creates list of all the words with the matching most common index
    polyFinFam = []  
    for key,value in polyFam.items():
        if value is popInd:
            polyFinFam.append(key)   
    
    #Attempts to insert each letter at each index in value. Need the right object type for i however.
    for i in value:
        myWord.insert(i,let)
        myWord.pop(i+1)
    return polyFinFam

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
    print(words)
    guess = 0
    print(guessAmt)
    while len(words) > 1 and guessAmt > guess or '-' in myWord: 
        letter = input("choose a letter: ")
        while not(len(letter) == 1 and letter not in letters):
            letter = input("choose a letter: ")
        letters.append(letter)
        nxtList = wordFamily(letter, words)
        words = nxtList
        print(words)
        if remain == 'y':
            print (len(words))
        print(myWord)
        guess = guess + 1
        print(guess)
        if myWord==(words[0]):
            print("You guessed the word! You won!!")
            again = input("Do you want to play again? ")
            while not(again =='y' or again == 'n'):
                again = input("Do you want to play again? (y/n) ")
            if again == "y":
                letters.clear()
                table.clear()
                myWord.clear()
                startup()
            if again =="n":
                print("Goodbye!!")
                sys.exit()
        elif guess == guessAmt:
            print("You lost! Better luck next time!")
            again = input("Do you want to play again? ")
            while not(again =='y' or again == 'n'):
                again = input("Do you want to play again? (y/n) ")
            if again == "y":
                letters.clear()
                table.clear()
                myWord.clear()
                startup()
            if again =="n":
                print("Goodbye!!")
                sys.exit()
    print("exiting while loop")
    
startup()   


#1. debug twoWordFam ~ kinda, so so close
#2. threeWordFam ~ Poly needs work
#3. play again - works, but had to add sys.exit() to make not play again to exit proeprly


