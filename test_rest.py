import requests


def test_rest_api():
    url = 'http://127.0.0.1:5000/'
    resp = requests.get(url)
    print('resp', resp.status_code)
    print('json', resp.json())
    assert resp.status_code == 200
    expect = {'rows': [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']], 'turn': 1, 'won': False, 'player': 'Player1 (X)'}
    assert resp.json() == expect
    print(resp.text)