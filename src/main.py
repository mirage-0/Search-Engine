import databasetest
import pathlib
import json
import timeit

# path = r'C:\Users'
# rajka\Desktop\uwe\ASD\Group_project\PROJ\asd\src'
path = r'C:\Users\rajka\Desktop\uwe\ASD\Group_project\PROJ'
x = pathlib.Path(path).parent
manager = databasetest.manager()
manager.buildList(x)
# print(len(manager.dirList), ' files loaded in database, sorting...')
# build file and directory list, sort them and construct dict in next step
# manager.buildList(x)
a = timeit.timeit()
tree = manager.layerManager()
b = timeit.timeit()
# print(tree.layer0)

# print('took ', b-a, ' seconds, or',
#       round((b-a)/60, 2), ' minutes to build database')
# for x in manager.fileList:
#     print(x)


def displayLayer(manager):
    for x in manager.tree.layer0:
        # print(x)
        for y in manager.tree.layer0[x]:
            # print('  -', y)
            for z in manager.tree.layer0[x][y]:
                # if z == 650070:
                # print('--    ', manager.tree.layer0[x][y]
                #       [z].stem, x, y, z)
                print(x, y, z,  manager.tree.layer0[x][y][z].as_posix())


print('\n')
displayLayer(manager)
# for x in manage:
# print(x)

# with open('convert.txt', 'w') as convert_file:
#     convert_file.write(json.dumps(manager.tree.layer0))

# print(manager.tree.layer0['movies'])
depth = 8

while False:
    # print('enter depth, 1-10 [larger is slower]')
    # depth = int(input())
    print('enter input [file name] -')
    search = input().lower()

    # print(manager.search(search))
    # manager.search(search)
    # print(timeit.timeit())
    m = manager.search(search, 1)
    # print(timeit.timeit())
    print('exact match - ')
    for x in m[0]:
        print('name ', '   ', '    |     location')
        print(x.stem, x)
    print('\n')
    print('close match - ')
    print('name ', '    |     location')
    crlist = []
    for j in range(1):
        m = manager.search(search, depth)
        for y in m[1]:

            # print(y.stem, '   ', y)
            crlist.append(y)
        # print('\n')

    # crlist = sorted(crlist, key=len)
    # crlist = list(set(crlist))
    # for x in crlist:
    #     print(x.stem, x)
    # print(m)

    # print('it took ', k-t, ' seconds to finish search ')


# {'unknown':
#     {'.pdf':
#         {'.asta':
#               {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/use case.asta')},
#                 62010: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/usecase diagram f.pdf')}}}

# {'unknown':
#     {'.pdf':{62010: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/usecase diagram f.pdf')} ,
#      '.asta': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/use case.asta')}}}}


# {'unknown': {'.url': {64010: WindowsPath('C:/Users/rajka/Desktop/War Thunder.url')},
#              '.lnk': {67000: WindowsPath('C:/Users/rajka/Desktop/:/Users/rajka/Desktop/backup/picturres/u4ijf8asaqc61.jpg (1)')},
#              '.jpg (2)': {16010: WindowsPath('C:/Users/rajka/Desktop/backup/picturres/6ku0is8lpku61.jpg (2)'), 16011: WindowsPath('C:/Users/rajka/Desktop/backup/picturres/6ku0is8lpku61.jpg (2)')},
#              '.jpeg': {51020: WindowsPath('C:/Users/rajka/Desktop/backup/picturres/Img_2021_10_07_18_29_31.jpeg'), 51021: WindowsPath('C:/Users/rajka/Desktop/backup/picturres/Img_2021_10_07_18_29_31.jpeg')},
#              '.kra': {59000: WindowsPath('C:/Users/rajka/Desktop/backup/picturres/K/roboragi.kra'), 59001: WindowsPath('C:/Users/rajka/Desktop/backup/picturres/K/roboragi.kra')},
#              '.zip': {43030: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/astah_uml_license_2022-2023.xml.zip')},
#              '.m4v': {61020: WindowsPath("C:/Users/rajka/Desktop/backup/Video/TFS - Vegeta's Dick_HD.m4v")},
#              '.ini': {46000: WindowsPath('C:/Users/rajka/Desktop/desktop.ini')},
#              '.sample': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/.git/hooks/update.sample')},
#              '.py': {63000: WindowsPath('C:/Users/rajka/Desktop/uwe/python/tutorial/v2.py')},
#              '.pyc': {50020: WindowsPath('C:/Users/rajka/Desktop/uwe/python/tutorial/__pycache__/helloworld.cpython-310.pyc')},
#              '.md': {59000: WindowsPath('C:/Users/rajka/Desktop/Search Engine/README.md')},
#              '.doc': {49020: WindowsPath('C:/Users/rajka/Desktop/uwe/AI/Worksheets/GA Karanraj Singh 22045397.doc'), 49021: WindowsPath('C:/Users/rajka/Desktop/uwe/AI/Worksheets/GA Karanraj Singh 22045397.doc')},
#              '.xml': {20020: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/astah_uml_license_2022-2023.xml/__MACOSX/._astah_uml_license_2022-2023.xml'), 20021: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/astah_uml_license_2022-2023.xml/__MACOSX/._astah_uml_license_2022-2023.xml')},
#              '.asta': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/use case.asta')},
#              '.bin': {60000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/state.bin')},
#              '.7z': {62010: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9.7z')},
#              '.docx': {57010: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/pintos system calls.docx')},
#              '.odt': {50010: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/WP22045397/Horizon_Cinema.odt')},
#              '.exe': {57000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/putty.exe'), 57001: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/putty.exe')},
#              '.vmem': {15030: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/564ddf3e-980a-68ad-6e43-0d23dc629b0f.vmem')},
#              '.lck': {54000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/uweOS_disk.vmdk.lck/M27308.lck')},
#              '.nvram': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/uweOS.nvram')},
#              '.vmsd': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/uweOS.vmsd')},
#              '.vmx': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/uweOS.vmx')},
#              '.vmxf': {62000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/uweOS.vmxf')},
#              '.vmdk': {62010: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/uweOS_disk.vmdk')},
#              '.scoreboard': {63000: WindowsPath('C:/Users/rajka/Desktop/uwe/OS/uweOS_vmware_v0.9/uweOS_vm/vm.scoreboard')}}}


# {'unknown': {'.py': {44000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/bookings.py'),
#                      45000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/cinema.py'),
#                      45001: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/city.py'),
#                      47000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/employee.py'),
#                      49000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/gui.py'),
#                      53000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/login.py'),
#                      54000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/main.py'),
#                      59000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/records.py')}}}

# {'unknown': {'.py': {44000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/bookings.py'),
#                      45000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/cinema.py'),
#                      45001: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/city.py'),
#                      47000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/employee.py'),
#                      49000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/gui.py'),
#                      53000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/login.py'),
#                      54000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/main.py'),
#                      59000: WindowsPath('C:/Users/rajka/Desktop/uwe/ASD/Group_project/PROJ/asd/src/records.py')}}}


# while True:
# print('Enter file name -')

# userInput = input().lower()
# score = manager.calcScore(userInput)
# result = manager.searchFunction(userInput)
# closestList = []
# resultList = []
# if result[0] != 0:
#     if userInput in str(result[0]):
#         print('result - \n')
#         print(result[0])
# elif result[0] == 0:
#     for a in result[1]:
#         if userInput in str(a).lower():
#             closestList.append(a)
#         else:
#             resultList.append(a)
#     print('Similar files - \n')
#     for j in closestList:
#         print(str(j))
# else:
#     print('No such file \n')
# print(closestList)
