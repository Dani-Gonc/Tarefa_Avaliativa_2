#[nome, [T1,T2], [P1,P2],[MT,MP],MF]

alunos = []

print("----SISTEMA ESCOLAR----")
quantAlunos = int(input("Quantos alunos serão cadastrados: "))

for i in range(quantAlunos):
    aluno = [] #Pra cada aluno cria um lista "aluno"

    aluno.append(input("Digite o nome do aluno: ")) #Pede o nome do aluno e armazena como o primeiro item da lista aluno.

    notasT = [] #Cria uma lista chamada notasT para armazenar as duas provas teóricas T1 e T2. Adiciona a lista à lista do aluno.
    notasT.append(float(input("Digite a nota T1: ")))
    notasT.append(float(input("Digite a nota T2: ")))
    aluno.append(notasT)

    notasP = [] #Cria uma lista chamada notasP para armazenar as duas provas práticas P1 e P2. Adiciona a lista à lista do aluno.
    notasP.append(float(input("Digite a nota P1: ")))
    notasP.append(float(input("Digite a nota P2: ")))
    aluno.append(notasP)

    medias = [ #Cria uma lista chamada medias para armazenar as médias teórica e prática. Adiciona a lista à lista do aluno.
        notasT[0] * 0.4 + notasT[1] * 0.6,
        (notasP[0] + notasP[1]) / 2
    ]
    aluno.append(medias)

    if medias[0] > 5 and medias[1] > 5:
        mediaF = medias[1] * 0.3 + medias[0] * 0.7  # MP * 0.3 + MT * 0.7
    else:
        mediaF = min(medias[0], medias[1])  # menor entre MT e MP

    aluno.append(mediaF)
    alunos.append(aluno)

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
        maiorMedia = alunos[0] #maiorMedia é o primeiro aluno da lista alunos

        for aluno in alunos:
            if aluno[4] > maiorMedia[4]: #Se a média do aluno for maior que a média do maiorMedia, o aluno se torna o novo maiorMedia.
                maiorMedia = aluno.copy()

        print("Nome: ", maiorMedia[0])

    elif opcao == 4:
        print("----ALUNO COM MENOR MÉDIA FINAL (MF)----")
        menorMedia = alunos[0]

        for aluno in alunos:
            if aluno[4] < menorMedia[4]:
                menorMedia = aluno.copy()

        print("Nome: ", menorMedia[0])
    
    elif opcao == 5:
        print("----PERCENTUAL DE ALUNOS COM MF > 5.0----")
        total = len(alunos)
        acima5 = 0

        for aluno in alunos:
            if aluno[4] > 5:
                acima5 += 1

        percentual = (acima5 / total) * 100
        print(f"{percentual:.2f}% dos alunos têm MF maior que 5.0")

    elif opcao == 6:
        print("----encerrando sistema----")
        break
