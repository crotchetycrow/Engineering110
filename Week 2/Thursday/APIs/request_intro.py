import requests
import json
from pprint import pprint

# r = requests.get('https://api.postcodes.io/postcodes/ct28ez')
#
# print(r, type(r))
# print(r.status_code)
# # print(r.headers, type(r.headers))
#
#
# # print(r.headers["age"])
# #
# if r.status_code == 200:
#     content = r.content
#     content_json = r.json()
#     result = content_json['result']
#     print(result)
#     # print(result['eastings'], result['northings'])
#     # print(result.get('eastings'), result.get('northings'))

headers = {"Content-Type": "application/json"}
data = {"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]}
# data_json = json.dumps(data)
# Use json=  instead of data=
r = requests.post(url='https://api.postcodes.io/postcodes', headers=headers, json=data)

print(r)
# print(r.json().get("error"))

r_json = r.json()["result"]

for postcode in r_json:
    each_result = postcode["result"]
    print(f'{each_result["region"], each_result["parliamentary_constituency"]}')
    pprint(each_result, sort_dicts=False)



# result1 = r_json["result"][0]["result"]
# result2 = r_json["result"][1]["result"]
# result3 = r_json["result"][2]["result"]
# results_region = result3["region"], result2["region"], result1["region"]
# results_constituency = result3["parliamentary_constituency"], result2["parliamentary_constituency"], result1["parliamentary_constituency"]
#
# print(results_region)
# print(results_constituency)