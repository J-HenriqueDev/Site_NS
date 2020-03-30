import os,requests
from flask import Flask, render_template, request, session, redirect, jsonify,url_for,Markup
import markdown, api
import datetime
import auth
import pytz

app = Flask(__name__)
port = 80
app.config['SECRET_KEY'] = auth.secretkey

@app.errorhandler(404)
def page_not_found(e):
  if session.get('token') is None:
     return render_template('404.html', css={"img":True,"name":"404 - Not found","desc":"A pagina não encontrada!"}), 404
  try:
    user = api.get_info(session.get('token'))
  except requests.exceptions.HTTPError:
    return redirect("/logout")
  return render_template('404.html',user=user, css={"img":True,"name":"404 - Not found","desc":"A pagina não que você inseriu não foi encontrada!"}), 404


@app.template_filter('datetimefilter')
def datetimefilter(value):
    date_time_obj = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    return date_time_obj.strftime("%H:%M:%S - %d/%m/%Y")

#### home do site
@app.route('/')
def index():
    return render_template('index.html')

  
@app.route('/callback')
def response():	
    try:
        codigo = request.args.get('code')
        resposta = api.codigo_troca(codigo)
    except requests.exceptions.HTTPError:
        return redirect('/logout')
    session['token'] = resposta['access_token']
    session['scopes'] = auth.scopes.split(" ")
    return redirect("/")

@app.route('/login')
def login():
    if session.get('token') is None:
       url_authentication = "https://discordapp.com/api/oauth2/authorize?client_id=682280200699904091&redirect_uri=https%3A%2F%2Fwww.neostore.wtf%2Fcallback%2F&response_type=code&scope=identify%20email%20guilds"
       return redirect(url_authentication)
    else:
      return redirect("/") 

@app.route('/logout')
def logout():
    if session.get('token'):
        del session['token']
    return redirect('/')

@app.route('/convite')
def invite():
      return redirect("https://discordapp.com/invite/VvMmNCw")

if __name__ == '__main__':
  app.run(debug=True,port=port)
