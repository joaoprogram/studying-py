print('Digite seu nome: ', end='')
name = input()

print('Digite seu CPF: ', end='')
cpf = input()

if len(cpf) != 11:
        print('Digite outro cpf')
        cpf = input()
    
print('Digite seu salário: ', end='')
salario = int(input())

aumento = salario + (salario*0.35)
print('Seu aumento será de:', aumento)