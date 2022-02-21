from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def main():
    return render_template('Pagina1.html')


@app.route("/calcular", methods=['POST', 'GET'])
def calcular():
    v1=request.form['v1']
    v2=request.form['v2']
    operador=request.form['operador']

    if (operador == "soma"):
        resultado = int(v1) + int(v2)

    elif(operador == "subtracao"):
        resultado = int(v1) - int(v2)

    elif(operador == "divisao"):
        if (v2 == 0):
            return ("Não e possivel dividir numeros por 0!!!")
        else:
            resultado = int(v1) / int(v2)
    elif (operador == "multiplicacao"):
        resultado = int(v1) * int(v2)
    else:
        return ("Não foi passado os numeros!!!")

    return str(resultado)


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
