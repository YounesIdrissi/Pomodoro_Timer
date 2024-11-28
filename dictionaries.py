dictionary = {'A': 1, 'B': 2, 'C': 3}

'''
Understanding for loops:
for loops can take one iterable, however, using zip() can allow for as many iterables
as needed. from itertools import zip_longest can help us iterate uneven list quantities,
without losing any data.
'''
#prints key, value pairs in tuple
for n in dictionary.items():
    print(n)

#enumerate extracts the index from each tuple; gives index position of each (key, value) pair
for n in enumerate(dictionary.items()):
    print(n)

#using enumerate AND .items() to get (key, value) pairs AND index, all separate
for index, (key, value) in enumerate(dictionary.items()):
    print(f"index: {index}, key: {key}, value: {value}")