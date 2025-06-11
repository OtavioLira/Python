class AnonymousSurvey:
    """ Coleta respostas anônimas para uma pergunta de pesquisa. """
    
    def __init__(self, question):
        """ Armazena uma pergunta e prepara para armazenar respostas. """
        self.question = question
        self.responses = []

    def show_question(self):
        """ Mostra a pergunta. """
        print(self.question)

    def store_response(self, new_response):
        """ Armazena uma única resposta. """
        self.responses.append(new_response)

    def show_results(self):
        """ Mostra todas as respostas fornecidas. """
        print("Respostas: ")
        for response in self.responses:
            print(f"- {response}")