#!/usr/bin/env python2
#
# vocab_test.py - Quiz the user with the words stored
#
# Copyright (c) 2015 Harsimran Singh <me@harsimransingh.in>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

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
