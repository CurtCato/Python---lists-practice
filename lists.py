# Practice - Random Numbers
import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

numb_list = range(1, 11)
for number in numb_list:
    contains = False
    for x in my_randoms:
        if x == number:
            contains = True
    print(f"My random list {'contains' if contains else 'does not contain'} {number}")


# Practice - Planet List
planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[8]

print(rocky_planets)
print(planet_list)