from functions.Classes.Login_Facebook import Login_Facebook as lg_fb
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
  lg_fb.click_button_publicar()
  lg_fb.encerrar_sessao()
  lg_fb.mensagem_exito()

login_usuario_facebook()