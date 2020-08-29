##Desenvolvido por Abilio com os conteúdos aprendidos nas aulas do curso Pythom Fundamentos.
#28-08-2020
#VERSÃO: 0.0.0.1
def calculadoraBasica():
    print('Seja bem vindo a Calculadora Simples')
    op=0
    teste = False#precisamos iniciar a variavel para fazermos a validação se for numero ou caractere
    
    #enquanto for diferente de 5 executa o loop
    while int(op) !=5:
    #inicialização de variável
        num1 = 0
        num2 = 0
        #menu
        op = input('\n 1 - Somar\n 2 - Subtração\n 3 - multiplicação\n 4 - divisão\n 5 - Sair\n')
        
        while teste == False:
            if not op.isdigit():
                teste = False
                print("Por favor digite um numero, você digitou uma letra ou simbolo!")
                op = input('\n 1 - Somar\n 2 - Subtração\n 3 - Multiplicação\n 4 - divisão\n 5 - Sair\n')#menu caso a pessoa tenha digitado uma letra
            else:
                teste=True#força a sair do loop e deixa continuar com o valor informado.
                
        if(int(op) ==1):#soma
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            result = int(num1)+int(num2)
            print("\n",num1,"+",num2,"=",result)#apenas para deixar mais bonito, poderia apenas ser o resultado.
            teste = False# fizemos para forçar a validação novamente se é uma string ou numero, ver linha 16
            
        elif(int(op) ==2):#Subtração
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            result = int(num1)-int(num2)
            print("\n",num1,'-',num2,'=',result)
            teste = False
        
        elif(int(op) ==3):#multiplicação
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            result = int(num1)*int(num2)
            print("\n",num1,"*",num2,"=",result)
            teste = False
        
        elif(int(op) ==4):#Divisão
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            result = float(num1)/float(num2)
            print("\n",num1,"/",num2,"=",result)
            teste = False
            
        elif(int(op) == 5):
            #print('Obrigado por usar o nosso sistema')
            return 'Obrigado por usar o nosso sistema'
        else:
            print('Opção inválida, por favor olhe o menu e digite umas das opções')
            teste = False
            

        
#Chamando a função Calculadora
calculadoraBasica()
