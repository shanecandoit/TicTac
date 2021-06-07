import json
from flask import Flask

from board import Board

app = Flask(__name__)


@app.route('/')
def index():
    b = Board()
    # return json.dumps({'name': 'alice',
    #                    'email': '[email protected]'})
    return json.dumps(b.__dict__)
    '''{"rows": [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]], "turn": 1, "won": false, "player": "Player1 (X)"}'''

app.run( debug=True,)
