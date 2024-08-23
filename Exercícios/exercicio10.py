## 10. Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18.

idade = int(input('Digite a sua idade \n'))

if idade >=18:
    print('Maior de idade')
elif idade <18:
    print('Menor de idade')
elif idade <=0:
    print('Idade inexistente')
    

