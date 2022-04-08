
def quicksort(collection):

    def recursive_quicksort(collection, start, end):

        if not start >= end:
            
            pivot = start
            j = start

            for i in range(j, end):
                if collection[i] < collection[pivot]:
                    collection[i], collection[j+1] = collection[j+1], collection[i]
                    j += 1

            collection[pivot], collection[j] = collection[j], collection[pivot]

            recursive_quicksort(collection, start, j)
            recursive_quicksort(collection, j+1, end)


    recursive_quicksort(collection, 0, len(collection))
