import requests
import json
from matplotlib import pyplot as plt
import os


def get_name(name: str) -> None:
    if (name ==""):
        return False
    
    response = json.loads(
        requests.get("http://servicodados.ibge.gov.br/api/v2/censos/nomes/" + name).text
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
    return True

while(1):
    os.system("cls")
    get_name(input("Nome: "))