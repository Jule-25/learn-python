class Planet:
    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"
    
    @classmethod
    def commons(cls):
        f"All planets are {cls.shape} because of gravity"

    @staticmethod
    def spin(speed = '200 miles per hour'):
        return f"The planet spins and spins at {speed}"

# Make a Planet
hoth = Planet('Hoth', 20000, 5.5, 'Hoth System')
print(hoth.orbit())
print(Planet.shape)

print(Planet.commons())
print(Planet.spin())


