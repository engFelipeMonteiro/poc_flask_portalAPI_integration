# flask
from flask import Flask

app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return {"Hello": "Flask"}

# fast-api
from fastapi import FastAPI

app_fast = FastAPI()
app_fast.title = "API do Felipe"
@app_fast.get("/")
def home_fast():
    return {"Hello": "Fast"}

# starlette combine apps
from starlette.applications import Starlette
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Route, Router, Mount


app_star = Starlette(...)

app_star.mount("/flask", app=WSGIMiddleware(app_flask.wsgi_app))
app_star.mount("/fast", app=app_fast)
