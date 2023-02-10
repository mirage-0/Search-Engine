import time
import pathlib
import random


# beta1 = ['0', '1', '2', '3', '4', '5', '6', '7',
#          '8', '9', '.', '_', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#          '-', '_', '+', '=', ']', '}', '{', '[', '!', '`', '~', 'a', 'b', 'c', 'd',
#          'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#          'u', 'v', 'w', 'x',
#          'y', 'z']
# betaNext = []
# testDict = {}
# nameList = []


class Tree:
    def __init__(self):
        # contains all files
        defaultCategories = ['music', 'movies', 'document', 'pictures']
        layer0 = {}
        # contains all file categories
        layer1 = {}
        # contains all category formats, are simple dictionaries
        layer2 = {}


class manager:

    def __init__(self):
        # character list
        self.beta1 = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '.', '_', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                      '-', '_', '+', '=', ']', '}', '{', '[', '!', '`', '~', 'a', 'b', 'c', 'd',
                      'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x',
                      'y', 'z']
        self.fileTree = Tree()
        self.dirTree = Tree()
        self.dirList = []
        self.fileList = []
        searchCount = 1
        numTest = 1
        # self.buildList()
        # look for files in this path

    def buildDict(self):
        for dirName in self.dirList:
            if dirName.stem:
                self.addToDict(self.calcScore(dirName.stem), dirName)
            else:  # z is a root disk ex: [C:\, D:\, E:\], thus .stem wont exist
                self.addToDict(self.calcScore(str(dirName)), dirName)

        for fileName in self.fileList:
            if fileName.stem:
                self.addToDict(self.calcScore(
                    fileName.stem, fileName), fileName)
            # will probably never run since filename stems will always exist
            else:
                self.addToDict(self.calcScore(str(fileName), fileName))

    def buildList(self, a):
        try:
            if a.is_dir():
                # all directories are appended to nameList
                self.dirList.append(a)
                for x in a.iterdir():
                    self.buildList(x)
            else:
                # all files are appended to fileList
                self.fileList.append(a)
        except PermissionError as e:
            pass

    def addToDict(self, score, file):
        # TODO: Select correct dictionary, if doesnt exist create it, add to specific dictionary
        x = True

        while x:
            counter = 0
            if score not in self.fileList:
                self.fileList[score] = file
                x = False
            else:
                while score+counter in self.fileList:
                    counter += 1
                self.fileList[score+counter] = file
                x = False
        x = True

    def calcScore(self, fileName):
        try:
            l = self.beta1.index(fileName.lower()[0])
            score = 0
            score += int((l+10))*1000
            score += int((len(fileName)/10))*10
            return (score)

        except ValueError:
            return 0

    # def score(self, z):
    #     score = 0
    #     try:
    #         l = self.beta1.index(z.lower()[0])
    #         score += int((l+10))*1000
    #         score += int((len(z))/10)*10
    #     except (ValueError, IndexError):
    #         score = 0
    #     return score

    def searchFunction(self, search):
        z = 0
        j = True
        resultList = []
        # TODO: search through the correct dict, if cant find initially, start searching through all dicts
        # current implementation will be sequential, future will be parallel, multi core
        while j:
            try:
                groupScore = self.calcScore(search)
                a = self.testDict[groupScore+z]
                if a.stem.lower() == search:
                    j = False
                    return (a.name, resultList)
                elif groupScore in self.testDict:
                    z += 1
                    resultList.append(a)
                # else:
                #     j = False
                    # return (0, resultList)
            except KeyError:
                j = False
        return (0, resultList)

    def similarity(self, value, resultList):
        # TODO: calculate value based on input value then compare with
        #       results list and sort result list based on similarity score
        score = 0
        dict = []
    # for x in range()

  #####################################################


# def func(a):
#     try:
#         if a.is_dir():
#             nameList.append(a)
#             for x in a.iterdir():
#                 func(x)
#         else:
#             nameList.append(a)
#     except PermissionError as e:
#         pass


# searchCount = 1
# numTest = 1
# x = pathlib.Path(r'C:\Users').parent
# print('Path- ', x)
# print('search Count -', searchCount)
# buildStart = time.time()

# func(x)
# print(len(nameList), ' files loaded in database, sorting...')


# def addToDict(score, j):
#     x = True
#     while x:
#         counter = 0
#         if score not in testDict:
#             testDict[score] = j
#             x = False
#         else:
#             while score+counter in testDict:
#                 counter += 1
#             testDict[score+counter] = j
#             x = False
#     x = True


# def calcScore(z, name):
#     try:
#         l = beta1.index(z.lower()[0])
#         score = 0
#         score += int((l+10))*1000
#         score += int((len(z)/10))*10
#         addToDict(score, name)

#     except ValueError:
#         pass


# for z in nameList:
#     if z.stem:
#         calcScore(z.stem, z)
#     else:
#         calcScore(str(z), z)

# buildFinish = time.time()
# print('build diff - ', buildFinish-buildStart)
# print('Beginning search...', time.time())


# def score(z):
#     score = 0
#     try:
#         l = beta1.index(z.lower()[0])
#         score += int((l+10))*1000
#         score += int((len(z))/10)*10
#     except (ValueError, IndexError):
#         score = 0
#     return score


# def searchFunction(search):
#     z = 0
#     j = True
#     resultList = []
#     while j:
#         try:
#             temp = score(search)
#             a = testDict[temp+z]
#             if str(a.stem).lower() == search.lower():
#                 j = False
#                 return (str(a), resultList)
#             elif temp in testDict:
#                 z += 1
#                 resultList.append(a)
#             else:
#                 j = False
#                 return resultList
#         except KeyError:
#             j = False
#     return (0, resultList)


# flag2 = True
# avgTime = []
# startTime = time.time()

# finishTime = time.time()
# print('Time to build database - ', buildFinish-buildStart)


# def abcd(z):
#     for a in range(4):
#         try:
#             l = beta1.index(z.lower()[0])
#             score = 0
#             score += int((l+10))*1000
#             score += int((len(z)/10))*10
#             return score

#         except ValueError:
#             pass


# while True:
#     print('Enter file name -')

#     userInput = input()
#     print(score(userInput))
#     result = searchFunction(userInput.lower())
#     closestList = []
#     resultList = []
#     if result[0] != 0:
#         if userInput in str(result[0]):
#             print('result - \n')
#             print(result[0])
#     elif result[0] == 0:
#         for a in result[1]:
#             if userInput in str(a).lower():
#                 closestList.append(a)
#             else:
#                 resultList.append(a)
#         print('Similar files - \n')
#         for j in closestList:
#             print(str(j))
#     else:
#         print('No such file \n')
#     print(closestList)
#     # for x in resultList:
#     #     print(str(x))
