from packages.planet import Planet
from packages.cal import planet_mass, planet_vol

naboo = Planet('Naboo', 3000000.0, 300, 'Naboo System')
naboo_vol = planet_vol(naboo.radius)

print(f"{naboo.name} has a vol of {naboo_vol}")
