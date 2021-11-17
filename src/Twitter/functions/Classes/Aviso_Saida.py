import time

class Aviso_Saida():
  def saida():
    i = 5

    while i != 0:
      print(f'Saindo em: {i}')
      time.sleep(1)
      i -= 1