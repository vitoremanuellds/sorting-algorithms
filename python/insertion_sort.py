def insertion_sort(item):
    
    for i in range(1, len(item)):

        auxElement = item[i]

        k = i

        while (k > 0 and item[k-1] > auxElement):

            item[k] = item[k-1]

            k -= 1

        item[k] = auxElement
