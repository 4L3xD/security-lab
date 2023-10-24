from flask import render_template, redirect
from flask import request
from app import app

@app.route('/')
def home():
    return render_template("home.html")


#################### CÓDIGO VULNERÁVEL ####################
'''Parâmetros controlados pelo usuário permitem requisições maliciosas
para recursos internos ou para aplicações externas.'''

@app.route("/param/<param_name>")
def param_vuln(param_name):
    return redirect(f"https://{param_name}.com")
    # Exploit: localhost:56733/param/google

@app.route("/args")
def arg_vuln():
    target = request.args["target"]
    return redirect(f"https://{target}.example.com/data/")
    # Exploit: localhost:56733/args?target=google.com?

###########################################################


#################### CÓDIGO CORRIGIDO #####################

'''É recomendado o uso de whitelist'''

# @app.route("/param/<param_name>")
# def param_vuln(param_name):
#     if param_name == "servico-1":
#         return redirect("https://servico-1.com/exemplo1")
#     elif param_name == "servico-2":
#         return redirect("https://servico-2.com/exemplo2")
#     else:
#         return redirect("https://servico-padrao.com/requisicao-padrao")


'''O subdomínio é controlado pelo servidor'''

# @app.route("/args")
# def arg_vuln():
#     target = request.args["target"]
#     subdomain = "brasil" if target == "BR" else "mundo"
#     return redirect(f"https://{subdomain}.example.com/data/")

###########################################################