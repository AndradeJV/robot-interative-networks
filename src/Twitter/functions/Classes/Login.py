from selenium import webdriver
import time

driver = webdriver.Chrome()


class Login:
  def abrir_twitter():
    driver.get("https://twitter.com/")
    time.sleep(2)
  
  def click_logar():
    driver.find_element_by_css_selector(".r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0 > span > span").click()
    driver.find_element_by_css_selector("a > div").click()
    time.sleep(3)

  def inserir_usuario(usuario):
    driver.find_element_by_css_selector("div > input").send_keys(usuario)
    time.sleep(1)
    driver.find_element_by_css_selector(".r-ttdzmv > div > div").click()

  def inserir_senha(senha):
    time.sleep(1)
    driver.find_element_by_css_selector("div > input").send_keys(senha)
    time.sleep(1)
    driver.find_element_by_css_selector(".r-ttdzmv > div > div > div").click()

  def realizar_tweet(mensagem):
    time.sleep(3)
    driver.find_element_by_css_selector(".DraftEditor-editorContainer > div > div > div > div").send_keys(mensagem)
    driver.find_element_by_css_selector(".r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span").click()
