ficha = []

while True:
    dados = []

    nome = str(input('Digite o nome: ')).strip()
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))

    media = (n1+n2)/2

    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    dados.append(media)

    continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida ! Digite [S] para SIM e [N] para não. Deseja continuar ? [S/N]: '))
    if continuar == 'N':
        ficha.append(dados[:])
        break
    else:
        ficha.append(dados[:])

print('='*40)
print(f'{"Nº":<5}{"NOME":<20}{"MÉDIA":>10}')
print('-'*40)
for pos in range(len(ficha)):
    print(f'{pos:<5}{ficha[pos][0]:<20}{ficha[pos][3]:>10}')
print('-'*40)
notas = int(input('Deseja mostrar as notas de qual aluno?[999 interrompe]: '))
while notas != 999:
    if notas < 0 or notas >= len(ficha):
        notas = int(input('Erro ! Digite um dos números dos alunos ou 999 para sair !: '))
    else:
        print(f'Notas de {ficha[notas][0]} são: {ficha[notas][1], ficha[notas][2]}')
        notas = int(input('Deseja mostrar as notas de qual aluno?[999 interrompe]: '))
if notas == 999:
    print('Obrigado por utilizar o programa ! :)')