Eng110 = {
    "name": "Jack",
    "job": "Trainee DevOps Consultant",
    "age": 29
}

print(Eng110, type(Eng110))

print(Eng110["job"])
Eng110["job"] = "Junior DevOps Consultant"
print(Eng110["job"])
Eng110["hobbies"] = ["Video games", "Hiking", "Skiing"]
print(Eng110)

print(Eng110.get("name"))
print(Eng110.update({"name": "Jack Hooper"}))
print(Eng110)


favourite_film = {
    "title": "The Batman",
    "director": "Matt Reeves",
    "genre": "Action",
    "year": 2022,
    "ratings": {
        "iMDb": 9,
        "Rotten Tomatoes": 8.5,
        "Metacritic": 9.2
    }
}

print(favourite_film)
print(favourite_film["ratings"]["Metacritic"])

print(favourite_film.keys())
print(favourite_film.values())
print(favourite_film.items())