from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    has_moon: Mapped[bool]

# class Planet:

#     def __init__(self, id, name, description, has_moon):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.has_moon = has_moon

# planets = [
#     Planet(1, "Mars", "4217 miles in diameter, very cold and red", True),
#     Planet(2, "Earth", "7926 miles in diameter, habitable and blue", True),
#     Planet(3, "Venus", "3760.4 miles in diameter, hottest planet and red", False)
#     ]