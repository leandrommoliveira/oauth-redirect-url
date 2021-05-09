from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/authorize', methods=['GET'])
def authorization_code():
    code = request.args.get('code')
    state = request.args.get('state')
    error = request.args.get('error')

    if error:
        return 'error=' + error
    
    if code and state:
        return 'authorization_code=' + code + ', state=' + state 
    
    if code:
        return 'authorization_code=' + code

