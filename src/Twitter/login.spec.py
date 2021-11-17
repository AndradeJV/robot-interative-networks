from functions.Classes.Login import Login
from ..Funcoes_Globais.Funcoes_Globais import Funcoes_Globais
import json


def login_usuario_twitter():
    with open("src/Twitter/fixtures/login/pessoal.json") as f_login:
        data_login = json.load(f_login)

    with open("src/Twitter/fixtures/geral/tweets.json") as f_tweets:
        data_tweets = json.load(f_tweets)
    
    Login.abrir_twitter()
    Funcoes_Globais.maximizar_janela()
    Login.click_logar()
    Login.inserir_usuario(data_login.get('login'))
    Login.inserir_senha(data_login.get('senha'))
    Login.realizar_tweet(data_tweets.get('tweetTres'))
    Funcoes_Globais.sair()

login_usuario_twitter()