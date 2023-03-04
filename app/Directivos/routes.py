from flask import Blueprint

directivos = Blueprint("directivos", __name__)

@directivos.get("/directivos")
def directivo():
  return {'key': 'Directivos'}