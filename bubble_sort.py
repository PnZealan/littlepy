import random


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def main(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                swap(list, j, j+1)

if __name__ == '__main__':
    l = []
    for i in range(2, 10**4):
        l.append(random.randint(1, i))
    main(l)
    print(l)
