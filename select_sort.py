import random


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def main(list):
    n = len(list)
    print(list)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if list[j] < list[min]:
                swap(list, j, min)
    print(list)

if __name__ == '__main__':
    l = []
    for i in range(2, 10**4):
        l.append(random.randint(1, i))
    main(l)
        
