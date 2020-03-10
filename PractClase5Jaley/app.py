from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def resultado():
    number1 = int(request.args.get("number1", 0))
    number2 = int(request.args.get("number2", 0))
    resultado = number1 + number2
    return f'resultado, {escape(resultado)}!'