from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    """ Uma pesquisa que estará disponível para todas as funções de teste. """
    question = "Qual língua você aprendeu a falar pela primeira vez?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """ Testa se uma única resposta é armazenada corretamente. """
    language_survey.store_response('English')

    assert "English" in language_survey.responses

def test_store_multiple_responses(language_survey):
    """ Testa se três respostas são armazenadas corretamente. """
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
