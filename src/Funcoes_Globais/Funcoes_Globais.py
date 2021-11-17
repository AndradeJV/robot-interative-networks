from selenium import webdriver
import time

driver = webdriver.Chrome()


class Funcoes_Globais:
  def maximizar_janela():
    time.sleep(1)
    driver.maximize_window()

  def sair():
    i = 5

    while i != 0:
      print(f'Saindo em: {i}')
      time.sleep(1)
      i -= 1