def criar_matriz(n_linhas, n_colunas, valor):
    #lista vazia
    matriz = []
    for i in range(n_linhas):
        linha = []

        for j in range(n_colunas):
            linha.append(valor)

        matriz.append(linha)
    return matriz


#programa principal
A = criar_matriz(5, 5, 0)

print(A)