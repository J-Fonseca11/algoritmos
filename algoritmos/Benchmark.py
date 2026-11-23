import csv
import os
import random
import time

from BubbleSort import bubble_sort
from MergeSort import merge_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort

TAMANHOS = [100, 500, 1000, 5000, 10000]
REPETICOES = 5

pasta = os.path.dirname(os.path.abspath(__file__))

dados = []
with open(os.path.join(pasta, "bakery_sales_dataset.csv"), encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        dados.append(float(linha["Total_Bill"]))

algoritmos = [("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort),
              ("Selection Sort", selection_sort), ("Merge Sort", merge_sort)]

def fmt(x, casas):
    return f"{x:.{casas}f}".replace(".", ",")   # vírgula decimal para o Power BI em pt-BR

random.seed(42)
linhas = []
for n in TAMANHOS:
    aleatoria = random.sample(dados, n)
    ordenada, _, _ = merge_sort(aleatoria)      # sem sorted()
    cenarios = [("Aleatório", aleatoria), ("Ordenado", ordenada), ("Inverso", ordenada[::-1])]
    for cenario, amostra in cenarios:
        for nome, funcao in algoritmos:
            tempos = []
            for _ in range(REPETICOES):
                ini = time.perf_counter()
                _, comp, troc = funcao(amostra)
                tempos.append((time.perf_counter() - ini) * 1000)
            media = sum(tempos) / REPETICOES
            linhas.append([nome, cenario, n, fmt(media, 3), comp, troc])
            print(f"n={n:<6} {cenario:<10} {nome:<15} {media:10.2f} ms")

with open(os.path.join(pasta, "resultados.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["Algoritmo", "Cenario", "n", "Tempo_ms", "Comparacoes", "Trocas"])
    w.writerows(linhas)
print("\nGerado: resultados.csv")
