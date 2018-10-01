
'''=========================================================
@Autor: Rodrigo Barreto

Objetivo: Módulo criado para testar as funções
do módulo Planeta


========================================================='''
from planeta import Planeta
import json
import planeta as pl


# Teste 1: Listando todos os planetas

p = Planeta()

print("=====================================")
print("Teste 1: Listando todos os planetas:")
print()
pl.showAllPLanets(p)


# Teste 2: Buscando um planeta por nome

print("=====================================")
print("Teste 2: Buscando um planeta por nome")
print("")
namePlanet = "Yavin IV"
planet = pl.getPlanetByName(p, namePlanet)
pl.showPlanet(planet)


print("")
namePlanet = "XYZ"
planet = pl.getPlanetByName(p, namePlanet)
pl.showPlanet(planet)


# Teste 3: Buscando um planeta por ID

print("=====================================")
print("Teste 3: Buscando um planeta por ID")
print("")

planet = pl.getPLanetByID(p, 1)
pl.showPlanet(planet)


planet = pl.getPLanetByID(p, 25)
pl.showPlanet(planet)


#planet = pl.getPLanetByID(p, 101)
#pl.showPlanet(planet)





# Teste 4: Adicionando um novo planeta

print("=====================================")
print("Teste 4: Adicionando um novo planeta")


url = "https://swapi.co/api/planets/"

data = {
"name": "RBS",
"rotation_period": "24",
"orbital_period": "11111",
"diameter": "22223",
"climate": "moist, tropical",
"gravity": "33 standard",
"terrain": "jungle, rainforests",
"surface_water": "44",
"population": "55503",
"residents": ["https://swapi.co/api/people/1/"],
"films": [
		"https://swapi.co/api/films/1/" ,
         "https://swapi.co/api/films/2/"
  ],
"created": "2015-10-10T11:37:19.144000Z",
"edited": "2018-06-20T20:58:18.421000Z",
"url": "https://swapi.co/api/planets/3/"

}
pl.addPlanet(p, url, data)




# Teste 5: Remove planeta

print("=====================================")
print("Teste 5: Remove planeta")
print("")
url = "https://swapi.co/api/planets/"

data= {
	"name": "Yavin IV",
	"rotation_period": "24",
	"orbital_period": "4818",
	"diameter": "10200",
	"climate": "temperate, tropical",
	"gravity": "1 standard",
	"terrain": "jungle, rainforests",
	"surface_water": "8",
	"population": "1000",
	"residents": [],
	"films": [
		"https://swapi.co/api/films/1/"
	],
	"created": "2014-12-10T11:37:19.144000Z",
	"edited": "2014-12-20T20:58:18.421000Z",
	"url": "https://swapi.co/api/planets/3/"
}


pl.removePlanet(p , url, data)


'''===========================xxxxxxxxxxxxxx=============================='''