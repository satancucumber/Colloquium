from random import randint

f = open('1307Litsevanova.txt', 'w')

a = list('qwertyuiopasdfghjklzxcvbnm_')
print(a)
n = randint(50, 100 + 1)

for i in range(n):
    sym = list(a)
    row = ''
    m = randint(20, 27)
    for j in range(m):
            b = randint(0, len(sym) - 1)
            print(b, len(sym), sym, j)
            l = sym[b]
            row += l
            sym.pop(sym.index(l))
    if '_' in sym:
        row += '_'
    if i != n - 1:
        f.write(row + '\n')
    else:
        f.write(row + '\n#')
