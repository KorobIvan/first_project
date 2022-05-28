from random import randint


def prime_number():
    line = sorted(set([randint(1, 10) for i in range(10)]))
    #print(line)
    z = ''
    for i in line:
        j = 0
        #print(i)
        for a in range(10):
            #print(a)
            if i % (int(a) + 1) == 0:
                j += 1
                #print(j)
        if j <= 2:
            z += f'{str(i)}, '
    return (line, z[:-2])
print(prime_number())