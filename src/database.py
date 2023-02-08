import time
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
                # print('--', x, '--')
                # list.append(x.stem)
                # write(x, 0)
                func(x)
    except PermissionError as e:
        pass


searchCount = 200
x = pathlib.Path(r'C:\Users').parent
print('Path- ', x)
print('search Count -', searchCount)
buildStart = time.time()

func(x)
print(len(nameList), ' files in database', time.time())


def addToDict(score, j):
    # TODO: Check if key exists in dictionary
    x = True
    while x:
        counter = 0
        # print(j.name, 'x')
        if score not in testDict:
            testDict[score] = j
            x = False
            # print(j.name, 'y')
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
        if z.stem:
            calcScore(i, z.stem, z)
        else:
            calcScore(i, str(z), z)

buildFinish = time.time()
print('build diff - ', buildFinish-buildStart)
print('Beginning search...', time.time())
flag = True

temp = 0
lis = []
# for j in testDict.keys():
#     # print((int(j/100) not in lis), lis,  '!!!!!!')
#     if int(j/100) not in lis:
#         lis.append(int(j/100))
#         x = 0
#         # print(j, '----')
#         while flag:
#             try:
#                 print(testDict[j + x], j+x)
#                 x = x+1
#             except KeyError:
#                 flag = False

#         flag = True
#     else:
#         pass

# temp = j/1000
# print(len(testDict), len(nameList))
# print(testDict.keys())


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
                # print(testDict[score(search)+z])
                # print(a)
                j = False
            else:
                z += 1
        except KeyError:
            pass


flag2 = True
avgTime = []
startTime = time.time()
# print(time.time(), 'START -------------------####################')
for n in range(100):
    sTime = time.time()
    for l in range(searchCount):
        s = nameList[random.randint(0, len(nameList)-1)]
        # print(s)
        if s.stem:
            searchFunction(s.stem)
        else:
            searchFunction(str(s))
    fTime = time.time()
    avgTime.append(fTime-sTime)


# if i == '':
#     flag2 = False
finishTime = time.time()
print('Search Start - ', startTime)
print('Search Finish -', finishTime)
print('Search Time taken - ', finishTime-startTime)
print('buildStart - ', buildStart)
print('buildFinish- ', buildFinish)
print('build diff - ', buildFinish-buildStart)
print(sum(avgTime)/len(avgTime))


# searchFunction()
