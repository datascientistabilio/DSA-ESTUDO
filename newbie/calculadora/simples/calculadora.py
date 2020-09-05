##Desenvolvido por Abilio com os conteúdos aprendidos nas aulas do curso Pythom Fundamentos.
#28-08-2020
#VERSÃO: 0.0.0.3
def calculadoraBasica():
    print('Seja bem vindo a Calculadora Simples')
    op=0
    
    #enquanto for diferente de 5 executa o loop
    while int(op) !=5:
    #inicialização de variável
        num1 = 0
        num2 = 0
        #menu
        #Não converto neste momento, pois preciso ter certeza que o valor é um numero, então eu recebo valor e faço a verificação com a função validacao()
        op = input('\n 1 - Somar\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Sair\n')
        
        #validação para tratar se é um numero ou string
        op = validacao(op)
                
        if(int(op) ==1):#soma
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            
            result = int(num1)+int(num2)
            print("\n",num1,"+",num2,"=",result)#apenas para deixar mais bonito, poderia apenas ser o resultado.
            
        elif(int(op) ==2):#Subtração
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            
            result = int(num1)-int(num2)
            print("\n",num1,'-',num2,'=',result)
           
        elif(int(op) ==3):#multiplicação
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            
            result = int(num1)*int(num2)
            print("\n",num1,"*",num2,"=",result)
           
        elif(int(op) ==4):#Divisão
            num1 = input('Digite o primeiro numero ')
            num2 = input('\nDigite o segundo numero')
            
            if int(num2) == 0:#pequena validação para saber se a pessoa não vai querer dividir por zero.
                print('Você não pode dividir por zero')
            else:
                result = float(num1)/float(num2)
                print("\n",num1,"/",num2,"=",result)
            
        elif(int(op) == 5):
            return 'Obrigado por usar o nosso sistema'
        else:
            print('Opção inválida, por favor olhe o menu e digite umas das opções')
            
def validacao(num):
    teste = False#precisamos iniciar a variavel para fazermos a validação se for numero ou caractere
    
    while teste == False:
            if not num.isdigit():
                
                print("Por favor digite um numero, você digitou uma letra ou simbolo!")
                num = input('\n 1 - Somar\n 2 - Subtração\n 3 - Multiplicação\n 4 - divisão\n 5 - Sair\n')#menu caso a pessoa tenha digitado uma letra
            else:
                teste=True#força a sair do loop e deixa continuar com o valor informado.
                return num
            
            
#Chamando a função Calculadora
calculadoraBasica()
