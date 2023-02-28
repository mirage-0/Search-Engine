import time
import pathlib
import random
import copy


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
        # 'document', 'pictures',
        # default formats
        self.musicFormats = ['.mp3', '.aac', '.ogg', '.flac', '.alac', '.m4a', 'm4v',
                             '.wav', '.aiff', '.dsd', '.pcm', '.mp1', '.mp2', '.webm']

        self.videoFormats = ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.mov', '.qt',
                             '.flv', '.swf', '.mts', '.m2ts', '.ts']
        self.unknownFormat = []
        self.documentFormat = ['.pdf', '.docx',
                               '.zip', '.7zip', '.doc', '.asta', '.txt']
        self.photoFormats = ['.jpg', '.png', '.PNG', '.jpeg', '.gif', '']
        self.executableFormat = ['.apk', '.exe']
        self.defaultCategories = {'easilyrecognisablemusic': self.musicFormats, 'movies': self.videoFormats,
                                  'photo': self.photoFormats, 'document': self.documentFormat, 'executable': self.executableFormat, 'unknown': self.unknownFormat}
        # contains all file categories

        # self.layer0 = {'music': layer1[0],
        #                'movies': layer1[1], 'unknown': layer[2]}
        self.layer0 = {}
        # self.layer1 = {}
        # contains all category formats, are simple dictionaries
        # self.layer1 = {score('mp4'): layer2, score(
        #     'mp3'): layer2, score('mp2'): layer2}

        # dictionary, create new, dont use this
        # self.layer2 = {score('filename'): path}

    # TODO implement search function in tree class, return file path
    def search(self, file, score, buffer):
        # print(file, score)
        flag = 1
        result = []
        closeResult = []
        for k in self.layer0:
            layer1 = self.layer0[k]
            for l in layer1:
                layer2 = layer1[l]
                for m in layer2:
                    # if m == 440040:
                    # {print(m, file, score)}
                    # print('file- ', (m), file,
                    #       (score), layer2[m])
                    div = (len(str(score))-2)
                    # if m == 2996000:
                    #     print(div, file, score)

                    # print(score, div)
                    if int(m / 10**div) == int(score/10**div):
                        flag = True
                        counter = 0
                        # print('a')
                        while flag:
                            # print('enter while')
                            try:
                                # print('file- ', file, score, layer2[m+counter])
                                dFile = layer2[m+counter]
                                # if m == 2996000:
                                #     print(div, file, dFile, score, m,
                                #           int(m/10**div), int(score/10**div))
                                if dFile.stem.lower() == file:
                                    # print(file, dFile.stem, m+counter)

                                    # if file == dFile.stem.lower():
                                    # print('aaa')
                                    # print('wor')
                                    result.append(dFile)
                                elif self.similarity(file.lower(), dFile.stem.lower(), buffer):
                                    # print('W')
                                    # if (dFile.stem) == 'Satan.m4a':
                                    # print(file, 'tf',
                                    #       dFile.stem.lower(), '\n', '\n')
                                    closeResult.append(dFile)
                                    # print(tuple(closeResult))
                            except KeyError:
                                # print('L', score, counter)
                                flag = False

                            # print('exit while', counter)
                            counter += 1
        if result or closeResult:
            return (result, closeResult)
        else:
            return 0

    def similarity(self, file, f, buffer):
        file = list(file)
        f = list(f)
        c = 0.75
        s = 0
        score = []
        for x in range(buffer):
            file.pop(0)
            # print(file)
        y = 0
        j = 0
        temp = 0
        flag2 = True
        # TODO optimise by checking string len diff
        while y < len(f)-1 and flag2:
            # print(f, file, y)
            # print(f, file, y)

            try:
                index = file.index(f[y])

                j = index
                flag = True
                temp = y
                # print('out of while break ----------')
                # print('enter while loop', file[j], f[y], j, y)
                while j < len(file) and flag and temp < len(f):
                    # if f == const:
                    # print('1', file[j], f[temp], j, temp)
                    # print(file)
                    if file[j] == f[temp]:
                        s += 1
                        # if f == const:
                        # print('2',  file[j], f[temp],
                        #   j, temp, f, file)
                        # print(f, file, '\n')
                        if j+1 >= len(file)-1:
                            # print(s)
                            score.append(s)
                            s = 0
                            flag = False
                    else:
                        # if f == const:
                        # print('3', file[j], f[temp], j, temp, '\n')
                        flag = False
                        # if temp+1 >= len(file)-1:
                        #     # print('shi')
                        #     flag2 = False
                        # y += 1
                        # y = temp
                        # TODO optimise by calcing score here only and stopping
                        # if f == ['[', 'e', 'x', 't', 'e', 'n', 'd', 'e', 'd', ']', ' ', 'r', 'o', 'y', 'a', 'l', ' ', 'b', 'l', 'u', 'e', ' ', '(', 'v', 'e', 'g', 'e', 't', 'a', '_', 's', ' ', 'l', 'i', 'm', 'i', 't', ' ', 'b', 'r', 'e', 'a', 'k', 'e', 'r', ' ', 't', 'h', 'e', 'm', 'e', ')', ' ', '_', ' ', 'd', 'r', 'a', 'g', 'o', 'n', ' ', 'b', 'a', 'l', 'l', ' ', 's', 'u', 'p', 'e', 'r', ' ', '「', 'e', 'p', 'i', 'c', ' ', 'o', 'r', 'c', 'h', 'e', 's', 't', 'r', 'a', 'l', ' ', 'c', 'o', 'v', 'e', 'r', '」']:
                        #     print(s, 'else', len(file))
                        # print('###### score - ', s)
                        score.append(s)
                        s = 0
                        # y = temp
                    j += 1
                    temp += 1
                    # y += 1
            except ValueError:
                # print('error', y)
                y += 1
            y += 1
        # file = ''.join(file)
        # for x in range(len(file)):
        #     if file[x] in f:
        #         if f == ['p', 'r', 'e', 's', 'c', 'r', 'i', 'p', 't', 'i', 'o', 'n']:
        #             print('what is going on', f)
        #         j = x
        #         while f[j] == file[x+j]:
        #             s.append(1)
        #             j += 1

        #         # j = 0
        #         # while file[x+j] in f and x+j < len(file)-1:
        #         #     s += 1
        #         #     j += 1
        #     else:
        #         score.append(sum(s))
        #         s.clear()
        # if s:
        #     score.append(s)

        result = 0

        try:
            result = max(score)/len(file)
            # for h in f:
            #     if 's', 'o', 'n', 'i', 'c' in h:
            # print(file, '   ', score, '    ', result, '    ', f)
        except ValueError:
            # print(file, f)
            pass
        # print('wwwwww', result, file)
        # print(file, '   ', score, '    ', result, '    ', f)
        if result > c:
            # print('wwwwww', result, file, f, score, '\n'*200)
            # print(a)
            return True
        else:
            return False

    def addFile(self, file, score):
        # testFlag = True
        flag = True
        print('-----', file.stem, file.suffix)
        for x in self.defaultCategories:
            # print('entering addfile', 'category = ', x, '\n')

            ext = file.suffix

            # print('file and suffixx', file.name, ext)
            # print('x --- ', self.defaultCategories)

            # get extension instead of file.name
            if ext in self.defaultCategories[x]:  # and testFlag:

                # print(file.stem, 'inside default')
                flag = False
                # print('in category', file.stem, ext, x)
                # check if x (defaultCategory) exists in layer0 keys
                # print('before trying', file.stem, ext)
                try:
                    # print('trying')
                    try:
                        print('\n')
                        if self.layer0[x]:
                            # if yes, set layer1 for easy access
                            layer1 = self.layer0[x]
                            print('entering addfile', 'category = ', x, '\n')
                            # loop through layer1 keys (extensions for this category)
                            # for j in (layer1):
                            if layer1[ext]:
                                print(file.stem, file.suffix, '-4')
                                # print((layer1), 'x\n')

                                # if match found, add item to dict
                                layer2 = layer1[ext]
                                # print(file.stem, 'before ext ==j')
                                # for m in layer2:
                                # if ext == j:
                                # print('file and suffixx', file.name, ext)

                                # print(file.stem, self.layer0, 'after ext ==j')
                                loopFlag = True
                                while loopFlag:
                                    counter = 0
                                    if score not in layer2:
                                        print(file.stem, file.suffix, '- fail')
                                        layer2.update({score: file})
                                        # print('added layer2', file.stem)
                                        # print('added layer2 in new position',
                                        #       self.layer0, 'sadsa')
                                        # testFlag = False
                                        loopFlag = False
                                        flag = False
                                    else:
                                        while score+counter in layer2:
                                            counter += 1
                                        layer2.update(
                                            {score+counter: file})
                                        print(file.stem, file.suffix,
                                              '- not fail')
                                        # print('added layer2 in new position',
                                        #       self.layer0)
                                        # testFlag = False
                                        loopFlag = False
                                        flag = False
                            else:
                                print('else ran \n')
                                layer1.update({ext: {score: file}})
                                # print(self.layer0)
                                print('layer1', layer1)
                                # testFlag = False
                                flag = False
                    except KeyError:
                        # print('found it')
                        print('else ran 1', self.layer0[x], '\n')
                        self.layer0[x].update({ext: {score: file}})
                        # testFlag = False
                        flag = False

                        # otherwise append a new layer2 {score: file} to layer1
                    # else:
                    #     # no need to check if key exists in layer2 as layer1 itself doesnt exist
                    #     print(
                    #         'else works???? layer 0 element, layer1 created', 'else')
                    #     self.layer0[x] = {ext: {score: file}}
                    #     flag = False

                    # if category doesn't exist in layer0 keys, make layer1 dict {ext:{layer2}}
                except KeyError:
                    # create layer0[x]
                    # no need to check if key exists in layer2 or layer1 as layer0 itself doesnt exist
                    # print('else works???? layer 0 element, layer1 created', 'except')
                    # print(ext, 'exwasdasafkbshbsblhsbvkjsbflbf')
                    self.layer0.update({x: {ext: {score: file}}})
                    print('else 3', self.layer0)
                    # print(self.layer0, x)
                    # print(self.layer0)
                    # testFlag = False
                    flag = False

             # exension not in categories add it to unknownFormat
               # if layer1:
        if flag:
            print('adding unknown format')
            # print(file)
            self.addUknownFormat(ext)
            # print(self.unknownFormat)
            self.addFile(file, score)
            # else:
            #     temp = {ext: {score, file}}
            #     self.layer1 = temp
        return 1

    # let user create their own category by selecting multiple extensions from a list of unknown formats
    def createNewCat(self, catName, listOfFormats):
        # either get a list, or make a list whichever
        newFormatList = list(listOfFormats)
        self.defaultCategories[catName] = newFormatList

    def addUknownFormat(self, format):
        if format not in self.unknownFormat:
            self.unknownFormat.append(format)
            # print(1)
            return 1

        else:
            return 0


class manager:

    def __init__(self):
        # character list
        self.beta1 = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '.', '_', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                      '-', '_', '+', '=', ']', '}', '{', '[', '!', '`', '~', 'a', 'b', 'c', 'd',
                      'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x',
                      'y', 'z']

        # self.dirTree = Tree()
        self.dirList = []
        self.fileList = []
        self.tree = 0
        self.layerManager()
        searchCount = 1
        numTest = 1
        # self.buildList()
        # look for files in this path

    def layerManager(self):
        # create tree
        self.tree = Tree()
        # populate the tree
        for file in self.fileList:
            if file.suffix:
                # print(file.stem)
                score = self.calcScore(file.stem)
                # print(file, score)
                self.tree.addFile(file, score)
        return (self.tree)

    def search(self, file, depth):
        # print('search ', file)

        # y = (self.tree.search(file, self.calcScore(file)))
        searchDepth = depth
        resultList = []
        closeResults = []
        fileName = file
        # result = self.tree.search(file)
        results = self.tree.search(fileName, self.calcScore(fileName), 0)
        # print(results)
        if results != 0:
            # print('fuck')
            # print(results)
            for x in results[0]:
                resultList.append(x)
            for y in results[1]:
                closeResults.append(y)
        # print(resultList, closeResults)Xs4AsSv.png Xzzzssv
        for buffer in range(searchDepth):
            fileName = ' '+fileName
            # print(fileName)
            for char in self.beta1:
                # print(fileName, '    1')
                fileName = list(fileName)
                # print(fileName, '    2')
                fileName[0] = char
                # print(fileName, '    3')

                fileName = ''.join(fileName)
                # if fileName == 'xzzzssv':
                #     print(self.calcScore('Xs4AsSv'))
                results = self.tree.search(
                    fileName, self.calcScore(fileName), buffer+1)
                # print(results)
                if results != 0:
                    # print('fuck')
                    for x in results[0]:
                        resultList.append(x)
                    for y in results[1]:
                        closeResults.append(y)
        # print(resultList)
        return (resultList, closeResults)

    # def recurse(self, fileName):
    #     for x in range(searchDepth):
    #         fileName = ' '+file
    #         print(fileName)
    #         for char in self.beta1:
    #             # print(fileName, '    1')
    #             fileName = list(fileName)
    #             # print(fileName, '    2')
    #             fileName[0] = char
    #             # print(fileName, '    3')

    #             fileName = ''.join(fileName)
    #             # print(fileName)
    #             results = self.tree.search(fileName, self.calcScore(fileName))
    #             # print(results)
    #             if results != 0:
    #                 # print('fuck')
    #                 return (results, results)

        # print(x+file, y[0], 'bbbbb')

        # for x in self.beta1:
        #     y = (self.tree.search(file, self.calcScore(file)))
        #     if y[0] == 0:
        #         y = (self.tree.search(x+file, self.calcScore(x+file)))

    # def buildDict(self):
    #     # TODO: Later
    #     # for dirName in self.dirList:
    #     #     if dirName.stem:
    #     #         self.addToDict(self.calcScore(dirName.stem), dirName)
    #     #     else:  # z is a root disk ex: [C:\, D:\, E:\], thus .stem wont exist
    #     #         self.addToDict(self.calcScore(str(dirName)), dirName)

    #     # Go through all files
    #     for fileName in self.fileList:
    #         if fileName.name:

    #             self.addToDict(self.calcScore(
    #                 fileName.stem, fileName), fileName)
    #         # will probably never run since filename stems will always exist
    #         else:
    #             self.addToDict(self.calcScore(str(fileName), fileName))

    def buildList(self, a):
        try:
            if a.is_dir():
                # all directories are appended to nameList
                self.dirList.append(a)
                for x in a.iterdir():
                    self.buildList(x)
            else:
                # all files are appended to fileList
                # print(a)
                # if a.suffix == '':
                # print(a)
                self.fileList.append(a)
        except PermissionError as e:
            pass

    # def addToDict(self, score, file, dict):
    #     # TODO: Select correct dictionary, if doesnt exist create it, add to specific dictionary
    #     x = True

    #     while x:
    #         counter = 0
    #         if score not in self.fileList:
    #             self.fileList[score] = file
    #             x = False
    #         else:
    #             while score+counter in self.fileList:
    #                 counter += 1
    #             self.fileList[score+counter] = file
    #             x = False
    #     x = True

    def calcScore(self, fileName):
        # TODO update to search in the middle of strings
        # a = copy.deepcopy(self.beta1)
        # d = {}
        # for x in a:
        #     d.update({x: 0})

        # for y in fileName.lower():
        #     if y in d:
        #         d[y] = d[y]+1
        # # delete all 0's
        # for z in list(d):
        #     if d[z] == 0:
        #         del d[z]
        # finalDict = {}
        # word = []
        # temp = list(d)
        # temp.sort()
        # for c in range(100):
        #     for x in d:
        #         if d[x] == c:
        #             try:
        #                 if finalDict[c]:
        #                     finalDict[c] = finalDict[c] + x
        #             except KeyError:
        #                 finalDict[c] = x
        # print(finalDict)
        # for o in temp:

        #     word.append(o)
        # print(d)

        try:
            l = self.beta1.index(fileName.lower()[0])
            score = 0
            score += int((l))*100000
            # print(score, 'name')
            score += int((len(fileName)))*1000
            # print(score, 'len')
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

    # def searchFunction(self, search):
    #     z = 0
    #     j = True
    #     resultList = []
    #     # TODO: search through the correct dict, if cant find initially, start searching through all dicts
    #     # current implementation will be sequential, future will be parallel, multi core
    #     while j:
    #         try:
    #             groupScore = self.calcScore(search)
    #             a = self.testDict[groupScore+z]
    #             if a.stem.lower() == search:
    #                 j = False
    #                 return (a.name, resultList)
    #             elif groupScore in self.testDict:
    #                 z += 1
    #                 resultList.append(a)
    #             # else:
    #             #     j = False
    #                 # return (0, resultList)
    #         except KeyError:
    #             j = False
    #     return (0, resultList)

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
