import requests

url = 'https://api.chucknorris.io/jokes/random'


def get_joke():
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()['value']
    except Exception:
        joke = '''Международный Магический Сервис Шуток Чака Норриса приносит свои извинения за неполадки.
В кратчайшие сроки вы снова сможете наслаждаться штуками про Чака Норриса.
С уважением, ММСШЧК'''
    return joke