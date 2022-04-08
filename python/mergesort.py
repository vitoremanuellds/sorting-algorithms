def mergesort(collection):
    
    def merge(a, b):
        c = []
        while (len(a) != 0 and len(b) != 0):
            if a[0] < b[0]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))

        for i in range(max(len(a), len(b))):
            if len(a) == 0:
                c.append(b.pop(0))
            else:
                c.append(a.pop(0))

        return c


    if (len(collection)) <= 1:
        return collection
  
    middle = int(len(collection)/2)
  
    a = mergesort(collection[:middle])
    b = mergesort(collection[middle:])
  
    return merge(a, b)

