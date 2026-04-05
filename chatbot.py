nome_bot: str = "Rodolfo"  # introdução do bot
print(f"{nome_bot}: Olá! eu sou o {nome_bot}! Como eu posso te auxiliar hoje?")


def iniciar_quiz():  # função pra começar o quiz
    perguntas = (f"{nome_bot}: Aonde meu criador mora? ",
                 f"{nome_bot}: Qual é o anime favorito do meu criador? ",
                 f"{nome_bot}: Qual é o nome do irmão do meu criador? ",
                 f"{nome_bot}: Qual é o sonho do meu criador? ",
                 f"{nome_bot}: Qual é o número mais aura?")

    opções = (("A. Vilhena", "B. Acre", "C. São Paulo", "D. Rio de Janeiro"),
              ("A. Jojo", "B. Jujutsu Kaisen", "C. Dragon Ball", "D. Demon Slayer"),
              ("A. Ronaldo", "B. Alberto", "C. Guilherme", "D. Matheus"),
              ("A. Trabalhar no tribunal", "B. Ser peão de gringo",
               "C. Farmar aura", "D. Comer muito bolo"),
              ("A. 123", "B. 61", "C. 67", "D. 0"))

    alternativas_corretas = ("A", "B", "D", "A", "C")
    chutes = []
    pontuacao = 0
    pergunta_atual = 0

    for pergunta in perguntas:
        print("-----------------------")
        print(pergunta)
        for opção in opções[pergunta_atual]:
            print(opção)

        chute: str = input(
            "Escolha sua alternativa: (A, B, C, D)").upper()
        chutes.append(chute)
        if chute == alternativas_corretas[pergunta_atual]:
            pontuacao += 1
            print(f"{nome_bot}: Você acertou!")
        else:
            print(f"{nome_bot}: Você errou..")
            print(
                f"{nome_bot}: A resposta correta era a alternativa: {alternativas_corretas[pergunta_atual]} ")

        pergunta_atual += 1

    print("-----------------------")
    print("     RESULTADOS:       ")
    print("-----------------------")

    print("Alternativas: ", end="")
    for alternativa in alternativas_corretas:
        print(alternativa, end=" ")
    print()

    print("Chutes: ", end="")
    for chute in chutes:
        print(chute, end=" ")
    print()

    pontuacao = int(pontuacao / len(perguntas) * 100)
    print(f"{nome_bot}: Sua pontuação foi de: {pontuacao}%")


while True:  # loop de dialogo com o chatbot/interações
    usuario_input: str = input("Você: ").lower()

    if usuario_input in ["oi", "olá", "eae", "oie", "opa"]:
        print(f"{nome_bot}: Oi! como eu posso te ajudar?")

    elif usuario_input in ["tchau", "adeus", "até outro dia", "até", "flw"]:
        print(f"{nome_bot}: Até logo!")
        break

    elif usuario_input in ["quiz", "Quiz", "jogar", "jogo"]:
        print(f"{nome_bot}: Perfeito! vamos jogar um quiz!")
        iniciar_quiz()

    elif usuario_input in ["somar", "calculadora", "calcular", "calculo"]:  # calculadora
        print(
            f"{nome_bot}: Beleza! vamos começar a calcular, qual operação você deseja efetuar?(+, -, /, *, %)")
        try:
            operacao = input("Você: ")
            if operacao not in ["+", "-", "*", "/", "%"]:
                print(f"{nome_bot}: Esse operador não existe!")
            else:
                print(f"{nome_bot}: Insira o primeiro número:")
                num1 = float(input("Você: "))
                print(f"{nome_bot}: Insira o segundo número:")
                num2 = float(input("Você: "))
                if operacao == "+":
                    resultado = num1 + num2
                elif operacao == "-":
                    resultado = num1 - num2
                elif operacao == "*":
                    resultado = num1 * num2
                elif operacao == "/":
                    resultado = num1 / num2
                elif operacao == "%":
                    resultado == num1 % num2
                print(
                    f"{nome_bot}: O resultado deste cálculo é igual a: {resultado}! ")

        except ValueError:
            print(
                f"{nome_bot}: Eita! parece que algo deu errado, por favor tente novamente!")
    else:
        print(f"{nome_bot}: Eu não entendi.. por favor tente novamente.")
