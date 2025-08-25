a = 10
b = 11
c = 12
d = 13
e = 14
f = 15

def bitCharacterToBinary(arr):
    for x in arr:
        value = 0
        if x == 'a':
            value = a
        if x == 'b':
            value = b
        if x == 'c':
            value = c
        if x == 'd':
            value = d
        if x == 'e':
            value = e
        if x == 'f':
            value = f
        if x.isnumeric():
            value = int(x)
            
        for y in [8, 4, 2, 1]:
            if value - y < 0:
                print('0', end='')
            else:
                print('1', end='')
                value -= y
        
        print(' ', end='')

def bitCharacterToTotalNum(arr):
    print('')
    value = 0
    for x in arr:
        if x == 'a':
            value += a
        if x == 'b':
            value += b
        if x == 'c':
            value += c
        if x == 'd':
            value += d
        if x == 'e':
            value += e
        if x == 'f':
            value += f
        if x.isnumeric():
            value += int(x)
    print(value)
        
arr = '01ff'
bitCharacterToBinary(arr)
bitCharacterToTotalNum(arr)
