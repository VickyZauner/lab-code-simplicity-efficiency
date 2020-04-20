

import random
# defining the sequence of characters
sequence = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

count = [] # a variable to count the desired number of strings
#asking for input
l = int(input('Enter minimum string length: '))
u = int(input('Enter maximum string length: '))
n = int(input('How many random strings to generate? '))
# a function creating random strings with random length within given borders
def ran_str():
    global l
    global u
    print("".join(random.sample(sequence, random.randint(l, u))))
    count.append(1) # counting the rounds

while sum(count) < n: # loop keeping string prooduction going while strings counted are less than desired number n
    ran_str() # start function
