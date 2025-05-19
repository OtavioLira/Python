"""
Automação Web com Python
# requisitos:
# - Python
# - Selenium
# - Baixar  webdriver para o navegador a ser usado, ex: chromedriver, geckodriver,

# imports
# !pip install selenium

Objetivo: baixar o Demonstrativo de Resultados da Magazine Luiza
Passo 1: Entrar em "https://ri.magazineluiza.com.br/"
Passo 2: Clicar em "informações financeiras"
Passo 3: Clicar em "Planilha de Resultado"
Passo 4: Clicar em "Planilha de resultados Trimestrais"
Passo 5: Clicar em "salvar"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Configuração para o chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #Não fechar após executar os comandos
chrome_options.add_argument("--kiosk") #tela cheia

# Abrir o navegador
navegador = webdriver.Chrome(options=chrome_options)

navegador.get("https://ri.magazineluiza.com.br/") # Navegar - Passo 1

elemento_informacoes = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Form1"]/header/div/div/div/div[2]/ul/li[3]/a')) # Espera o elemento ser encontrado
)
elemento_informacoes.click() #Clique

elemento_link_para_planilha = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#Form1 > div.desktop-menu.active > div > div > div > div > ul:nth-child(3) > li:nth-child(2) > a'))
)
elemento_link_para_planilha.click()

elemento_baixar_planilha = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, 'QkuLGwWq7MtNAgC4qqZQKg=='))
)
elemento_baixar_planilha.click()