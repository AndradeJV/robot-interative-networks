from selenium import webdriver
from .Aviso_Saida import Aviso_Saida
import time

driver = webdriver.Chrome()


class Registro:

  def click_registrar():
    driver.find_element_by_css_selector("a > div").click()
    time.sleep(1)

  def click_preencher_com_email():
    driver.find_element_by_css_selector(".r-1wzrnnt.r-bcqeeo.r-qvutc0 > span").click()
    time.sleep(1)

  def click_button_next():
    driver.find_element_by_css_selector(".r-ttdzmv.r-1xcajam.r-zchlnj > div > div").click()
    time.sleep(3)

  def abrir_twitter():
    driver.get("https://twitter.com/")
    time.sleep(2)

  def preencher_nome(nome):
    driver.find_element_by_class_name("name").send_keys(nome)
    time.sleep(1)

  def preencher_celular(celular):
    driver.find_element_by_class_name("phone_number").send_keys(celular)
    time.sleep(1)

  def preencher_email(email):
    driver.find_element_by_class_name("email").send_keys(email)
    time.sleep(1)

  def preencher_dia_nascimento(dia):
    driver.find_element_by_id("#SELECTOR_2").send_keys(dia)
    time.sleep(1)

  def preencher_mes_nascimento(mes):
    driver.find_element_by_id("#SELECTOR_1").send_keys(mes)
    time.sleep(1)

  def preencher_ano_nascimento(ano):
    driver.find_element_by_id("#SELECTOR_3").send_keys(ano)
    time.sleep(1)