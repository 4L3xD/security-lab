from flask import render_template, redirect
from flask import request
from app import app

@app.route('/')
def home():
    return "<b>Página inicial</b>"


@app.route('/template')
def template():
    return render_template('home.html')


@app.route("/service_status/<service_name>") # Internal Server Error
def get_service_status(service_name):
    # BAD:
    # user-controlled parameters can allow an attacker to
    # to send malicious requests to internal resources
    # or other external applications
    return redirect(f"https://{service_name}.com")

    # GOOD:
    # It is highly recommend to use a whitelist approach

    # if service_name == "someservice":
    #     return requests.get("https://someservice.com/myrequest")
    # elif service_name == "otherservice":
    #     return requests.get("https://otherservice.com/otherrequest")
    # else:
    #     return requests.get("https://defaultservice.com/defaultrequest")


@app.route("/full_ssrf")
def full_ssrf():
    target = request.args["target"]

    # BAD: user has full control of URL
    ## http://localhost:56733/full_ssrf?target=evil.com#
    return redirect(f"https://{target}.example.com/data/")

    # # GOOD: `subdomain` is controlled by the server.
    # subdomain = "europe" if target == "EU" else "world"
    # resp = requests.get("https://" + subdomain + ".example.com/data/")