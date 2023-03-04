from flask import Blueprint

maestros = Blueprint("maestros", __name__)

@maestros.get("/maestros")
def maestro():
  return {'key': 'Maestros'}