import urllib3
from urllib import parse, request

# import matplotlib.pyplot as plt
# import numpy as np
import json

import pprint

link = urllib3.PoolManager()
ibge_api = "https/servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/-6/variaveis/615|616?localidades=N2[all]"

params = {"N2": "[all]"}
querystring = parse.urlencode(params)
url = "https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/-6/variaveis/615|616?localidades=N2[all]" + "?" + querystring
resp = request.urlopen(url)
resp.isclosed()
""" pprint.pprint(querystring) """

""" response = link.request("GET", ibge_api)
content = response.data.decode('utf-8')
data = json.loads(content) """

# content_type = response.getheader("Content-Type")
# print(content_type)

""" print("Response status:", response.status)
import pprint
pprint.pprint(data) """
