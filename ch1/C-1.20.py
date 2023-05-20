#Python's random module includes a function shuffle(data) that accepts a list of 
# elements and randomly reorders the elements so that each possi- ble order occurs 
# with equal probability. The random module includes a more basic function randint(a, b) 
# that returns a uniformly random integer from a to b (including both endpoints). 
# Using only the randint function, implement your own version of the shuffle function.

from random import shuffle, randint

colours = ['orange', 'green', 'yellow', 'purple', 'red', 'blue', 'white']

#with shuffle method
shuffle(colours)
print(colours)


#with randint method
def shuffle_colours(data):
    shuffled_numbers = []
    shuffled = []
    size = len(data)
    while len(shuffled_numbers) < size:
        index = randint(0, size-1)
        if index in shuffled_numbers:
            continue
        shuffled_numbers.append(index)

    for num in shuffled_numbers:
        shuffled.append(data[num])
    return shuffled

result = shuffle_colours(colours)
print(result)


