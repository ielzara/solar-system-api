from flask import Blueprint, abort, make_response, request, Response
from app.models.moon import Moon
from app.models.planet import Planet
from ..db import db
from .route_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")


@bp.post("")
def create_moon():
    request_body = request.get_json()

    return create_model(Moon, request_body)


@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)


@bp.get("/<moon_id>")
def get_one_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    return moon.to_dict()


@bp.put("/<moon_id>")
def update_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    request_body = request.get_json()

    try:
        moon.name = request_body["name"]
        moon.description = request_body["description"]
        moon.size = request_body["size"]
    except KeyError as error:
        return make_response(
            {"message": f"Missing required field: {str(error.args[0])}"}, 400
        )

    db.session.commit()

    return make_response({"message": f"Moon #{moon.id} successfully updated"}, 200)


@bp.delete("/<moon_id>")
def delete_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    db.session.delete(moon)
    db.session.commit()

    return {"message": f"Moon {moon_id} successfully deleted"}, 200
