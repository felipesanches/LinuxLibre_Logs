import requests

def lista_logs():
  BASE_URL = "http://linux-libre.fsfla.org/pub/linux-libre/releases"
  html = requests.get(BASE_URL).text
  logs = []
  for line in html.split('\n'):
    if 'href="' in line:
      log_url = line.split('href="')[1].split('"')[0]
      if "-gnu" in log_url:
        logs.append(f"{BASE_URL}/{log_url}")
  return logs


def analisa_log(url):
  text = requests.get(url).text
  modules = {}

  for line in text.split('\n'):
    if " - " in line:
      partes = line.split(" - ")
      nome = partes[0]
      desc = partes[1]
      if nome not in modules and len(nome) > 2 and nome.isupper():
        modules[nome] = desc

  return modules


logs = lista_logs()
print (logs)

m = analisa_log("http://linux-libre.fsfla.org/pub/linux-libre/releases/2.6.32.66-gnu1/linux-libre-2.6.32.66-gnu1.log")
for nome, desc in m.items():
  print (f"{nome}:\t {desc}")

