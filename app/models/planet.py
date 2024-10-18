class Planet:

    def __init__(self, id, name, description, has_moon):
        self.id = id
        self.name = name
        self.description = description
        self.has_moon = has_moon

planets = [
    Planet(1, "Mars", "4217 miles in diameter, very cold and red", True),
    Planet(2, "Earth", "7926 miles in diameter, habitable and blue", True),
    Planet(3, "Venus", "3760.4 miles in diameter, hottest planet and red", False)
    ]