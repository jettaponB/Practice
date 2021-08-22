class Tank:
    def __init__(self, name, ammo) -> None:
        self.name = name
        self.ammo = ammo

first_tank  = Tank('Serie1', 3)
print(first_tank.name)

second_tank = Tank('Serie2', 5)
print(second_tank.name)