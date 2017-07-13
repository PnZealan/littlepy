import random


def main(list):
    n = len(list)
    for i in range(1, n):
        left = 0
        get = list[i]
        right = i-1
        while(left <= right):
            mid = int((left + right) / 2)
            if (list[mid] > get):
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i-1, left+1, -1):
            list[j+1] = list[j]
        list[left] = get
    print(list)

if __name__ == '__main__':
    l = []
    for i in range(2, 10**4):
        l.append(random.randint(1, i))
    main(l)
            
