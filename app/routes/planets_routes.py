from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db 

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    query=db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response=[]
    for planet in planets:
        planets_response.append(
            {
                "id":planet.id,
                "name":planet.name,
                "description":planet.description,
                "has_moon":planet.has_moon
            }
        )
    return planets_response

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    has_moon = request_body["has_moon"]

    new_planet = Planet(name=name, description=description, has_moon=has_moon)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "has_moon": new_planet.has_moon
    }
    return response, 201

@planets_bp.get('/<planet_id>')
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "has_moon": planet.has_moon,
    }


@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_moon = request_body["has_moon"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet

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
