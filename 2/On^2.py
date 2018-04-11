from random import randint # 随机函数
import timeit  # 时间

# 冒泡排序
def bubbleSort(alist):
  exchange = False
  for i in range(len(alist)-1, 0, -1):
    for j in range(i):
      if alist[j] > alist[j+1]:
        alist[j],alist[j+1] = alist[j+1],alist[j]
        exchange = True
    if not exchange:
      break
  return alist

# 选择排序
def selectionSort(mylist):
  for i in range(len(mylist)):
    minP = i
    for j in range(i, len(mylist)):
      if mylist[minP] > mylist[j]:
        minP = j
    mylist[i], mylist[minP] = mylist[minP], mylist[i]
  return mylist

# 插入排序
def insertionSort (alist):
  for i in range(1, len(alist)):
    currentvalue = alist[i]
    position = i
    while alist[position - 1] > currentvalue and position > 0:
      alist[position] = alist[position - 1]
      position = position - 1
    alist[position] = currentvalue
  return alist

max = 5000
listc = [randint(-max, max) for i in range(max)]
alist = listc[:]
blist = listc[:]
clist = listc[:]
t1 = timeit.Timer('bubbleSort(alist)','from __main__ import bubbleSort,alist')
print('冒泡排序: %s s' %t1.timeit(number=1))

t2=timeit.Timer('selectionSort(blist)','from __main__ import selectionSort,blist')
print('选择排序: %s s' %t2.timeit(number=1))

t3=timeit.Timer('insertionSort(clist)','from __main__ import insertionSort,clist')
print('插入排序: %s s' %t3.timeit(number=1))

  
