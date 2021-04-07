import requests
import __main__ as main
import json
from helper import get_env

def get_promo_bach2023():
    PROMO = main.SESSION.get("https://prepintra-api.etna-alternance.net/trombi/614")
    return (PROMO.json())

def get_promo_bach_piscine():
    PROMO = main.SESSION.get("https://prepintra-api.etna-alternance.net/trombi/515")
    return (PROMO.json())

def sortSecond(val): 
    return val[1]

def get_student_mark(student):
    PROMO = main.SESSION.get("https://intra-api.etna-alternance.net/terms/614/students/{}/marks".format(student))
    print(json.dumps(PROMO.json(), indent=2, separators=(". ", " = ")))

def get_note(promo):
    url_note = "https://prepintra-api.etna-alternance.net/terms/515/students/{}/marks"
    i = 0
    my_dico = []
    my_result = []
    moyenne = 0
    count_exo = 0
    for p in promo['students']:
        my_dico.append({'student_name':p['login'], 'student_bench':main.SESSION.get(url_note.format(p['login'])).json()})
    for d in my_dico:
        for module in d['student_bench']:
            if  "DEVC" in module['uv_name']:
                moyenne += module['student_mark']
                count_exo += 1
        if count_exo > 0:
            my_result.append((d['student_name'], moyenne/count_exo))
        moyenne = 0
        count_exo = 0
        i += 1
    my_result.sort(key = sortSecond, reverse = True)
    print(*my_result, sep = "\n")