from flask import Flask, request, render_template
import services.sql as sql
import services.cep as cepApi

app = Flask(__name__)

# Rota base para renderizar a página inicial/index
@app.route("/")
def menu():
    return render_template("index.html", message = None)

# Rota utilizada para renderizar o template de registro
@app.route('/register')
def register():
    return render_template('forms/register.html')

# Rota para realizar cadastro
# Pega os dados conforme a queryString "name" através dos request.form e valida o CEP conforme a chamada na API passando o valor.
@app.route("/cliente/novo", methods = ["POST"])
def criar_cliente_api():
    message = None
    nome_cliente = request.form["nome_cliente"]
    login = request.form["login"]
    senha = request.form["senha"]
    cpf = request.form["cpf"]
    cep = request.form['cep']
    try:
        verifica_cep = cepApi.verifica_cep(cep)
        id_cliente = sql.criar_cliente(nome_cliente, login, senha, cpf, cep)
        message = "O cadastro foi realizado com sucesso"
        
    except:
        message = "Falha em cadastrar usuário"

    return render_template('index.html', message = "O cadastro foi realizado com sucesso")


if __name__ == "__main__":
    sql.criar_bd()
    app.run(host='127.0.0.1', port=8000)




#### Não necessários logo abaixo
##
# @app.route("/cliente/novo", methods = ["GET"])
# def form_criar_cliente_api():
#     return render_template("form_cliente.html", id_cliente = "novo", nome_cliente = "", login = "", senha = "", cpf = "")

# def row_to_dict(description, row):
#     if row == None:
#         return None
#     d = {}
#     for i in range(0, len(row)):
#         d[description[i][0]] = row[i]
#     return d


# def rows_to_dict(description, rows):
#     result = []
#     for row in rows:
#         result.append(row_to_dict(description, row))
#     return result