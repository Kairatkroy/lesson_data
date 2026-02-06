import json
import yaml

data = {
        "fruits": ["apple", "banana",'"orange", "grape", "melon"'],
         "numbers": ["1, 2, 3, 4, 5"],
        "fds": {"hoi": 21}
       }



with open("kloi", "w") as w:
    coin = yaml.dump(data, w)

with open("kloi") as r:
    h = yaml.safe_load(r)


json_new = json.dumps(data, indent=4)

with open("json1", "w") as w:
    w.write(json_new)

with open("json1") as r:
    json1 = json.load(r)
    print(json1)
