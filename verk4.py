from sys import argv
import bottle
from bottle import *
import urllib.request, json

# templates
@route("/")
def index():
    return """
    <h2>Verkefni 4</h2>
    <p><a href="/a">Local Json</a></p>
    <p><a href="/b">Json API</a></p>
    """

#template dæmi - json
@route("/a")
def index():
    return template("index.tpl")

with urllib.request.urlopen("http://apis.is/currency/") as url:
    data = json.loads(url.read().decode())

@route("/b")
def index():
    return template("index2.tpl", data=data)



######################################################
# template dæmi - fréttasíða
@route("/static/<skra>")
def static_skrar(skra):
    return static_file(skra, root='./static')

@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"

#run(host='localhost', port=8080, reloader=True, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])