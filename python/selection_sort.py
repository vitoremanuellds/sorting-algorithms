def selection_sort(item):
    
    for i in range(len(item)-1):

        smallest = i

        for k in range(i+1, len(item)):
            if item[k] < item[smallest]:
                smallest = k

        item[i], item[smallest] = item[smallest], item[i]
