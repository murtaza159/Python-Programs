letter_point = {'a':1, 'b':2, 'c':3, 'd':4, 'e':1, 'f':2, 'g':5, 'h':6, 'i':3, 'j':4, 'k':2, 'l':3, 'm':2, 'n':3, 'o':1, 'p':3, 'q':5,
'r':6, 's':3, 't':4, 'u':3, 'v':6, 'w':5, 'x':4, 'y':3, 'z':9}

def scrabble_points(word):
    tot_points=0
    for letter in word.lower():
        tot_points+=letter_point[letter]
    return tot_points

Word1=input("Enter word: ")

print("Score =",scrabble_points(Word1))