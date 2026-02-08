import json
from xml.etree.ElementTree import indent

import yaml
import pandas

import pandas as pd
import numpy as np

data = {
    "ints": [1, 2, 3],
    "floats": [1.1, 2.2, 3.3],
    "bools": [True, False, True],
    "strings": ["яблоко", "приправа", "корнос"],
    "dates": (["2024-01-01", "2024-01-02", "2024-01-03"]),
    "categories":(["A", "B", "A"]),

}


panda = pd.DataFrame(data,) # превращение файла в pandas файл при "DataFrame"
panda.to_csv("panda.csv", index=False) # сохранение данных в файл при помощи "to_csv"

js = json.dumps(data, indent=3, ensure_ascii=False) # стерилизация файла в json формат при "dumps"
with open("json.format", "w", encoding="utf-8") as j: # 1
    j.write(js) # 2 # сохранение дынных в файл при 1 и 2 "write"

with open("json.format", "r", encoding="utf-8",) as r:
    re = json.load(r) # стерилизация формата из json на dict при "load"
    print(re)

with open("js", "w", encoding="utf-8") as w:
    json.dump(data, w, indent=4, ensure_ascii=False) # сокращение кода при "dump" стерилизация и сохранение "ensure_ascii=False" - чтение кирилицы




with open("yaml.format", "w", encoding="utf-8") as w:
    yaml.dump(data, w, allow_unicode=True) # стерилизация и сохранение в ямл формат "dump" "allow_unicode=True" - чтение кирилицы

with open("yaml.format", "r", encoding="utf-8") as r:
    re = yaml.safe_load(r) # стерилизация формата из json на обычный тип данных при "load"
    print(re)




