# from multiprocessing import Pool


# def f(x):
#     return x*x


# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))


x = [1, 2, 3, 4]
print(x, 'line 15\n')
x.append([])
print(x, 'line 17\n')
# x[4] = 5 will give an error, x[4] is a list itself
x[4].append('joe')
print(x, 'line 19\n')
x[4].append('xbox')
print(x, 'line 21\n')
x[4].append([])
print(x, 'line 23\n')
x[4][2].append('list in a list in a list')
print(x)
