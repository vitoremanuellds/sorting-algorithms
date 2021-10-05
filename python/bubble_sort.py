def bubble_sort(item):

    for i in range(len(item) - 1):

        for k in range(len(item) - 1 - i):

            if item[k] > item[k + 1]:
                item[k], item[k+1] = item[k+1], item[k]