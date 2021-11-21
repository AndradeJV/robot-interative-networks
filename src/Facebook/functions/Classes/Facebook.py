from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome()


class Facebook:
  def abrir_facebook():
    driver.get("https://www.facebook.com/")
    time.sleep(1)

  def click_button_log_in():
    driver.find_element_by_name("login").click()
    time.sleep(5)
    
  
  def click_button_publicar():
    driver.find_element_by_css_selector(".bp9cbjyn > div > div > div.bp9cbjyn.j83agx80.taijpn5t.c4xchbtz.by2jbhx6.a0jftqn4").click()


  def click_usuario_pesquisado():
    time.sleep(1)
    driver.find_element_by_css_selector("#dir_nav_sts\:100013089223359 > div > a > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.p8fzw8mz.pcp91wgn.iuny7tx3.ipjc6fyt").click()
    time.sleep(2)

  def click_button_mensagem():
    driver.find_element_by_css_selector(".h374gqy3 > div > div > div:nth-child(2) > div > div > div").click()
    time.sleep(2)


  def preencher_email(email):
    driver.find_element_by_id("email").send_keys(email)
    time.sleep(1)


  def preencher_celular(celular):
    driver.find_element_by_id("email").send_keys(celular)
    time.sleep(1)


  def preencher_senha(senha):
    driver.find_element_by_id("pass").send_keys(senha)
    time.sleep(1)


  def maximizar_janela():
    driver.maximize_window()


  def validar_usuario():
    with open("src/Facebook/fixtures/pessoal.json") as f_login:
      data_login = json.load(f_login)
    
    url_perfil = data_login['urlPerfil']
    usuario_perfil = data_login['usuario']

    driver.find_element_by_css_selector(".q5xnexhs > a > span > span").click()
    time.sleep(4)

    validacao_url_perfil_fb = driver.current_url
   
    print(f'URL do perfil: {url_perfil}')
    print(f'URL para validar: {validacao_url_perfil_fb}')


    if url_perfil == validacao_url_perfil_fb:
      print(f'Usuario: {usuario_perfil} validado com sucesso')
    
    else:
      driver.quit()


  def go_pagina_inicial():
    driver.find_element_by_css_selector("li:nth-child(1) > span > div > a > span > svg").click()
    time.sleep(2)
    driver.find_element_by_css_selector("li:nth-child(1) > span > div > a > span > svg").click()
    time.sleep(2)


  def validar_url_pag_inicial():
    with open("src/Facebook/fixtures/urls.json") as f_urls:
      data_urls = json.load(f_urls)

    url_pagina_inicial = data_urls['paginaInicial']

    validacao_pagina_inicial_fb = driver.current_url

    time.sleep(4)
    print(f'URL página inicial: {validacao_pagina_inicial_fb}')


    if url_pagina_inicial == validacao_pagina_inicial_fb:
      print(f'Validação pagina inicial feita com sucesso')

    else:
      driver.quit()

  def realizar_publicacao_textual(texto):
    time.sleep(2)
    driver.find_element_by_css_selector(".k4urcfbm.qv66sw1b > span").click()
    time.sleep(2)
    driver.find_element_by_css_selector("._5rpb > div > div > div > div").send_keys(texto)

  def pesquisar_usuario(usuario):
    driver.find_element_by_css_selector("label > input").send_keys(usuario)
    time.sleep(2)

  def enviar_mensagem(mensagem):
    driver.find_element_by_css_selector("div._5rpb > div > div > div > div").send_keys(mensagem)
    time.sleep(2)
    driver.find_element_by_css_selector("div._5rpb > div > div > div > div").send_keys(Keys.ENTER)
    time.sleep(2)

  def mensagem_exito():
    print("Automação realizada com sucesso")

  def encerrar_sessao():
    driver.quit()

  