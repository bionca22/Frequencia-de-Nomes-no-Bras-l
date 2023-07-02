import urllib3
# import matplotlib.pyplot as plt
# import numpy as np
import json

link = urllib3.PoolManager()
ibge_api = "http://servicodados.ibge.gov.br/api/v3/agregados/8418/periodos/-6/variaveis/12747?localidades=N2[5]"


response = link.request("GET", ibge_api)
content = response.data.decode('utf-8')
data = json.loads(content)

print("Response status:", response.status)

# content_type = response.getheader("Content-Type")
# print(content_type)
import pprint
pprint.pprint(data[0]["resultados"][0]["series"][0]["localidade"]["nivel"]["nome"])
