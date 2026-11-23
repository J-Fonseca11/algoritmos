def insertion_sort(lista):
    v = lista.copy()
    comp = troc = 0
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if v[j] > chave:
                v[j + 1] = v[j]
                troc += 1
                j -= 1
            else:
                break
        v[j + 1] = chave
    return v, comp, troc