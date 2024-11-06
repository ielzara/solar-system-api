from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .planet import Planet


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[int]
    description: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_as_dict = {
            "id": self.id, 
            "name": self.name,
            "size": self.size,
            "description": self.description
            }
        if self.planet:
            moon_as_dict["planet"] = self.planet.name

        return moon_as_dict

    @classmethod
    def from_dict(cls, moon_data):
        planet_id = moon_data.get("planet_id")
        description = moon_data["description"]

        new_moon = cls(
            name=moon_data["name"],
            size=moon_data["size"],
            description=description,
            planet_id=planet_id
            )

        return new_moon
