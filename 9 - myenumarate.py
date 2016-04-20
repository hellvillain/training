kulema = [1, 554, 12]

def my_enumerate(list):
    tricky_kulema = {}
    count = 0
    for every in list:
        tricky_kulema[count] = every
        count = count + 1
    return tricky_kulema

print my_enumerate(kulema)
