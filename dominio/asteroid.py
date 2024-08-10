from servicio.celestial_object import CelestialObject
class Asteroid(CelestialObject):

    def __init__(self, image_path, distance, orbit_speed, mass):
        
        super().__init__(image_path=image_path, mass=mass, distance=distance, orbit_speed=orbit_speed)
        
       
    def generate_magnetic_field(self, screen):
        pass       