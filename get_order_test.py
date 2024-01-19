# Анна Рыкун, 12-я когорта - Финальный проект. Инженер по тестированию плюс

import config
import data
import requests

def post_create_order():
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=data.user_body,
                         headers=data.headers)

def get_order(track):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH,
                         params={"t": track})

# Проверка, что код ответа равен 200
def test_order():
    resp = post_create_order()
    track = resp.json()["track"]
    resp = get_order(track)
    assert resp.status_code == 200
