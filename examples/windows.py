import pathlib
import stat
import os
import string


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


list = []

y = []


def func(a):
    try:
        if a.is_dir():
            list.append(a.stem)
            for x in a.iterdir():
                print('--', x, '--')
                # list.append(x.stem)
                # write(x, 0)
                func(x)
    except PermissionError as e:
        pass
        # print(e)


x = pathlib.Path(r'C:\Users\rajka\Desktop\uwe\ASD\Group_project\PROJ')
# C:\Users\rajka\AppData\Roaming\Microsoft\Windows\Recent
# print('x')
# func(x)
# x = p.parents[len(p.parents)-6]
# if x.is_dir():
#     for a in x.iterdir():
#         # print(a, 0)
#         # write(a, 1)
#         # gets file name no extension
#         # print(a.stem)
#         # # gets only exension
#         # print(a.suffix)
#         # print(a.as_posix())
#         # print(a.stat())
#         if a.is_dir:
#             func(a)
print('x')

for i in list.copy():
    if len(i) < 3:
        list.remove(i)
# print(list2)
list.sort()
# print(list)
lenlist = []
for j in list:
    lenlist.append(len(j))
lenlist.sort()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9']
alphanum = []
for k in list:
    for l in alpha:
        alphanum.append((l, k.count(l)))
# print(lenlist, alphanum)
# print(list.index('xbox'))
# print(pathlib.Path(r'C:\Users\rajka\Desktop\uwe\ASD\Group_project\PROJ\asd\src').is_relative_to(
    # pathlib.Path(r'C:\Users\rajka\Desktop\uwe\ASD\Group_project\PROJ\asd')))

# output of all directories in a list
nameList = ['.git', 'ASD', 'ASD', 'PROJ', 'Tkinter Examples', 'WP22045397', '__pycache__', '__pycache__',
            '__pycache__', 'asd', 'asd-project', 'data', 'data', 'heads', 'heads', 'hooks', 'info', 'info',
            'logs', 'objects', 'pack', 'refs', 'refs', 'remotes', 'remotes', 'src', 'src', 'tags', 'xbox']
[3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 5, 5, 5, 7, 7, 7, 10, 11, 11, 11, 11, 16]
# for i in y:
#     print(i.is_relative_to(list[5]))


class File:
    def __init__(self, name):
        self.name = name
        self.score = 0


beta1 = ['a', 'b', 'c', 'd',
         'A', 'B', 'C', 'D',  '0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9', '.', '_', '/']
beta4 = ['e', 'f', 'g', 'h', 'i', 'j', 'E', 'F', 'G', 'H', 'I', 'J']

beta2 = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
beta3 = ['v', 'w', 'x',
         'y', 'z', 'V',
         'W', 'X', 'Y', 'Z']
betaNext = []
beta = [beta3, beta2, beta4, beta1]

fileList = []
for m in nameList:
    fileList.append(File(m))


def calcScore(value, z):
    try:
        beta[value].index(z.name[0])
        z.score += int((value+10))*1000
    except ValueError:
        pass


def calcScore2(value, z):
    z.score += int((len(z.name)/7))*1000


for z in fileList:
    # z.score += len(z.name)/7
    for i in range(4):
        calcScore(i, z)
        calcScore2(i, z)


scoreList = []

# print(len(fileList))


def sort():
    for z in range(len(fileList)-1):
        for x in range(len(fileList)-1):

            if (fileList[x].score < fileList[x+1].score) and ((x+1) <= len(fileList)):
                # print('1 - ', fileList[x].name,
                #   '2 - ', fileList[x+1].name)
                y = fileList[x]
                # print(y)
                fileList[x] = fileList[x+1]
                fileList[x+1] = y

                # print('1 - ', fileList[x].name,
                #       '2 - ', fileList[x+1].name)
        z += 1

        # print(x+1)


# for k in fileList:
#     print('++', int(k.score))


def objToList(list):
    temp = []
    for x in list:
        temp.append(x.score)

    temp.sort()
    # print('++++++', temp)
    for z in range(len(list)):
        for m in range(len(list)):
            if temp[z] == list[m].score:
                # print('$', list[m].score, z, m)

                t = list[m]
                list[z] = list[m]

                list[m] = t
                # print('#', list[m].score, t.score)

    # for k in list:
    #     print('--', k.score)
    #     print('------------')
    # print(list)
    return temp


# scoreList = objToList(fileList)
# scoreList.sort()
testDict = {}


def addToDict(file):
    for j in fileList:
        # TODO: Check if key exists in dictionary

        while x:
            counter = 0
            # print(j.name, 'x')
            if j.score not in testDict:
                testDict[j.score] = j
                x = False
                # print(j.name, 'y')
            else:
                while j.score+counter in testDict:
                    counter += 1
                testDict[j.score+counter] = j
                x = False
        x = True


    # print((fileList[j].score), fileList[j].name)
print(testDict.keys(), testDict.values())

flag = True
x = 0
while flag:
    try:
        print(testDict[13000 + x].name, 13000+x)
    except KeyError:
        flag = False
    x = x+1


# sort()
# for mn in fileList:
# if 0 < mn.score <= 1:
# print(mn.name, '-', mn.score)
# elif 1 < mn.score <= 1.6:
# print(mn.name, '-', mn.score)
# elif 1.6 < mn.score:
# print(mn.name, '-', mn.score)
# scoreList.append(mn.score)


# TODO : Quickly seperate floats to nearest int value in ascending order.
