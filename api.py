import requests
import __main__ as main
import json
import os
from helper import get_env
import sys

def get_promo_bach2023():
    PROMO = main.SESSION.get("https://prepintra-api.etna-alternance.net/trombi/614")
    return (PROMO.json())

def get_promo_bach_piscine():
    PROMO = main.SESSION.get("https://prepintra-api.etna-alternance.net/trombi/515")
    return (PROMO.json())

def sortSecond(val): 
    return val[1]

def get_student_mark(student):
    try: 
        os.mkdir("student_marks")
    except:
        print (os.getcwd() + "/student_marks")
        file = open("./student_marks/{}_mark.json".format(student), "w") 
        PROMO = main.SESSION.get("https://intra-api.etna-alternance.net/terms/614/students/{}/marks".format(student))
        if PROMO.status_code == 200:
            result = json.dumps(PROMO.json(), indent=4)
            file.write(result)
            print("vous pouvez maintenant regarder le fichier student_marks/{}_marks.json".format(student))
        else:
            print("Le login entré n'existe pas ou n'est pas dans le promo bachelor 2023")


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