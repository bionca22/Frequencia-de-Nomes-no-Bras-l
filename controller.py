import requests
import json
from matplotlib import pyplot as plt

name = input("escreva um nome: ")
response = json.loads(
    requests.get("http://servicodados.ibge.gov.br/api/v2/censos/nomes/" + nome).text
)

periodlist = []
frequencylist = []

for line in response[0]["res"]:
    frequency = int(line["frequencia"])
    period = line["periodo"].replace("[", " ")

    periodlist.append(period)
    frequencylist.append(frequency)

plt.plot(periodlist, frequencylist)
plt.show()
