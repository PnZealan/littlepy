#-*- coding:utf-8 -*-
#filename: quick_sort.py
import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    #print(A)

def Partition(A, left, right):
    pivot = A[right]
    tail = left - 1
    for i in range(left, right):
        if A[i] <= pivot:
            tail += 1
            swap(A, tail, i)
    swap(A, tail+1, right)
    return tail+1

def QuickSort(A, left, right):
    if (left >= right):
        return
    index_pivot = Partition(A, left, right)
    QuickSort(A, left, index_pivot-1)
    QuickSort(A, index_pivot+1, right)

def main():
    #A = [5, 6, 8, 3, 7, 2, 9]
    A = []
    for i in range(10**4):
        A.append(random.randint(1,100))
    #print(A)
    QuickSort(A, 0, len(A)-1)
    #print(A)

if __name__ == '__main__':
    main()
    

