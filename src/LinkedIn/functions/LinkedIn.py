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
    time.sleep(1)


  def click_button_mensagens():
    driver.find_element_by_css_selector("#ember24 > span").click()
    time.sleep(2)


  def click_button_nova_mensagem():
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div/div/main/div/section[1]/div[1]/div[1]/a").click()
    time.sleep(2)


  def click_button_enviar_mensagem():
    driver.find_element_by_css_selector(".align-items-center > div:nth-child(1) > button").click()
    time.sleep(1)


  def click_button_enviar_mensagem_via_pesquisa():
    driver.find_element_by_css_selector("#ember43").click()

  
  def click_usuario_pesquisado():
    driver.find_element_by_css_selector("div.entity-result__content.pt3.pb3.t-12.t-black--light > div.t-roman.t-sans > div > span.entity-result__title-line.flex-shrink-1.entity-result__title-text--black > span > a > span > span:nth-child(1)").click()
    time.sleep(2)


  def click_button_enviar_msg_via_perfil():
    driver.find_element_by_css_selector(".pt2.display-flex > div > a").click()


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


  def pesquisar_usuario_via_pagina_inicial(usuario):
    driver.find_element_by_css_selector("#global-nav-typeahead > input").send_keys(usuario)
    time.sleep(1)
    driver.find_element_by_css_selector("#global-nav-typeahead > input").send_keys(Keys.ENTER)


  def pesquisar_usuario_via_mensagem(usuario):
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div/div/main/div/section[2]/div[1]/div[2]/section/div/input").send_keys(usuario)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div/div/main/div/section[2]/div[1]/div[2]/section/div/input").send_keys(Keys.ENTER)
    time.sleep(1)


  def enviar_mensagem_via_pesquisa(mensagem):
    driver.find_element_by_css_selector("#msg-form-ember82 > div.msg-form__msg-content-container.msg-form__message-texteditor.relative.flex-grow-1.display-flex > div > div.flex-grow-1 > div.msg-form__contenteditable.t-14.t-black--light.t-normal.flex-grow-1.full-height.notranslate").send_keys(mensagem)


  # Necessita de manutenção
  def enviar_mensagem_textual_via_mensagens(mensagem):
    driver.find_element_by_css_selector(".full-height.notranslate").send_keys(mensagem)


  def validar_url_pag_inicial():
    with open("src/LinkedIn/fixtures/urls.json") as f_urls:
      data_urls = json.load(f_urls)

    
    time.sleep(2)

    url_local = driver.current_url
    url_validar = data_urls.get('urlPaginaInicial')


    if url_local == url_validar:
      print(f'URL página inicial validada com sucesso: {url_local}')

    else:
      driver.quit()


  def validar_url_perfil_pessoal():
    with open("src/LinkedIn/fixtures/pessoal.json") as f_urls:
      data_urls = json.load(f_urls)


    url_local = driver.current_url
    url_validar = data_urls.get('url')


    if url_local == url_validar:
      print(f'URL perfil validada com sucesso: {url_local}')

    else:
      driver.quit()


  def encerrar_sessao():
    driver.quit()


  def mensagem_sucesso():
    print("Automação realizada com sucesso")