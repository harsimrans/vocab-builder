import os
import sys
import random
import getpass

MAIN_DIRECTORY= os.path.join(os.path.expanduser("~"), "wordlist")

def getinput(a):
    """hacked getpass for user input"""
    inp = getpass.getpass(a)
    return inp

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print "Usage: python vocab_test.py [mmddyy]"
        exit(10)
    if len(sys.argv) == 1:
        pick_random_wl()
    elif len(sys.argv) == 2:
        pick_random_wl(sys.argv[1])

def pick_random_wl(wordlist=None):

    # get list of all worlists
    if not wordlist:
        wordlists = os.listdir(MAIN_DIRECTORY)
        wordlist = random.choice(wordlists)
    else:
        wordlist = "wl" + wordlist

    print "\n-----xxxxx-------xxxxx------"
    print "Choosen file: ", wordlist
    print "Press (Y/y) to display meaning"
    print "-----xxxxx-------xxxxx------\n"

    # fetch words from wordlist
    filepath = os.path.join(MAIN_DIRECTORY, wordlist)
    f = open(filepath, 'r')
    for line in f:
        word, meaning = line.split(",")
        word = word.strip(" ")
        meaning = meaning.strip(" ")
        print "Word: ",  word,

        disp = getinput("")
        while disp != 'y' and disp != 'Y':
            disp = getinput("")
            continue;
        print "Meaning: ", meaning
        print "------------------------------------"



if __name__=='__main__':
    pick_random_wl()
