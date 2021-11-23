from functions.LinkedIn import LinkedIn as lk
import json


def logar_linkedin():
  with open("src/LinkedIn/fixtures/pessoal.json") as f_login:
    data_login = json.load(f_login)

  lk.abrir_linkedin()
  lk.maximizar_janela()
  lk.preencher_email(data_login.get('email'))
  lk.preencher_senha(data_login.get('senha'))
  lk.click_button_login()
  lk.validar_url_pag_inicial()
  lk.acessar_perfil_pessoal()
  lk.validar_url_perfil_pessoal()
  lk.go_to_pagina_inicial()
  lk.validar_url_pag_inicial()


def enviar_mensagem():
  logar_linkedin()
  lk.pesquisar_usuario_via_pagina_inicial("Isabelly Vitorino")
  lk.click_usuario_pesquisado()
  lk.click_button_enviar_msg_via_perfil()
  lk.enviar_mensagem_via_pesquisa("Teste automatizado")
  # lk.click_button_enviar_mensagem()
  lk.click_button_enviar_mensagem()


enviar_mensagem()


lk.encerrar_sessao()
lk.mensagem_sucesso()
