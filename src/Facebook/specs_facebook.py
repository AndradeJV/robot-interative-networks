from functions.Classes.Facebook import Facebook
import json


def logar_publicar_texto():
  with open("src/Facebook/fixtures/pessoal.json") as f_login:
    data_login = json.load(f_login)

  with open("src/Facebook/fixtures/publicacoes.json") as f_publicacao:
    data_publi = json.load(f_publicacao)


  Facebook.abrir_facebook()
  Facebook.maximizar_janela()
  Facebook.preencher_celular(data_login.get("celular"))
  Facebook.preencher_senha(data_login.get("senha"))
  Facebook.click_button_log_in()
  Facebook.validar_usuario()
  Facebook.go_pagina_inicial()
  Facebook.validar_url_pag_inicial()
  Facebook.realizar_publicacao_textual(data_publi.get('publicacao1'))
  Facebook.click_button_publicar()
  Facebook.encerrar_sessao()
  Facebook.mensagem_exito()

logar_publicar_texto()