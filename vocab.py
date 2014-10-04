import sys, os, time


def main(argv):
    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print "Usage: python vocab.py --option"
        print "Option: -a or --add to add a word (default if no args given)"
        print "Option: -d or --disp to display words"
        sys.exit(10)
    if len(sys.argv) == 1 or sys.argv[1] == '-a' or sys.argv[1] == '--add':
        word, meaning = get_word()
        add_word(word, meaning)
    elif sys.argv[1] == '-d' or sys.argv[1] == '--disp':
        display_words()

def get_word():
    print "Enter the word",
    word = raw_input()
    #print word
    print "enter the meaning",
    meaning = raw_input()
    #print meaning
    return word, meaning


def add_word(word, meaning):
    main_directory = os.path.join(os.path.expanduser("~"),  "wordlist")
    print main_directory

    if os.path.exists(main_directory):
        filename = os.path.join(main_directory, file_to_store())
        print filename
        f = open(filename, 'a')
        #f = open(main_directory + "/" + file_to_store(), 'a')
        f.write(word + ', ' + meaning + '\n')
        f.close()

def display_words():
    print "Enter date(mmddyy): ",
    date = raw_input()
    filename = 'wl' + date
    filepath = os.path.expanduser("~") + "/wordlist/" + filename
    if not os.path.exists(filepath):
        print "sorry file not found!"
        exit()

    # display the contents of the file
    f = open(filepath, 'r')
    for line in f:
        line.rstrip('\n')
        word, meaning = line.split(',')
        print word + ": " + meaning,


def file_to_store():
    # save maintaing unique file for each day
    # check if the directory exist
    main_directory = os.path.expanduser("~") + "/wordlist"
    if not os.path.isdir(main_directory):
        os.makedirs(main_directory)
    # grant a unique file name for current date
    filename = "wl" + time.strftime("%m%d%y")
    return filename


if __name__ == '__main__':
    main(sys.argv)

