import pathlib


def write(a):
    try:
        with open('readme.txt', 'w') as f:
            f.write('\n'.join(str(a)))
            print(str(a))
    except UnicodeEncodeError as e:
        pass


def func(a):
    try:
        for x in a.iterdir():
            # print('--', x, '--')
            write(x)
            func(x)
    except NotADirectoryError as e:
        pass


p = pathlib.Path(__file__)
print('x')
x = p.parents[len(p.parents)-4]
for a in x.iterdir():
    # print(a)
    write(a)
    func(a)
print('x')
