URL = "http://linux-libre.fsfla.org/pub/linux-libre/releases/2.6.32.66-gnu1/linux-libre-2.6.32.66-gnu1.log"

import requests

text = requests.get(URL).text

modules = {}

for line in text.split('\n'):
  if " - " in line:
    partes = line.split(" - ")
    nome = partes[0]
    desc = partes[1]
    if nome not in modules and len(nome) > 2 and nome.isupper():
      modules[nome] = desc
      print (f"{nome}:\t {desc}")
