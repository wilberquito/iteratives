n = input('Enter seed: ')
n = int(n)

if n <= 0:
    print('wtf')
    exit()
    
def digit_sum(n):
    count = 0

    while(n > 9):
        add = n % 10
        n = n // 10
        count = count + add

    return count + (n % 10)
    
def generator(n):

    def _generator(n, history):
        history.append(n)
        if (n != 1 and digit_sum(n) % 7 != 0):
            if (n % 2 == 0): # is even
                nxt = n / 2
            else:
                nxt = n * 3 + 1
            _generator(nxt, history)
        
        return history
    
    return _generator(n, [])

xs = generator(n)

for x in xs:
    print(x, end=' ')

ms1 = 'LA SUMA DE DÍGITS DE {m} ÉS {n}, I {n} ÉS MÚLTIPLE DE {x}'
ms2 = 'NOMBRE DE TERMES = {n}'
ms3 = 'SUMA DELS TERMES = {n}'

latest = xs[-1]

if digit_sum(latest) % 7 == 0:
    print(ms1.format(m = latest, n = digit_sum(7), x = 7))

print(ms2.format(n = len(xs)))
print(ms3.format(n = sum(xs)))