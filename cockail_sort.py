import random


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def main(list):
    left = 0
    right = len(list) - 1
    #print(list)
    while(left < right):
        for i in range(right):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
        right = right - 1
        for j in range(right, left, -1):
            if list[j-1] > list[j]:
                swap(list, j-1, j)
        left = left + 1
    print(list)

if __name__ == '__main__':
    l = []
    for i in range(2, 10**4):
        l.append(random.randint(1, i))
    main(l)
