import requests
import __main__ as main
from helper import check_env, get_env, remove_env

def authentification():
    check_env()
    PARAMETERS = {
        "login" : get_env("LOGIN"),
        "password" : get_env("PASSWORD")
    }
    REQUEST = main.SESSION.post("https://auth.etna-alternance.net/login", PARAMETERS) # API Request
    
    if(REQUEST.status_code == 200) :
        print("\x1bc", "Vous êtes connecté.\n\n")
        
        return 1
    else :
        print('\x1bc', "Mot de passe ou login incorrect, Veuillez réesayer\n")
        remove_env()
        return 0