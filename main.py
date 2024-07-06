# Definir soma entre dois números

def add(x, y):
    return x + y

# Definir subtração entre dois números


def subtract(x, y):
    return x - y

# Definir multiplicação entre dois números


def multiply(x, y):
    return x * y

# Definir divisão entre dois números


def divide(x, y):
    return x / y


# Funções para o usuário escolher
print("Selecione uma operação.")
print("1-Soma")
print("2-Subtração")
print("3-Multiplicação")
print("4-Divisão")

while True:
    # Seleciona o input do usuário
    choice = input(print("Escolha(1/2/3/4): "))

    # Chega a opção selecionada pelo usuário
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
        except ValueError:
            print("Input invalido. Por favor insira um NÚMERO.")
            continue
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    # Chegar se o usuário quer fazer outro calculo
    # E quebrar o loop caso ele escolha Não
    proximo_calculo = input("Você quer ir para o próximo calculo? (Sim/Não): ")
    if proximo_calculo == "Não":
        break
else:
    print("Número inválido")
