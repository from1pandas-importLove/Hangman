import random
import string

print('H A N G M A N')
while True:

    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == 'play':
        result = list(string.ascii_lowercase)
        words = ['python', 'java', 'kotlin', 'javascript']
        select = random.choice(words)
        hiden = '-' * len(select)
        limit = 0
        typed = []


        while True:
            print()
            print(hiden)
            letter = input('Input a letter: ')
            if len(letter) > 1:
                print('You should input a single letter')
                continue
            typed.append(letter)
            if len(typed) > len(set(typed)):
                print('You already typed this letter')
                typed = typed[:-1]
                continue
            if letter not in result:
                print('It is not an ASCII lowercase letter')
                continue
            elif letter in select:
                ind = [i for i, l in enumerate(list(select)) if l == letter]
                for i in ind:
                    temp = list(hiden)
                    temp[i] = letter
                    hiden = "".join(temp)
            elif letter not in select:
                print('No such letter in the word')
                limit += 1
            if '-' not in hiden:
                print()
                print(hiden)
                print('You guessed the word!')
                print('You survived!')
                break
            if limit == 8:
                print('You are hanged!')
                break
    elif choice == 'exit':
        break
