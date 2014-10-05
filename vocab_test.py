import os
import sys
import random
import getpass

MAIN_DIRECTORY= os.path.join(os.path.expanduser("~"), "wordlist")

def main(argv):
    if (len(sys.argv) != 1 and len(sys.argv) != 2) or sys.argv[1] == '--help':
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

    print "\n     ------------------------------"
    print "     Choosen file: ", wordlist
    print "     Press enter to display meaning"
    print "     ------------------------------\n"

    # fetch words from wordlist
    filepath = os.path.join(MAIN_DIRECTORY, wordlist)
    f = open(filepath, 'r')
    for line in f:
        word, meaning = line.split(",")
        word = word.strip(" ")
        meaning = meaning.strip(" ")
        print "Word: ",  word,

        disp = raw_input()
        print "Meaning: ", meaning
        print "------------------------------------"

if __name__=='__main__':
    main(sys.argv)
