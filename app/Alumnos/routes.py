from flask import Blueprint

alumnos = Blueprint("alumnos", __name__)

@alumnos.get("/alumnos")
def alumno():
  return {'key': 'Alumnos'}