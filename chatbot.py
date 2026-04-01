nome_bot: str = "Rodolfo"  # introdução do bot
print(f"{nome_bot}: Olá! eu sou o {nome_bot}! Como eu posso te auxiliar hoje?")


def iniciar_quiz():  # função pra começar o quiz
    pontuação = 0

    # pergunta_1
    print(f"{nome_bot}: Onde meu criador mora?")
    usuario_resposta1: str = input("Você: ").lower()
    if usuario_resposta1 in ["Vilhena", "vilhena"]:
        print(f"{nome_bot}: Você acertou!")
        pontuação += 1
    else:
        print(f"{nome_bot}: Você errou..")

    # pergunta 2
    print(f"{nome_bot}: Próxima pergunta, qual é o nome do cara mais lindo do mundo?")
    usuario_resposta2: str = input("Você: ").lower()
    if usuario_resposta2 in ["Miguel", "miguel", "damonrius"]:
        print(f"{nome_bot}: Você acertou! boa mlk")
        pontuação += 1
    else:
        print(f"{nome_bot}: Errou burro")

    # pergunta 3
    print(f"{nome_bot}: Agora a última pergunta.. qual é o anime favorito do meu criador?")
    usuario_resposta3: str = input("Você: ").lower()
    if usuario_resposta3 in ["Jujutsu", "jujutsu", "jujutsu kaisen", "Jujutsu Kaisen"]:
        print(f"{nome_bot}: Acertou seu danado!")
        pontuação += 1
    else:
        print(f"{nome_bot}: Errou animal")

    if pontuação == 3:  # quantos pontos você fez
        print(
            f"{nome_bot}: Parabéns! você terminou o quiz com {pontuação} pontos! seu GÊNIO!")
    elif pontuação == 2:
        print(
            f"{nome_bot}: Nada mal! você terminou o quiz com {pontuação} pontos! seu safado")
    elif pontuação == 1:
        print(
            f"{nome_bot}: Você terminou o quiz com apenas {pontuação} ponto.. foi bem ruim")
    elif pontuação == 0:
        print(
            f"{nome_bot}: Você é muito burro, tu terminou o quiz com {pontuação} pontos.. jamanta")


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
