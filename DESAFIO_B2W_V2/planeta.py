
'''=========================================================
 @Autor: Rodrigo Barreto

 Objetivo: Módulo que implementa as funcionalidades
 do planeta
========================================================='''

import requests
import swapi
import json

class Planeta():


 '''
Nome 
Clima
Terreno 
'''

'''========================================================
         Implementação das funcionalidades
==========================================================='''


'''
- Adicionar um planeta (com nome, clima e terreno)
- Listar planetas - OK 1
- Buscar por nome - OK 1
- Buscar por ID - OK 1
- Remover planeta
'''


# Método: Adicionar um planeta (com nome, clima e terreno)


def addPlanet(self, url , payload):
 '''
  #planets = []
  planets = swapi.get_all("planets")
  planets.append(planet)
'''
 headers = {'User-Agent': 'swapi-python'}
 response = requests.post(url, data=json.dumps(payload), headers=headers)
 print(response.text)

# Método: Listar planetas

def showAllPLanets(self):

    cont = 1
    planets = swapi.get_all("planets")
    for i in planets.order_by("name"):
        print(cont)
        print("Nome do Planeta: " + i.name)
        print("Diâmetro: " + i.diameter)
        print("Período de rotação: " + i.rotation_period)
        print("Período orbital: " + i.orbital_period)
        print("Gravidade: " + i.gravity)
        print("População: " + i.population)
        print("Clima: " + i.climate)
        print("Terreno: " + i.terrain)
        print("Superfície da água: " + i.surface_water)

        for j, aux in enumerate(i.residents):
            print("Residentes: " + i.residents[j])

        for k, aux2 in enumerate(i.films):
            print("Quantidade de Filmes: " + i.films[k])

        print("Url: " + i.url)
        print("Criado: " + i.created)
        print("Editado: " + i.edited)
        print("")
        cont = cont + 1


# Método: Exibe todas as informações de um planeta a partir do seu ID

def showPlanet(t):

    if(t is None):
        return "O planeta não existe"

    print("Nome do Planeta: " + t.name)
    print("Diâmetro: " + t.diameter)
    print("Período de rotação: " + t.rotation_period)
    print("Período orbital: " + t.orbital_period)
    print("Gravidade: " + t.gravity)
    print("População: " + t.population)
    print("Clima: " + t.climate)
    print("Terreno: " + t.terrain)
    print("Superfície da água: " + t.surface_water)

    for j, k in enumerate(t.residents):
        print("tidentes: " + t.residents[j])

    for l, m in enumerate(t.films):
        print("Quantidade de Filmes: " + t.films[l])

    print("Url: " + t.url)
    print("Criado: " + t.created)
    print("Editado: " + t.edited)
    print("")


# Método: Buscar planeta por nome

def getPlanetByName(self, namePlanet ):

     planets = swapi.get_all("planets")
     for p in planets.order_by("name"):
        if( p.name == namePlanet ):
           return p

     return None



# Método: Buscar planeta por ID

def getPLanetByID(self, idPlanet ):

  planet = swapi.get_planet(idPlanet)
  print(planet)
  if(planet is None):
     return None

  return planet



# Método: Remover planeta

def removePlanet(self, url , payload):

  '''
  planets= []
  planets = swapi.get_all("planets")
  if( planets.__sizeof__() == 0 ):
   return "Lista está vazia"
'''

# headers = {'content-type': 'application/json'}
  headers = {'User-Agent': 'swapi-python'}
  response = requests.delete(url, data=json.dumps(payload), headers=headers)


'''==========================xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=============================='''


