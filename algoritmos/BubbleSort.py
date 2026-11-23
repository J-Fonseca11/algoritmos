def bubble_sort(lista):
    a = lista.copy()
    comp = troc = 0
    n = len(a)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comp += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                troc += 1
                trocou = True
        if not trocou:
            break
    return a, comp, troc