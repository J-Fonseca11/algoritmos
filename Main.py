import csv
import os
import time

from BubbleSort import bubble_sort
from MergeSort import merge_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort

# Acha o CSV na mesma pasta do script, de qualquer lugar que você rodar
pasta = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta, "bakery_sales_dataset.csv")

dados = []
with open(caminho, encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        dados.append(float(linha["Total_Bill"]))

print(len(dados))   # deve mostrar 19321

while True:
    print("\n1 - Bubble Sort")
    print("2 - Merge Sort")
    print("3 - Insertion Sort")
    print("4 - Selection Sort")
    print("0 - Sair")

    opcao = input("Escolha: ")

    match opcao:
        case "0":
            break
        case "1":
            nome, funcao = "Bubble Sort", bubble_sort
        case "2":
            nome, funcao = "Merge Sort", merge_sort
        case "3":
            nome, funcao = "Insertion Sort", insertion_sort
        case "4":
            nome, funcao = "Selection Sort", selection_sort
        case _:
            print("Opção inválida!")
            continue

    n = int(input(f"Tamanho da amostra (máx {len(dados)}): "))
    amostra = dados[:n]

    inicio = time.perf_counter()
    ordenada, comparacoes, trocas = funcao(amostra)
    fim = time.perf_counter()

    print(f"\n{nome} com n = {n}")
    print(f"Tempo: {(fim - inicio) * 1000:.2f} ms")
    print(f"Comparações: {comparacoes}")
    print(f"Trocas/movimentações: {trocas}")
    print("Primeiros 5:", ordenada[:5])