import numpy as np

# Exercise number one
def one():
    a = np.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]])
    print(a)

# Exercise number two
def two(arr):
    print(np.all(arr))

# Exercise number three
def three():
    a = np.array([1, 7, 13, 105])
    print("%d bytes" % (a.size * a.itemsize))

# Exercise number four
def four():
    print(np.arange(30, 71))

# Exercise number five
def five(arr):
    rev_arr = arr[::-1]
    print(rev_arr)

# Exercise number six
def six():
    a = np.arange(1, 100)
    n = a[(a % 3 == 0) | (a % 5 == 0)]
    print(n)
    print(n.sum())

# Exercise number seven
def seven():
    arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
    arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
    addedArr = np.add(arrayOne, arrayTwo)
    square = np.sqrt(addedArr)
    print(square)

# Exercise numebr eight
def eight():
    a = np.arange(100, 200, 10)
    a = a.reshape(5, 2)
    print(a)

# Exercise number nine
def nine():
    sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
    print(np.amax(sampleArray, 0))
    print(np.amin(sampleArray, 1))

# Exercise number ten
def ten():
    sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
    sortRow = sampleArray[:, sampleArray[1].argsort()]
    sortColumn = sampleArray[np.argsort(sampleArray[:, 1])]
    print(sortRow)
    print(sortColumn)