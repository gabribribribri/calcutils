from elems import elems
from inlib import parse_input

def is_elem(s):
    return s[0].upper()+s[1:] in elems[s[0].upper()]

def word_to_elem(word, so_far):
    if len(word) == 0:
        print("<", so_far, sep="")
        return
    if is_elem(word[0]):
        word_to_elem(word[1:], so_far + " " + word[0].upper())
    if len(word) >= 2 and is_elem(word[0:2]):
        word_to_elem(word[2:], so_far + " " + word[0].upper() + word[1])


while True:
    word = parse_input("> ", {str.isalpha:"only letters."})
    if word is None:
        exit()
    word_to_elem(word, "")
