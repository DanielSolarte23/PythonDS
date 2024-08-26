from PooPy.Perro.Perro import Perro

chanda1 = Perro("Blue", "Beagle")

chanda2 = Perro("Zeus", "Pastor Aleman")

print(f"{chanda1.nombre} es de raza {chanda1.raza}")
print(f"{chanda2.nombre} es de raza {chanda2.raza}")

chanda1.caminar(5)
chanda1.ladrar()

chanda2.caminar(1453)
chanda2.ladrar()