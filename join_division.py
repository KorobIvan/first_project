from random import randint


def division():
    """"""
    a = randint(1,20)
    b = randint(1,20)
    c = 0
    if a > b:
        d = b
        while b > 0:
            if a % b == 0 and d % b == 0:
                c = b
            else:
                b -= 1
    else:
        d = a
        while a > 0:
            if b % a == 0 and d % a == 0:
                c = a
            else:
                a -= 1   
    return (a, b, c)
print(division())

def division_result():
    pass
if __name__ == '__main__':
    division_result()