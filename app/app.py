import flask

from Alumnos.routes import alumnos
from Maestros.routes import maestros
from Directivos.routes import directivos

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.get("/")
def home():
  return flask.jsonify(
    {
      "name": "Home"
    }
  )

app.register_blueprint(alumnos)
app.register_blueprint(maestros)
app.register_blueprint(directivos)

if __name__ == "__main__":
  app.run()