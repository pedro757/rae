from rae.rae import Definitions, Raiz
import pytest

@pytest.fixture
def palabra_menester() -> list[Raiz]:
  rae = Definitions()
  return rae.get_definition('menester')

def test_acepciones_not_empty(palabra_menester):
  assert len(palabra_menester[0]['acepciones']) >= 1

def test_definition(palabra_menester):
  acepciones = palabra_menester[0]['acepciones']
  assert acepciones[0] == "1. m. Falta o necesidad de algo."
  assert acepciones[1] == "2. m. Oficio u ocupación habitual U. m. en pl."
  assert acepciones[2] == "3. m. pl. Necesidades fisiológicas."

def test_ethymology(palabra_menester):
  assert palabra_menester[0]['etimologia'] == "Del lat. ministerium 'servicio', 'oficio'."
