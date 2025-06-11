from survey import AnonymousSurvey

# Define uma pergunta e faz uma pesquisa anônima
question = "Qual língua você aprendeu a falar pela primeira vez?"
language_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas
language_survey.show_question()
print("Digite 'q' a qualquer momento para sair.")
while True:
    response = input("Linguagem: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Mostra os resultados da pesquisa
print("\nObrigado por participar da pesquisa!")
language_survey.show_results()