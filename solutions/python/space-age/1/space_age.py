class SpaceAge:
    def __init__(self, seconds):
        self.base_line = 31_557_600
        self.seconds = seconds
        orbital_periods = {
            "on_mercury": 0.2408467,
            "on_venus": 0.61519726,
            "on_earth": 1.0,
            "on_mars": 1.8808158,
            "on_jupiter": 11.862615,
            "on_saturn": 29.447498,
            "on_uranus": 84.016846,
            "on_neptune": 164.79132,
        }

        for planet, period in orbital_periods.items():
            self.add_lambda(planet, lambda period=period: round(self.seconds / self.base_line / period, 2))

    def add_lambda(self, name, func):
        setattr(self, name, func)