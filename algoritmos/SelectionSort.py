def selection_sort(lista):
    v = lista.copy()
    comp = troc = 0
    n = len(v)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comp += 1
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            troc += 1
    return v, comp, troc