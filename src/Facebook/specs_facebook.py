from functions.Classes.Facebook import Facebook
import json


def logar_facebook():
  with open("src/Facebook/fixtures/pessoal.json") as f_login:
    data_login = json.load(f_login)


  Facebook.abrir_facebook()
  Facebook.maximizar_janela()
  Facebook.preencher_celular(data_login.get("celular"))
  Facebook.preencher_senha(data_login.get("senha"))
  Facebook.click_button_log_in()
  Facebook.validar_usuario()
  Facebook.go_pagina_inicial()
  Facebook.validar_url_pag_inicial()
  Facebook.mensagem_exito()  
  #
  # dFacebook.encerrar_sessao()


def logar_publicar_texto():
  with open("src/Facebook/fixtures/publicacoes.json") as f_publicacao:
    data_publi = json.load(f_publicacao)


  logar_facebook()
  Facebook.realizar_publicacao_textual(data_publi.get('publicacao1'))
  Facebook.mensagem_exito()
  Facebook.encerrar_sessao()

def mandar_mensagem_textual():
  with open("src/Facebook/fixtures/usuarios.json") as f_usuarios:
    data_users = json.load(f_usuarios)

  with open("src/Facebook/fixtures/mensagem.json") as f_mensagem:
    data_msgs = json.load(f_mensagem)

  logar_facebook()
  Facebook.pesquisar_usuario(data_users.get('Usuario1'))
  Facebook.click_usuario_pesquisado()
  Facebook.click_button_mensagem()
  Facebook.enviar_mensagem(data_msgs.get('mensagem1'))


# logar_facebook()
# logar_publicar_texto()

mandar_mensagem_textual()