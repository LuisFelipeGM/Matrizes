def meses():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return meses

def criar_matriz():
    #matriz vazia (coluna)
    matriz = []
    for i in range(12):
        #criando linha (Mes)
        linha = []

        # Verifica se o mês é Fevereiro
        if(i == 1):
            for k in range(28):
                # Coloca o valor (dia) na linha
                linha.append(k)
            matriz.append(linha)

        # Verifica se o mês tem 31 dias 
        elif (i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11):
            for j in range(31):
                # Coloca o valor (dia) na linha
                linha.append(j)
            matriz.append(linha)



