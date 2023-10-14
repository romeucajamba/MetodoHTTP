from flask import Flask
from flask import request
from flask import redirect
from json import dumps

app = Flask(__name__, static_folder='page')

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        return dumps(request.form)
    elif request.method == 'GET':
        return redirect('http://facebook.com/romeucajamba/')
    else:
        return '<h1>Não foi poosível executar o pedido</h1>'

if __name__ == '__main__':
    app.run(debug=False, port=3000)