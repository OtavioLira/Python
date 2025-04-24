import requests

# Configuração da API
API_KEY = "Sua Chave"  # Substitua pela sua chave da API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obter_clima(cidade):
    """
    Faz uma requisição à API OpenWeather para obter informações do clima de uma cidade.

    Args:
        cidade (str): Nome da cidade.

    Returns:
        dict: Dicionário contendo descrição do clima e temperatura em Celsius.
    """
    try:
        # Monta o endpoint com os parâmetros necessários
        params = {
            "q": cidade,
            "appid": API_KEY,
            "lang": "pt_br",  # Idioma da resposta
            "units": "metric"  # Retorna a temperatura em Celsius
        }
        # Faz a requisição
        resposta = requests.get(BASE_URL, params=params)
        resposta.raise_for_status()  # Lança uma exceção para códigos de status HTTP de erro

        # Processa a resposta
        dados = resposta.json()
        descricao = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]

        return {
            "descricao": descricao,
            "temperatura": temperatura
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None
    except KeyError:
        print("Erro ao processar os dados da resposta.")
        return None

def exibir_clima(cidade):
    """
    Exibe as informações do clima de uma cidade.

    Args:
        cidade (str): Nome da cidade.
    """
    clima = obter_clima(cidade)
    if clima:
        print(f"Clima em {cidade}:")
        print(f"Descrição: {clima['descricao']}")
        print(f"Temperatura: {clima['temperatura']}°C")
    else:
        print("Não foi possível obter as informações do clima.")

# Exemplo de uso
if __name__ == "__main__":
    while True:
        cidade = input("Digite o nome da cidade (ou 'sair' para encerrar): ")
        if cidade.lower() == 'sair':
            break
        exibir_clima(cidade)