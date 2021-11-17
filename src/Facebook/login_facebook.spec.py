from functions.Classes.Login_Facebook import Login_Facebook as lg_fb
#from ..Funcoes_Globais.Funcoes_Globais import Funcoes_Globais
import json


def login_usuario_facebook():
  with open("src/Facebook/fixtures/pessoal.json") as f_login:
    data_login = json.load(f_login)

  with open("src/Facebook/fixtures/publicacoes.json") as f_publicacao:
    data_publi = json.load(f_publicacao)


  lg_fb.abrir_facebook()
  lg_fb.maximizar_janela()
  lg_fb.preencher_celular(data_login.get("celular"))
  lg_fb.preencher_senha(data_login.get("senha"))
  lg_fb.click_button_log_in()
  lg_fb.validar_usuario()
  lg_fb.go_pagina_inicial()
  lg_fb.validar_url_pag_inicial()
  lg_fb.realizar_publicacao_textual(data_publi.get('publicacao1'))
  #lg_fb.encerrar_sessao()

  #Funcoes_Globais.sair()

login_usuario_facebook()