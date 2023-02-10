import time
import pathlib
import random


nameList = ['.git', 'ASD', 'ASD', 'PROJ', 'Tkinter Examples', 'WP22045397', '__pycache__', '__pycache__',
            '__pycache__', 'asd', 'asd-project', 'data', 'data', 'heads', 'heads', 'hooks', 'info', 'info',
            'logs', 'objects', 'pack', 'refs', 'refs', 'remotes', 'remotes', 'src', 'src', 'tags', 'xbox']

# beta1 = ['a', 'b', 'c', 'd',
#          'A', 'B', 'C', 'D',  '0', '1', '2', '3', '4', '5', '6', '7',
#          '8', '9', '.', '_', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#          '-', '_', '+', '=', ']', '}', '{', '[', '!', '`', '~']
# beta4 = ['e', 'f', 'g', 'h', 'i', 'j', 'E', 'F', 'G', 'H', 'I', 'J']

# beta2 = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#          'u', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
# beta3 = ['v', 'w', 'x',
#          'y', 'z', 'V',
#          'W', 'X', 'Y', 'Z']
# flag = True

# temp = 0
# lis = []
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
beta1 = ['0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9', '.', '_', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')',
         '-', '_', '+', '=', ']', '}', '{', '[', '!', '`', '~', 'a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x',
         'y', 'z']
betaNext = []
# beta = [beta3, beta2, beta4, beta1]

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
        else:
            nameList.append(a)
    except PermissionError as e:
        pass


searchCount = 1
numTest = 1
x = pathlib.Path(r'C:\Users\rajka\Desktop\uwe').parent
print('Path- ', x)
print('search Count -', searchCount)
buildStart = time.time()

func(x)
print(len(nameList), ' files loaded in database, sorting...')


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


def calcScore(z, name):
    try:
        l = beta1.index(z.lower()[0])
        score = 0
        score += int((l+10))*1000
        score += int((len(z)/10))*10
        addToDict(score, name)

    except ValueError:
        pass


for z in nameList:
    # for i in range(1):
    if z.stem:
        calcScore(z.stem, z)
    else:
        calcScore(str(z), z)

buildFinish = time.time()
print('build diff - ', buildFinish-buildStart)
print('Beginning search...', time.time())


def score(z):
    # for i in range(4):
    score = 0
    try:
        l = beta1.index(z.lower()[0])
        score += int((l+10))*1000
        score += int((len(z))/10)*10
    except (ValueError, IndexError):
        score = 0
    return score


def searchFunction(search):
    z = 0
    j = True
    resultList = []
    while j:
        try:
            temp = score(search)
            a = testDict[temp+z]
            # print(temp, 'xxxx')
            # print(a, 'x')
            if str(a.stem).lower() == search.lower():
                # print(testDict[score(search)+z])
                # print(a)
                j = False
                return (str(a), resultList)
            elif temp in testDict:
                z += 1
                resultList.append(a)
            else:
                j = False
                return resultList
        except KeyError:
            j = False
    return (0, resultList)


flag2 = True
avgTime = []
startTime = time.time()
# print(time.time(), 'START -------------------####################')
# for n in range(numTest):
#     sTime = time.time()
#     for l in range(searchCount):
#         s = nameList[random.randint(0, len(nameList)-1)]
#         # print(s)
#         if s.stem:
#             searchFunction(s.stem)
#         else:
#             searchFunction(str(s))
#     fTime = time.time()
#     avgTime.append(fTime-sTime)


# if i == '':
#     flag2 = False
finishTime = time.time()
print('Time to build database - ', buildFinish-buildStart)
# print('Search Start - ', startTime)
# print('Search Finish -', finishTime)
# print('Time to finish search - ', finishTime-startTime)
# print('buildStart - ', buildStart)
# print('buildFinish- ', buildFinish)

# print('avg time for search - ', sum(avgTime)/len(avgTime))

# print('enter file name to search')

# for x in nameList:
#     print(x)
# print(userInput in nameList)


def abcd(z):
    for a in range(4):
        try:
            l = beta1.index(z.lower()[0])
            score = 0
            score += int((l+10))*1000
            score += int((len(z)/10))*10
            return score

        except ValueError:
            pass


mna = []
for l in testDict:
    mna.append(l)
    print(l, testDict[l].stem)
mna.sort()
for b in mna:
    print(b, testDict[b].stem, len(
        testDict[b].stem), abcd(testDict[b].stem))


def similarity(value, resultList):
    # TODO: calculate value based on input value then compare with
    #       results list and sort result list based on similarity score
    score = 0
    dict = []
    # for x in range()


while True:
    print('Enter file name -')

    userInput = input()
    print(score(userInput))
    result = searchFunction(userInput.lower())
    # print(result)
    closestList = []
    resultList = []
    if result[0] != 0:
        if userInput in str(result[0]):  # or userInput == str(result[0]):
            print('result - \n')
            print(result[0])
    elif result[0] == 0:
        # print('list of results -- \n')
        for a in result[1]:
            if userInput in str(a).lower():  # or userInput.lower() == str(a):
                closestList.append(a)
                # print('appended -------------', a)
            else:
                resultList.append(a)
        print('Similar files - \n')
        for j in closestList:
            print(str(j))
    else:
        print('No such file \n')
    # for j in result[1]:
    #     print(j)
    # print('Press ctrl + c to exit')

# searchFunction()
