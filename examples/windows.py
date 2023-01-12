import pathlib
import stat
import os


def write(a, b):
    if b == 1:
        try:
            with open('readme.txt', 'a') as f:
                f.write('|' + '\n')
                # print(str(a))
                # print(str(a))
        except UnicodeEncodeError as e:
            pass
    else:
        try:
            with open('readme.txt', 'a') as f:
                f.write((str(a)) + '\n')
                # print(str(a))
                # print(str(a))
        except UnicodeEncodeError as e:
            pass


def func(a):
    try:
        if a.is_dir():
            print(a)
            for x in a.iterdir():
                print('--', x, '--')
                write(x, 0)
                func(x)
    except PermissionError as e:
        print(e)


p = pathlib.Path(__file__)
print('x')
x = p.parents[len(p.parents)-2]
if x.is_dir():
    for a in x.iterdir():
        # print(a)
        write(a, 1)
        func(a)
print('x')
