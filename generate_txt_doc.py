import json
import random
import yaml
import string
import xmltodict
import os
import datetime
from enum import Enum
import numpy as np

class TxtFileType(Enum):
    Json = 0
    Xml = 1
    Yaml = 2

def load_words_from_file(file_path):
    res = dict()
    with open(file_path, 'r') as file:
        x = [i.lower().split(' ') for i in file.read().splitlines()]
        for w in [w for w in x]:
            x = [i for i in w if(len(i) > 2 and i.isalpha())]
            for item in x:
                res[item] = None
    return list(res.keys())

def generate_random_word(words, rnd):
    return rnd.choice(words)

def generate_random_json(depth, words, rnd, mixinVal):
    if depth == 0:
        return rnd.choice([random.randint(1, 100), random.random(), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))]
)

    result = {}
    num_keys = rnd.randint(2, 5)
    for _ in range(num_keys):
        key = generate_random_word(words, rnd)
        value = generate_random_json(depth - 1, words, rnd, mixinVal - 1)
        result[key] = value
    if(random.randint(0, 100) <= mixinVal): # add mixin
        rndMixin = np.random.RandomState()
        key = generate_random_word(words, rndMixin)
        value = generate_random_json(depth - 1, words, rndMixin, mixinVal - 1)
        result[key] = value

    return result

def generate_random_doc(docScheme: int, mixinVal:int, txtType: TxtFileType):
    words = load_words_from_file('some_text.txt')
    rndState = np.random.RandomState(docScheme)
    random_json = generate_random_json(rndState.randint(3, 5), words, rndState, mixinVal)
    random_json_str = json.dumps(random_json, indent=4)
    python_dict=json.loads(random_json_str)
    # print(keys_to_list(random_json))
    txt_doc = ""
    if txtType == TxtFileType.Json:
      txt_doc = random_json_str
    elif txtType == TxtFileType.Yaml:
      txt_doc = yaml.dump(python_dict)
    else:
      xml_root = {'root':python_dict}
      txt_doc = xmltodict.unparse(xml_root)
    return (txt_doc, keys_to_list(random_json))

def keys_to_list(d, parent_key=''):
    keys = []
    for k, v in d.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            keys.extend(keys_to_list(v, new_key))
        else:
            keys.append(new_key)
    return keys

def generate_random_docs(types_count: int, docs_pre_type:int, mixin: int):
    t = 1
    keys_arr = []
    new_dir = f'run_{datetime.datetime.now().strftime("%H%M%S")}'
    os.makedirs(new_dir, exist_ok=True)
    while t <= types_count:
        i = 1
        while i <= docs_pre_type:
            doc, keys = generate_random_doc(t, mixin, TxtFileType.Json)
            keys_arr.append(keys)
            file = open(f'{new_dir}/some_t_{t:02}_n_{i:02}.json', 'w')
            file.write(doc)
            file.close()
            i = i + 1
        t = t + 1
    return keys_arr
