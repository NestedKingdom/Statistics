import csv
import math as mh

def csvtolist(str):
    with open(str) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cs = list(csv_reader)
        cs = list(map(int, cs[0]))
    return cs

# tr=csvtolist('data.txt') example of function

def getmean(lst):
    while len(lst) > 5:
        a = 0
        b = 5
        ls = []

        for i in range(int(mh.ceil(len(lst) / 5))):
            ls.append([])
            if len(lst) % 5 != 0 and i == int(mh.ceil(len(lst) / 5)) - 1:
                b = len(lst) % 5

            for j in range(a, a + b):
                ls[i].append(lst[j])
            a += 5
        for j in range(len(ls)):
            mean = sum(ls[j]) / len(ls[j])
            ls[j] = mean
        lst = ls
    if len(lst) <= 5:
        mean = sum(lst) / len(lst)
        return mean


def getmedian(lst):
    while len(lst) > 5:
        a = 0
        b = 5
        ls = []

        for i in range(int(mh.ceil(len(lst) / 5))):
            ls.append([])
            if len(lst) % 5 != 0 and i == int(mh.ceil(len(lst) / 5)) - 1:
                b = len(lst) % 5

            for j in range(a, a + b):
                ls[i].append(lst[j])
            a += 5
        for j in range(len(ls)):
            if len(ls[j]) % 2 != 0:
                median = sorted(ls[j])
                median = median[int(len(median) / 2)]
                ls[j] = median
            else:
                median = sorted(ls[j])
                median = getmean(median[int(a / 2):int((a / 2) + 1)])
                ls[j] = median
        lst = ls
    a = len(lst)
    if a <= 5:
        if a % 2 != 0:
            median = sorted(lst)
            median = median[int(len(median) / 2)]
            return median
        else:
            median = sorted(lst)
            median = getmean(median[int(a / 2):int((a / 2) + 1)])
            return median


def getmode(lst):
        return max(lst,key=lst.count)
