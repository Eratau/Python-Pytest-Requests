import requests

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = '22a1c01efefc3afba10dc4382c93d6f6'
HEADER = {'Content-Type':'application/jison', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "vihodcev1989@gmail.com",
    "password": "123qweQQ123rewa55",
    "password_re": "123qweQQ123rewa55"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_creat = {
    "name": "Бульбазавр",
    "photo_id": 12
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers= HEADER, json = body_registration )
print(response.text)'''

'''respons_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json= body_confirmation)
print(respons_confirmation.text)'''

response_create= requests.post(url=f'{URL}/pokemons',headers=HEADER, json= body_creat)
print(response_create.text)

massege= response_create.json['massege']
print(massege)