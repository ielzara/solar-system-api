# place in a top-level file. call it something like seed.py
# no need to dwell on the `with my_app.app_context():`, other than to say
# that the `db` reference won't work unless it runs with an app context

from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context() as ctx:
    db.session.add(Planet(name="Mars", description="4217 miles in diameter, very cold and red", has_moon=True)),
    db.session.add(Planet(name="Earth",description="7926 miles in diameter, habitable and blue", has_moon=True)),
    db.session.add(Planet(name="Venus",description="3760.4 miles in diameter, hottest planet and red", has_moon=False)),
    db.session.commit()
