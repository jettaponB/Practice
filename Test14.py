import class_tank as CT

first_tank  = CT.Tank('Serie1', 3)
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(4)
print(first_tank.ammo)
