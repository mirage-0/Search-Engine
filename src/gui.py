import timeit
import pathlib
import random

m = r'''
import pathlib
import random
nameList = ['.git', 'ASD', 'ASD', 'PROJ', 'Tkinter Examples', 'WP22045397', '__pycache__', '__pycache__',
            '__pycache__', 'asd', 'asd-project', 'data', 'data', 'heads', 'heads', 'hooks', 'info', 'info',
            'logs', 'objects', 'pack', 'refs', 'refs', 'remotes', 'remotes', 'src', 'src', 'tags', 'xbox']

beta1 = ['a', 'b', 'c', 'd',
         'A', 'B', 'C', 'D',  '0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9', '.', '_', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')',
         '-', '_', '+', '=', ']', '}', '{', '[', '!', '`', '~']
beta4 = ['e', 'f', 'g', 'h', 'i', 'j', 'E', 'F', 'G', 'H', 'I', 'J']

beta2 = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
beta3 = ['v', 'w', 'x',
         'y', 'z', 'V',
         'W', 'X', 'Y', 'Z']
betaNext = []
beta = [beta3, beta2, beta4, beta1]

testDict = {}
nameList = []


def func(a):
    try:
        if a.is_dir():
            nameList.append(a)
            for x in a.iterdir():
                func(x)
    except PermissionError as e:
        pass


x = pathlib.Path(r'C:\Users\rajka\Desktop\uwe\ASD\Group_project\PROJ')

func(x)


def addToDict(score, j):
    x = True
    while x:
        counter = 0
        if score not in testDict:
            testDict[score] = j
            x = False
        else:
            while score+counter in testDict:
                counter += 1
            testDict[score+counter] = j
            x = False
    x = True


def calcScore(value, z, name):
    try:
        beta[value].index(z[0])
        score = 0
        score += int((value+10))*1000
        score += int((len(z)/7))*1000
        addToDict(score, name)

    except ValueError:
        pass


for z in nameList:
    for i in range(4):
        calcScore(i, z.stem, z)

flag = True

temp = 0
lis = []



def score(z):
    for i in range(4):
        try:
            beta[i].index(z[0])
            score = 0
            score += int((i+10))*1000
            score += int((len(z)/7))*1000
            return score
        except (ValueError, IndexError):
            pass


def searchFunction(search):
    z = 0
    j = True
    while j:
        try:
            a = testDict[score(search)+z]
            if a.stem == search:
                print(a)
                j = False
            else:
                z += 1
        except KeyError:
            pass
            
s = nameList[random.randint(0, len(nameList)-1)]
searchFunction(s.stem)
'''
mysetup = 'print("hi")'


# def run():
#     s = nameList[random.randint(0, len(nameList)-1)]
#     searchFunction(s.stem)


print(timeit.timeit(setup=mysetup, stmt=m, number=100))
