from functions.Classes.Registro import Registro
from ..Funcoes_Globais.Funcoes_Globais import Funcoes_Globais
import json


def registrar_usuario_twitter():
  with open("src/Twitter/fixtures/registro/registro.teste.json") as f_login:
    data_login = json.load(f_login)


  Registro.abrir_twitter()
  Funcoes_Globais.maximizar_janela()
  Registro.click_registrar()
  Registro.acessar_iframe()
  Registro.preencher_nome(data_login.get("nome"))
  Registro.click_preencher_com_email()
  Registro.click_preencher_com_email(data_login.get("email"))
  Registro.preencher_dia_nascimento(data_login.get("diaNascimento"))
  Registro.preencher_mes_nascimento(data_login.get("mesNascimento"))
  Registro.preencher_ano_nascimento(data_login.get("anoNascimento"))
  Registro.click_button_next()
  Funcoes_Globais.sair()


registrar_usuario_twitter()