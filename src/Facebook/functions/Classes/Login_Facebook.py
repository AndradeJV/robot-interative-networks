from selenium import webdriver
import time
import json

driver = webdriver.Chrome()


class Login_Facebook:
  def click_button_log_in():
    driver.find_element_by_name("login").click()
    time.sleep(5)


  def abrir_facebook():
    driver.get("https://www.facebook.com/")
    time.sleep(1)


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
    driver.find_element_by_css_selector(".k4urcfbm.qv66sw1b > span").click()

    time.sleep(4)
    iframe = driver.find_element_by_css_selector(".du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div")
    driver.switch_to.frame(iframe)

    time.sleep(2)
    driver.find_element_by_css_selector("._5rpb > div > div > div > div").send_keys(texto)


  def encerrar_sessao():
    driver.quit()

  