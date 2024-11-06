from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from ..db import db 
from .route_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)

@bp.post("")
def create_planet():
    request_body = request.get_json()

    return create_model(Planet, request_body)

@bp.get('/<planet_id>')
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_moon = request_body["has_moon"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)


@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    response = [book.to_dict() for book in planet.moons]
    return response


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))


# @planets_bp.get("")
# def get_all_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id":planet.id,
#                 "name":planet.name,
#                 "description":planet.description,
#                 "has_moon":planet.has_moon,
#             }
#         )
#     return planets_response


# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id":planet.id,
#         "title":planet.name,
#         "description":planet.description,
#         "has_moon":planet.has_moon,
#     }
