from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class Definitions():
  def __init__(self):
    options = Options()
    options.headless = True
    self.browser = webdriver.Firefox(options=options)
    self.url = "https://dle.rae.es/"

  def get_definition(self, word:str) -> dict[str, list[str]]:
    self.browser.get(self.url + word)
    definition = self.browser.find_elements(By.XPATH,
      "//div[@id='resultados']/article/p[not(@class='n5') and not(starts-with(@class, 'l'))]")
    phrases = self.browser.find_elements(By.XPATH,
      "//div[@id='resultados']/article/p[starts-with(@class, 'l')]")
    acepciones = []
    frases = []
    for acepcion in definition:
      acepciones.append(acepcion.text)
    for phrase in phrases:
      frases.append(phrase)
    self.browser.close()
    return {
      "acepciones": acepciones,
      "frases": frases,
    }
