__version__ = '0.1.0'
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, jsonify
from flask_restful import Api, Resource
import pandas as pd
import numpy

app = Flask(__name__)
api = Api(app)

options = Options()
options.headless = True

class words_bulk(Resource):
  def get(self):
    columns = numpy.array(["word", "meaning", "examples", "url"])
    words = pd.read_csv('palabras.csv', names=columns,
      dtype={'word': 'str', 'meaning': 'str', 'examples': 'str', 'url': 'str' })
    browser = webdriver.Firefox(options=options)
    for row in words.itertuples():
      url = "https://dle.rae.es/" + getattr(row, "word")
      browser.get(url)
      lines = browser.find_elements(By.XPATH,
        "//div[@id='resultados']/article/p[not(@class='n5') and not(starts-with(@class, 'l'))]")
      examples = browser.find_elements(By.XPATH, "//div[@id='resultados']/article/p[starts-with(@class, 'l')]")
      meaning = ""
      eg = ""
      for line in lines:
        if 'De' == line.text[0:2]:
          if line.text == lines[0].text:
            meaning = meaning + line.text + "\n"
          else:
            meaning = meaning + "\n" + line.text + "\n"
        if line.text[0].isnumeric():
          breakline = "\n" if line.text != lines[-1].text else ""
          meaning = meaning + line.text + breakline
      words.at[getattr(row, "Index"), 'meaning'] = meaning
      for ex in examples:
        eg = eg + ex.text + "\n"
      words.at[getattr(row, "Index"), 'examples'] = eg
      words.at[getattr(row, "Index"), 'url'] = url
    browser.close()
    words.to_csv('definiciones.csv', header=False, index=False, line_terminator='←', sep='↓')
    return jsonify('ok')

api.add_resource(words_bulk, '/words')

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug = True)
