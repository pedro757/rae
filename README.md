# RAE spanish dictionary
A scrapping implementation of selenium for the spanish official dictionary

## Getting Started

### Installation

`pip install rae`

### Basic Usage

```python
from rae import Definitions

rae = Definitions()

word = rae.get_definition('hastiar')

print(word)
```

It will print out something like this:

```js
[{
  'etimologia': 'Del lat. fastidiāre.',
  'acepciones': [
    '1. tr. Causar hastío. U. t. c. prnl.'
  ]
}]
```

## Documentation

The Definition class contains the following methods:

### get_definition(`word: str`) -> `list[origins]`:

Get the definition of the word provided from the official spanish dictionary, like RAE, this method
will output the results in a list of origins for the word provided.

Look at this word for example. For the spanish word `placar` there are three
origins based on the ethymology, one from latin and the other two from french

```js
[
  {
    'etimologia': 'Del lat. placāre.',
    'acepciones': [
      '1. tr. desus. Aplacar, calmar, apaciguar.'
    ]
  }, {
    'etimologia': 'Del fr. plaquer.',
    'acepciones': [
      '1. tr. Dep. En rugby, detener un ataque, sujetando con las manos al
        contrario y forzándolo a abandonar el balón.'
    ]
  }, {
    'etimologia': 'Del fr. placard.',
    'acepciones': [
      '1. m. Arg. y Ur. armario empotrado.'
    ]
  }
]
```

## Contribuiting
Bug reports, feature suggestions and especially code contributions are welcome. You open a GitHub issue or pull
request. Please read [this document](CONTRIBUTING.md) before opening an issue.
