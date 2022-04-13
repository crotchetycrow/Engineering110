import json

# car = {"make": "tesla", "engine": "electric", "faults": "lots"}
#
# json_dumps = json.dumps(car)
#
# # print(json_dumps, type(json_dumps))
#
# # with open("car_json_file.json", "w") as jsonfile:
# #     json.dump(car, jsonfile)
#
# with open("new_car_json_file.json", "r") as jsonfile:
#     new_car = json.load(jsonfile)
#
# print(new_car, type(new_car))


films = {"title": "batman", "genre": "action", "director": "Matt Reeves", "ratings":{
    "rotten toms": 9,
    "imbd": 9,
    "me": 8
}}

with open("films_json_file.json", "w") as filmjson:
    json.dump(films, filmjson)
with open("films_json_file.json", "r") as filmjson:
    new_film = json.load(filmjson)
