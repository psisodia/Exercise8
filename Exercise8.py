#!/usr/bin/env python

from sys import argv
import re
script, filename = argv




def make_chains(my_file):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    f = open(my_file)
    filetext = f.read().replace('\n', " ")
    filetext = re.sub('[,?)(]', "", filetext)
            
    f.close()
    
    words = filetext.split(' ')

    bigrams_dict = {}

    i=0

    for i in range(len(words)-2):
        key = (words[i], words [i+1])
        value = words[i+2]
        if key in bigrams_dict:
            bigrams_dict[key] = bigrams_dict.setdefault(key, [value]) + [value]

        else: 
            bigrams_dict[key] = [value]

        i += 1

    print bigrams_dict

    return bigrams_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    

    # Change this to read input_text from a file
    #input_text = "Some text"

    make_chains(filename)
    #random_text = make_text(chain_dict)
    #print my_text

if __name__ == "__main__":
    main()