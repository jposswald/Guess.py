from random import choices
import random
#config
test = False # if test is true, it will display the answer first, useful for testing
max_tries = 10 #number of maximum tries.
digits = 4 # I recommend using 4.
charSet = "123456" #the characters that will constitute the answer. I recommend number 1 to 6.
tries = 0

def getNum(a,b): #Gives me the random number
    return (random.choices(str(a), k=int(b)))

def help(): #Defining the switcher
    print(info)
def undo():
    global tries
    tries -= 1
def solve():
    print("\x1b[31mYou lost!\x1b[0m \nThe right answer was:", "".join(ansList))
    exit()
def default():
    print("Input provided is not a 4 digit number. If you need help type: \x1b[33m'help'\x1b[0m")
switcher = {"help": help, "undo": undo, "solve": solve, "default": default}

def switch(a):
    return switcher.get(a, default)()

greeting = "Welcome to Guess! If this is your first time, type 'help' to learn how to play. If you already know what's goin on just... "
info ="""Welcome to Guess! This a short game coded in Python.
The goal is to guess a random generated 4 digits number, with numbers from 1 to 6, in less than 10 turns. (these parameters can be customized, tho)
Each guess gets a reply consisting of:
* \x1b[32mGreen X\x1b[0m for \x1b[33mcorrect numbers\x1b[0m in the \x1b[33mcorrect places.\x1b[0m
* \x1b[34mBlue X\x1b[0m for \x1b[33mcorrect numbers\x1b[0m in the \x1b[36mwrong places.\x1b[0m
* White X corresponding to \x1b[36mwrong numbers.\x1b[0m
To play you must simply type a 4 digits answer, with numbers from 1 to 6 (including).

Example: The correct answer is 1233, typing 4564 will reply XXXX, as no correct number is present.
Whereas 3156 will reply \x1b[34mXX\x1b[0mXX, as the 3 and 1 are present in the answer, but they aren't in the correct position.
Lastly, 3431 will reply \x1b[32mXX\x1b[0m\x1b[34mX\x1b[0mX as just a 3 is in the correct position.
Please note that the order of the reply will NOT vary depending on position, as it will always be \x1b[32mGreen\x1b[0m, then \x1b[34mBlue\x1b[0m, then White.


If you decide to give up or you can't wait to see the answer, you can simply type: 'solve'
"""
ansList= getNum(charSet, int(digits)) # gets the random answer sets first the avaliable characters, and then the number of characters.
win = False
inp_txt = "\x1b[33mGuess the numbers: \x1b[0m"
if test == True:
    print("".join(ansList))
print(greeting)
while (tries < max_tries and not win):
    inp = input(inp_txt)
    inpList =list(inp)
    if (not inp.isdigit()) or len(inp) !=4:
        switch(inp)
    else:
        compAns,  compInp  = "".join(ansList) , "".join(inpList) # create two temporary variables to compare the input and answer.
        compAns2, compInp2 = compAns, compInp
        if ansList == inpList:
            print ("\x1b[32mCongratulations! You win!\x1b[0m")
            win = True
        else:
            grex, blux = 0, 0,
            for i, x in enumerate(ansList): #sets GREEN X with correct numbers in correct places
                if inpList[i] == x:
                    grex +=1
                    compAns2, compInp2 = compAns2.replace(compAns[i],"",1), compInp2.replace(compAns[i],"",1)
            for i, x in enumerate(compAns2): #sets BLUE X, with correct numbers in wrong places
                if compInp2[i] in compAns2:
                    blux +=1
                    compAns2 = compAns2.replace(compInp2[i],"",1)
            fill = 4 - (int(grex)+ int(blux))
            print("\x1b[32mX\x1b[0m" * grex + "\x1b[34mX\x1b[0m" * blux + "X" * fill + f". {max_tries -1 -tries}", "try" if tries == max_tries-2 else "tries", " left.")
            tries +=1

            if tries == max_tries:
                solve()
