from random import choices
import random, yaml
#config
def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
f = read_yaml("config.yaml")

test = f["CONFIG"]["test"] # If test is true, it will display the answer first, useful for testing. Default False
max_tries = f["CONFIG"]["max_tries"] # Number of maximum tries. Default
infinite_mode = f["CONFIG"]["infinite_mode"] #Allows you to guess indefinitely. Good for learning, but where's the fun? Default False
digits = f["CONFIG"]["digits"] # Number of digits the answer will have. Default 4
character_set = f["CONFIG"]["character_set"] # The characters that will constitute the answer. Default "123456"
allow_dupes = f["CONFIG"]["allow_dupes"] # Allows you to have duplicates of characters. Default True

def getNum(a,b,dupes): #Gives me the random number
    if dupes == True:
        return (random.choices(str(a), k=int(b)))
    else:
        temp = (random.choices(str(a), k=int(b)))
        while (len(temp) != len(set(temp))):
            temp = (random.choices(str(a), k=int(b)))
            continue
        else:
            return temp


def help(): #Defining the switcher
    print(info)
def undo():
    global tries
    if (infinite_mode):
        pass
    elif tries == 0:
        print('Nope.')
    else: tries -= 1; print("Like nothing happened.")
def solve():
    print("\x1b[31mYou lost!\x1b[0m \nThe right answer was:", "".join(answer_list))
    exit()
def default():
    print("Input provided is not a", digits, "digit number. If you need help type: \x1b[33m'help'\x1b[0m")
switcher = {"help": help, "undo": undo, "solve": solve, "default": default}

def switch(a):
    return switcher.get(a, default)()

greeting = "Welcome to Guess! If this is your first time, type 'help' to learn how to play. If you already know what's goin on just... "
info ="""Welcome to Guess! This a short game coded in Python.
The goal is to guess a random generated 4 digits number, with numbers from 1 to 6, in less than 10 turns. (these parameters can be customized in the config file)
Each guess gets a reply consisting of:
* \x1b[32mGreen X\x1b[0m for \x1b[33mcorrect numbers\x1b[0m in the \x1b[33mcorrect places.\x1b[0m
* \x1b[34mBlue X\x1b[0m for \x1b[33mcorrect numbers\x1b[0m in the \x1b[36mwrong places.\x1b[0m
* White X corresponding to \x1b[36mwrong numbers.\x1b[0m
To play you must simply type a 4 digits answer, with numbers from 1 to 6 (including).

Example: The correct answer is 1233, typing 4564 will reply XXXX, as no correct number is present.
Whereas 3156 will reply \x1b[34mXX\x1b[0mXX, as the 3 and 1 are present in the answer, but they aren't in the correct position.
Lastly, 3431 will reply \x1b[32mXX\x1b[0m\x1b[34mX\x1b[0mX as just a 3 is in the correct position.
Please note that the order of the reply will NOT vary depending on position, as it will always be \x1b[32mGreen\x1b[0m, then \x1b[34mBlue\x1b[0m, then White.


If you decide to give up or you can't wait to see the answer, you can simply type: 'solve'.
Lastly, if you want to spice up things, heads up to the config file, where you can customize a little bit the parameters.
"""
if allow_dupes == False and digits > len(character_set):
    print("Error, it's impossible to create a non-duplicate "+ str(digits)+" digit answer with the current character set. Please check the config.")
    exit()
answer_list= getNum(character_set, int(digits), allow_dupes) # gets the random answer sets first the avaliable characters, and then the number of characters.
win = False
tries = 0
inp_txt = "\x1b[33mGuess the numbers: \x1b[0m"
if test == True:
    print("".join(answer_list))
print(greeting)
while (tries < max_tries and not win):
    inp = input(inp_txt)
    inp_list =list(inp)
    if (not inp.isdigit()) or len(inp) !=4:
        switch(inp)
    else:
        compAns,  compInp  = "".join(answer_list) , "".join(inp_list) # create two temporary variables to compare the input and answer.
        compAns2, compInp2 = compAns, compInp
        if answer_list == inp_list:
            print ("\x1b[32mCongratulations! You win!\x1b[0m")
            win = True
        else:
            grex, blux = 0, 0,
            for i, x in enumerate(answer_list): #sets GREEN X with correct numbers in correct places
                if inp_list[i] == x:
                    grex +=1
                    compAns2, compInp2 = compAns2.replace(compAns[i],"",1), compInp2.replace(compAns[i],"",1)
            for i, x in enumerate(compAns2): #sets BLUE X, with correct numbers in wrong places
                if compInp2[i] in compAns2:
                    blux +=1
                    compAns2 = compAns2.replace(compInp2[i],"",1)
            fill = 4 - (int(grex)+ int(blux))
            if (infinite_mode):
                print("\x1b[32mX\x1b[0m" * grex + "\x1b[34mX\x1b[0m" * blux + "X" * fill)
            else:
                print("\x1b[32mX\x1b[0m" * grex + "\x1b[34mX\x1b[0m" * blux + "X" * fill + f". {max_tries -1 -tries}", "try" if tries == max_tries-2 else "tries", " left.")
                tries +=1

            if tries == max_tries:
                solve()
