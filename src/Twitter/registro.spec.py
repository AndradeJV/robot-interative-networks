import json
from functions.Classes.Registro import Registro
from selenium import webdriver

driver = webdriver.Chrome()
# .r-1dqxon3 > div

def registrar_usuario_twitter():
  with open("src/Twitter/fixtures/registro/registro.teste.json") as f_login:
    data_login = json.load(f_login)


  Registro.abrir_twitter()
  Registro.click_registrar()

  iframe = driver.find_element_by_css_selector(".r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu")
  driver.switch_to_frame(iframe)

  Registro.preencher_nome(data_login.get("nome"))
  Registro.click_preencher_com_email()
  Registro.click_preencher_com_email(data_login.get("email"))
  Registro.preencher_dia_nascimento(data_login.get("diaNascimento"))
  Registro.preencher_mes_nascimento(data_login.get("mesNascimento"))
  Registro.preencher_ano_nascimento(data_login.get("anoNascimento"))
  Registro.click_button_next()


registrar_usuario_twitter()