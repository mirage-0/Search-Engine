import databasetest
import pathlib

path = r'C:\Users\rajka\Desktop\uwe\ASD\Group_project\PROJ'
x = pathlib.Path(path)
manager = databasetest.manager()
manager.buildList(x)
print(len(manager.dirList), ' files loaded in database, sorting...')
# build file and directory list, sort them and construct dict in next step
manager.buildList(x)
manager.buildDict()

while True:
    print('Enter file name -')

    userInput = input().lower()
    score = manager.calcScore(userInput)
    result = manager.searchFunction(userInput)
    closestList = []
    resultList = []
    if result[0] != 0:
        if userInput in str(result[0]):
            print('result - \n')
            print(result[0])
    elif result[0] == 0:
        for a in result[1]:
            if userInput in str(a).lower():
                closestList.append(a)
            else:
                resultList.append(a)
        print('Similar files - \n')
        for j in closestList:
            print(str(j))
    else:
        print('No such file \n')
    print(closestList)
