#functions can mutate objects given as an arguments, to a global level
'''
I had some slight confusion, but just cleared it up, So the object container must be passed as a functional argument 
to mutate the contained global objects within the container (dict or list for example). 
You can't pass the contained objects themselves as arguments and expect to globally mutate them.
'''
d = {'Num': 10}

def mutate(container):
    container['Num'] -= 1
    return container

mutate(d)

print(d['Num']) #passing the container dict as an argument
#functions can mutate objects given as an arguments, to a global level (given you pass the containers)