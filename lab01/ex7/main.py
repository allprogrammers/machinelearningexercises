import numpy as np

def main():
    n = int(input())
    m = int(input())

    # Exercise 7a
    arr = np.fromfunction(lambda i, j: (i+1) * (j+1), (n, m), dtype=float)

    print(arr)
    print("")

    # Exercise 7b
    for i in range(m):
        arr[:,i] = arr[:,i]/arr[:,i].sum()
    print(arr)
    print("")

    # Exercise 7c
    arr = np.fromfunction(lambda i, j: (i+1) * (j+1), (n, m), dtype=float)
    for i in range(n):
        arr[i,:] = arr[i,:]/arr[i,:].sum()
    print(arr)
    print("")

    # Exercise 7d
    arr = np.fromfunction(lambda i, j: (-i+1) * (j+1), (n, m), dtype=float)
    print(arr)
    # reduce all negative values to zero
    newarr = np.array(arr)
    newarr[newarr < 0] = 0

    print(newarr)

    # Exercise 7e
    arr1 = np.fromfunction(lambda i, j: (-i+1) * (j+1), (n, m), dtype=float)
    arr2 = np.fromfunction(lambda i, j: (i+1) * (j+1), (n, m), dtype=float)

    print(arr1)
    print(arr2)

    ans = np.dot(arr1, arr2)
    print(ans)
    print(ans.sum())



if __name__ == "__main__":
    main()
