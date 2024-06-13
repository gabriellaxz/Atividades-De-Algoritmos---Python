def add(x, y):
    """Função para adicionar dois números"""
    return x + y

def subtract(x, y):
    """Função para subtrair dois números"""
    return x - y

def multiply(x, y):
    """Função para multiplicar dois números"""
    return x * y

def divide(x, y):
    """Função para dividir dois números"""
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    while True:
        # Recebe a entrada do usuário
        opcao = input("Digite a escolha(1/2/3/4): ")
        
        # Verifica se a escolha é uma das opções válidas
        if opcao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
                
            elif opcao == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
                
            elif opcao == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
                
            elif opcao == '4':
                result = divide(num1, num2)
                if result == "Erro! Divisão por zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
                    
            # Verifica se o usuário deseja realizar outra operação
            next_calculation = input("Deseja realizar outra operação? (s/n): ")
            if next_calculation.lower() != 's':
                break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    calculadora()