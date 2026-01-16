A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]
C=list(map(lambda a,b :list(map(lambda x,y: x+y,a,b)),A,B))

print(C)