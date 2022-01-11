from rae.rae import Definitions

def test_definitions_not_empty():
  rae = Definitions()
  polimorfismo = rae.get_definition('polimorfismo')
  assert len(polimorfismo['acepciones']) >= 1
