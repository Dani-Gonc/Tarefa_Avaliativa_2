alunos = []

print("----SISTEMA ESCOLAR----")
quantAlunos = int(input("Quantos alunos serão cadastrados: "))

for i in range(quantAlunos):
    aluno = []

    aluno.append(input("Digite o nome do aluno: "))

    notasT = []
    notasT.append(float(input("Digite a nota T1: ")))
    notasT.append(float(input("Digite a nota T2: ")))
    aluno.append(notasT)

    notasP = []
    notasP.append(float(input("Digite a nota P1: ")))
    notasP.append(float(input("Digite a nota P2: ")))
    aluno.append(notasP)

    medias = [
        notasT[0] * 0.4 + notasT[1] * 0.6,
        (notasP[0] + notasP[1]) / 2
    ]
    aluno.append(medias)

    mediaF = medias[0] * 0.3 + medias[1] * 0.7

    if medias[0] > 5 and medias[1] > 5:
        if medias[0] < medias[1]:
            mediaF = medias[0]
        else:
            mediaF = medias[1]

    aluno.append(mediaF)

rodarMenu = True

while rodarMenu:
    print("----MENU DE OPÇÕES----")

    print("1 - Boletim de cada aluno")
    print("2 - Encontrar aluno por nome")
    print("3 - Aluno com maior média final (MF)")
    print("4 - Aluno com menor média final (MF)")
    print("5 - Percentual de alunos com média final (MF) superior a 5")
    print("6 - Sair")
    print("---------------------")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("----BOLETINS DOS ALUNOS----")

        for aluno in alunos:
            print("---------------------")
            print("Nome: ", aluno[0])
            print("Média teórica (MT): ", aluno[3][0])
            print("Média prática (MP): ", aluno[3][1])
            print("Média final (MF): ", aluno[4])

    elif opcao == 2:
        print("----PESQUISAR ALUNO----")
        nome = input("Digite o nome do aluno: ")

        for aluno in alunos:
            if aluno[0] == nome:
                print("---------------------")
                print("Nome: ", aluno[0])
                print("Nota T1: ", aluno[1][0])
                print("Nota T2: ", aluno[1][1])
                print("Nota P1: ", aluno[2][0])
                print("Nota P2: ", aluno[2][1])
                print("Média teórica (MT): ", aluno[3][0])
                print("Média prática (MP): ", aluno[3][1])
                print("Média final (MF): ", aluno[4])
                break
        
        print("Aluno não encontrado!")

    elif opcao == 3:
        print("----ALUNO COM MAIOR MÉDIA FINAL (MF)----")
        menorMedia = alunos[0]

        for aluno in alunos:
            if aluno[4] > menorMedia[4]:
                menorMedia = aluno.copy()

        print("Nome: ", menorMedia[0])

    elif opcao == 4:
        print("----ALUNO COM MAIOR MÉDIA FINAL (MF)----")
        menorMedia = alunos[0]

        for aluno in alunos:
            if aluno[4] < menorMedia[4]:
                menorMedia = aluno.copy()

        print("Nome: ", menorMedia[0])