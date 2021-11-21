from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome()

class LinkedIn():
  def abrir_linkedin():
    driver.get("https://www.linkedin.com/")
    time.sleep(1)


  def maximizar_janela():
    driver.maximize_window()


  def click_button_login():
    driver.find_element_by_css_selector(".babybear\:pt-\[24px\] > div > div > form > button").click()


  def preencher_email(email):
    driver.find_element_by_css_selector("#session_key").send_keys(email)
    time.sleep(2)

  def preencher_celular(celular):
    driver.find_element_by_css_selector("#session_key").send_keys(celular)
    time.sleep(2)


  def preencher_senha(senha):
    driver.find_element_by_css_selector("#session_password").send_keys(senha)
    time.sleep(1)


  def acessar_perfil_pessoal():
    driver.find_element_by_css_selector("div.t-16.t-black.t-bold").click()
    time.sleep(1)


  def go_to_pagina_inicial():
    driver.find_element_by_css_selector("#ember18").click()
    time.sleep(1)


  def validar_url_pag_inicial():
    with open("src/LinkedIn/fixtures/urls.json") as f_urls:
      data_urls = json.load(f_urls)

    
    time.sleep(2)

    url_local = driver.current_url
    url_validar = data_urls.get('urlPaginaInicial')


    if url_local == url_validar:
      print(f'URL validada com sucesso: {url_local}')

    else:
      driver.quit()


  def validar_url_perfil_pessoal():
    with open("src/LinkedIn/fixtures/pessoal.json") as f_urls:
      data_urls = json.load(f_urls)


    url_local = driver.current_url
    url_validar = data_urls.get('url')


    if url_local == url_validar:
      print(f'URL validada com sucesso: {url_local}')

    else:
      driver.quit()


  def encerrar_sessao():
    driver.quit()


  def mensagem_sucesso():
    print("Automação realizada com sucesso")