from rae.rae import Definitions
import pytest

@pytest.fixture
def palabra_menester():
  rae = Definitions()
  return rae.get_definition('menester')

def test_acepciones_not_empty(palabra_menester):
  assert len(palabra_menester[0]['acepciones']) >= 1

def test_ethymology(palabra_menester):
  assert palabra_menester[0]['etimologia'] == "Del lat. ministerium 'servicio', 'oficio'."
