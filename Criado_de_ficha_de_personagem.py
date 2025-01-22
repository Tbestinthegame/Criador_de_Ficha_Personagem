cont = 0
#Caracteristicas do personagem
while cont == 0:
    nome = str(input('Digite o nome ou alcunha do personagem:'))
    carac = str(input('Digite a personalidade do personagem:'))
    condicoes = str(input('Digite que itens o personagem carrega:'))
    tormentos = str(input('Digite os traumas do personagem:'))
    resposta = int(input('Deseja salvar essa ficha ou deseja alterá-la?[1 para salvar e 0 para alterar]:'))

#Ifs de acordo com a opção do usuário
    if resposta == 1:
        cont = 1
    elif resposta == '0':
        cont = 0

#Caso o usuário digite algo fora das opções disponíveis
    while resposta != 0 and resposta != 1:
        print("Digite uma resposta valida!")
        resposta = int(input('Deseja salvar essa ficha ou deseja alterá-la?[1 para salvar e 0 para alterar]:'))
        if resposta == 1:
            cont = 1
        elif resposta == '0':
            cont = 0

#formato do arquivo
formato = '.txt'
#qubra de linha para separar os campos
quebra = "\n"

#O arquivo é primeiro aberto no modo write para depois adcionar usando o append
arquivo = open(nome + formato, 'w')
escrever = arquivo.write("*Nome: " + nome + quebra)
arquivo = open(nome + formato, 'a')
escrever2 = arquivo.write("*Caracteristicas: " + carac + quebra)
escrever3 = arquivo.write("*Condiçoes: " + condicoes + quebra)
escrever4 = arquivo.write("*tormentos: " + tormentos + quebra)
print("Pronto! A ficha de personagem foi criada!")
arquivo.close()

