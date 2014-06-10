#!/usr/bin/env python

from sys import argv
import re
import random
script, filename = argv




def make_chains(my_file):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    f = open(my_file)
    filetext = f.read().replace('\n', " ")
    filetext = re.sub('[,)(]', "", filetext)
            
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

    #print bigrams_dict

    return bigrams_dict

def make_text(bigrams_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    key = random.choice(bigrams_dict.keys())
    #print key
    i = 0
    random_text_list = [key[0], key[1]]
    #print random_text_list

    for i in range(0,10):
        new_word = random.choice(bigrams_dict[key])
        #print new_word
        random_text_list.append(new_word)
        #print random_text_list
        key = (key[1], new_word) 
        print key
        i+= 1

    return random_text_list

def print_list_as_string(random_text_list):
    space = ' '
    print space.join(random_text_list)

 

def main():
    

    # Change this to read input_text from a file
    #input_text = "Some text"

    print_list_as_string(make_text(make_chains(filename)))



    #random_text = make_text(chain_dict)
    #print my_text

if __name__ == "__main__":
    main()