# part1
person = {
    "name": "aryam",
    "age": 13,
    "hobbies": ["swimming", "basketball", "horse riding"]
}

print("name:", person.get("name"), "age:", person.get("age"))
# part2   
person["age"]=14
person["country"]="kuwait"

print(person)
print(len(person))
# part3
person["hobbies"].append("football")
print(person)
def check_hobbies(person):
    if len(person["hobbies"])>=3:
        return "WOW YOU ARE AMAZING"
    else:
        return "YOUR STILL AMAZING"

print(check_hobbies(person))
