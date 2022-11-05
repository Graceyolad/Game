#!/usr/bin/env python
# coding: utf-8

# In[1]:



    print("""Welcome to the game! You are on an intergalactic search for a new human livable planet. 
    For your first route, the scientists in your team have suggested two options. 
    You can either visit the galaxy 'Scary Sunset', which is big and might have a better chance 
    to have at least one planet for humans or you can decide to go to the smaller galaxy 'Greedy Velvet'
    which has less planets in it. The scientists are however more optimistic to find a human livable planet there.""")
    choice = input("""Choose your adventure! Where do you want to go?
                   (a) The big Galaxy 'Scary Sunset' 
                   (b) The smaller Galaxy 'Greedy Velvet' """)
    if choice == 'a':
        print("""You are in Scary Sunset now! You found two planets that might be livable for human beings.
        On one side there is 'Red Olive' that smells strangely. On the other side, there is 'Blue Lemon' that
        has a very strange shape for a planet. 
        Choose your next destination.""")
        choice = input("""Which Planet would you like to go?
                       (c) Red Olive 
                       (d) Blue Lemon?""")
        if choice == 'c':
            print('Red Olive is not a planet, you lost!')
        elif choice == 'd':
            print('Blue Lemon is a planet, but not human livable. Kudos on the scientific discovery!')
    elif choice == 'b':
        print("""Welcome to Greedy Velvet! The scientists have a good feeling about this planet. You discover 
        two planets; 'Yellow Cherry' and 'Green Peach'. Yellow Cherry is very small, but looks promising. Green peach looks
        very eatable but not very livable.
        Choose your next destination.""")
        choice = input('Planet e-Yellow Cherry or f- Green Peach?')
        if choice == 'e':
            print('Congratulations! Yellow Cherry is indeed livable for humans.')
        elif choice == 'f':
            print('You were close but you unfortunately lost. Green Peach is not a planet!')
       

