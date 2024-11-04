from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db 
from .route_utilities import validate_model

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    sort_param = request.args.get("sort")
    
    if sort_param and sort_param.lower() == "name":
        query = db.select(Planet).order_by(Planet.name)
    else:
        query = db.select(Planet).order_by(Planet.id)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    has_moon_param = request.args.get("has_moon")

    if has_moon_param is not None:
        has_moon_value = has_moon_param.lower() == "true"
        query = query.where(Planet.has_moon == has_moon_value)

    planets = db.session.scalars(query)

    return [planet.to_dict() for planet in planets]

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@planets_bp.get('/<planet_id>')
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_moon = request_body["has_moon"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")



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
