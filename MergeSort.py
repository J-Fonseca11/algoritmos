def merge_sort(lista):
    cont = [0, 0]  # [comparações, movimentações]

    def ordenar(a):
        if len(a) <= 1:
            return a
        meio = len(a) // 2
        esq = ordenar(a[:meio])
        dir = ordenar(a[meio:])
        r = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            cont[0] += 1
            if esq[i] <= dir[j]:
                r.append(esq[i]); i += 1
            else:
                r.append(dir[j]); j += 1
            cont[1] += 1
        while i < len(esq):
            r.append(esq[i]); i += 1; cont[1] += 1
        while j < len(dir):
            r.append(dir[j]); j += 1; cont[1] += 1
        return r

    return ordenar(lista), cont[0], cont[1]