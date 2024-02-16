import csv
import random

import folium
import math

import geopy.distance
from haversine import haversine

positions = [
    [45.171112, 5.695952],
    [45.183152, 5.699386],
    [45.174115, 5.711106],
    [45.176123, 5.722083],
    [45.184301, 5.719791],
    [45.184252, 5.730698],
    [45.170588, 5.716664],
    [45.193702, 5.691028],
    [45.165641, 5.739938],
    [45.178718, 5.744940],
    [45.176857, 5.762518],
    [45.188512, 5.767172],
    [45.174017, 5.706729],
    [45.174458, 5.687902],
    [45.185110, 5.733667],
    [45.185702, 5.734507],
    [45.184726, 5.734666],
    [45.184438, 5.733735],
    [45.184902, 5.735256],
    [45.174812, 5.698095],
    [45.169851, 5.695723],
    [45.180943, 5.698965],
    [45.176205, 5.692165],
    [45.171244, 5.689872]
]

print("Voici les points GPS : ", positions, "\n")


# # Fonction qui récupère un csv et le transforme en objet python
def loadFile():
    positions.clear()
    with open('./70villes.csv') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            lat = float(row[0])
            lon = float(row[1])
            positions.append([lat, lon])
    return positions


loadFile()

visited = [False] * len(positions)
path = []


# Fonction pour calculer les distances entre deux points V1
def distance(i, j):
    gap = haversine(i, j)
    gap = round(gap, 5)
    return gap


# Fonction pour trier les positions par distance (matrice de distance)
matrix = [[distance(positions[i], positions[j]) for j in range(len(positions))] for i in range(len(positions))]
print("Matrice de distance :", matrix, "\n")


def total_distance(arr):
    total = 0
    for i in range(len(arr) - 1):
        lat1, lon1 = arr[i]
        lat2, lon2 = arr[i + 1]
        total += haversine((lat1, lon1), (lat2, lon2))
    return total


# ALGO DES PLUS PROCHES VOISINS_________________________________________________________________________________________

# Fonction du chemin le plus court non visité
def shortest_unvisited(current_town):
    visited[current_town] = True
    smallest = float("inf")
    i_smallest = 0

    for i in range(len(matrix)):
        if not visited[i]:
            if matrix[current_town][i] < smallest and matrix[current_town][i] != 0:
                smallest = matrix[current_town][i]
                i_smallest = i

    return i_smallest


shortest_unvisited(0)


# Index du chemin le plus court pour chaque ville
def nearest_neighbour():
    current_index = 0
    path.append(positions[current_index])
    for i in range(len(matrix)):
        index_town = shortest_unvisited(current_index)
        path.append(positions[index_town])
        current_index = index_town
    return path


nearest_neighbour()
print("Résultat du plus proche voisin :", path, "\nLa distance est égale à :", total_distance(path), "Km \n")


# ALGO GLOUTON__________________________________________________________________________________________________________
def algo_glouton(start_point, path):
    result = []
    result.insert(0, path.pop(start_point))
    while len(path) > 0:
        new_point = path.pop()
        temp = result[:]  # équivalent à result.copy()
        result.append(new_point)
        for j in range(0, len(result)):
            temp.insert(j, new_point)
            if total_distance(temp) < total_distance(result):
                result = temp[:]
            temp.pop(j)
    return result


path_glouton = algo_glouton(0, path.copy())
print("Résultat Glouton :", path_glouton)
total_glouton = total_distance(path_glouton)
print("La distance est égale à :", total_glouton, "Km")


# ALGO glouton optimisé
def shortest_glouton(path):
    shortest_way = 10000
    best_path = []
    for i in range(0, len(path) - 1):
        p = algo_glouton(i, path.copy())
        if total_distance(p) < shortest_way:
            shortest_way = total_distance(p)
            best_path.insert(0, p)
    return best_path[0]


path_glouton2 = shortest_glouton(path.copy())
print("\nRésultat du Glouton optimisé :", path_glouton2)
total_shortest_glouton = total_distance(path_glouton2)
print("La distance est égale à :", total_shortest_glouton, "Km")


# ALGO Génétique CHATGPT________________________________________________________________________________________________

# Fonction pour initialiser la population
def init_population(size_population):
    return [nearest_neighbour() for _ in range(size_population)]


# Fonction pour sélectionner les parents (tournoi binaire)
def selection_parents(population, scores):
    parents = [random.choice(population) for _ in range(len(population))]
    return parents


# Fonction de croisement (crossover)
def crossover(parent1, parent2, taux_croisement):
    if random.random() < taux_croisement:
        point_crossover = random.randint(1, len(parent1) - 1)
        enfant = parent1[:point_crossover] + [ville for ville in parent2 if ville not in parent1[:point_crossover]]
        return enfant
    else:
        return parent1


# Fonction de mutation
def mutation(individu, taux_mutation):
    if random.random() < taux_mutation:
        index1, index2 = random.sample(range(len(individu)), 2)
        individu[index1], individu[index2] = individu[index2], individu[index1]
    return individu


# Fonction principale de l'algorithme génétique
def algorithme_genetique(taille_population, taux_croisement, taux_mutation, nombre_generation):
    population = init_population(taille_population)
    meilleure_solution = None
    meilleure_distance = float('inf')

    for generation in range(nombre_generation):
        scores = [total_distance(individu) for individu in population]

        # Mise à jour de la meilleure solution de la génération actuelle
        index_meilleur = scores.index(min(scores))

        if scores[index_meilleur] < meilleure_distance:
            meilleure_solution = population[index_meilleur]
            meilleure_distance = scores[index_meilleur]

        parents = selection_parents(population, scores)

        nouvelle_generation = []
        for _ in range(taille_population // 2):
            parent1, parent2 = random.sample(parents, 2)
            enfant1 = crossover(parent1, parent2, taux_croisement)
            enfant2 = crossover(parent2, parent1, taux_croisement)
            enfant1 = mutation(enfant1, taux_mutation)
            enfant2 = mutation(enfant2, taux_mutation)
            nouvelle_generation.extend([enfant1, enfant2])

        population = nouvelle_generation

    return meilleure_solution


# Exécution de l'algorithme génétique
meilleure_solution_genetique = algorithme_genetique(taille_population=50, taux_croisement=0.8, taux_mutation=0.01,
                                                    nombre_generation=100)

print("\nMeilleure solution trouvée par l'algorithme génétique :", meilleure_solution_genetique)
print("Distance de la meilleure solution génétique :", total_distance(meilleure_solution_genetique), "Km")

# AFFICHAGE_____________________________________________________________________________________________________________

# Création de la carte
map = folium.Map([45.166672, 5.71667], tiles="cartodb positron", zoom_start=8)

# Marqueur du point de départ (Campus Numérique)
folium.Marker(
    location=[45.184599534292026, 5.731326584660483],
    tooltip="Le Campus Numérique",
    icon=folium.Icon(color="red", icon=""),
).add_to(map)

# Ajout des marqueurs sur la carte pour les positions
for index, position in enumerate(positions):
    folium.Marker(
        location=[position[0], position[1]],
        tooltip=str(index),
        icon=folium.Icon(color="green", icon="cloud"),
    ).add_to(map)

# # Ajout de la polyline pour connecter les points du résultat des plus proches voisins
# polyline_nearest_neighbour = folium.PolyLine(
#     locations=path, color='black'
# )
# polyline_nearest_neighbour.add_to(map)
#
# # Ajout des marqueurs sur la carte pour le résultat du glouton
# for index, position in enumerate(path_glouton):
#     folium.Marker(
#         location=[position[0], position[1]],
#         tooltip=str(index),
#         icon=folium.Icon(color="blue", icon="cloud"),
#     ).add_to(map)
#
# # Ajout de la polyline pour connecter les points du résultat du glouton
# polyline_glouton = folium.PolyLine(
#     locations=path_glouton, color='blue'
# )
# polyline_glouton.add_to(map)
#
# # Ajout des marqueurs sur la carte pour le résultat du glouton optimisé
# for index, position in enumerate(path_glouton2):
#     folium.Marker(
#         location=[position[0], position[1]],
#         tooltip=str(index),
#         icon=folium.Icon(color="purple", icon="cloud"),
#     ).add_to(map)
#
# # Ajout de la polyline pour connecter les points du résultat du glouton optimisé
# polyline_glouton_optimise = folium.PolyLine(
#     locations=path_glouton2, color='purple'
# )
# polyline_glouton_optimise.add_to(map)

# Ajout des marqueurs sur la carte pour le résultat de l'algorithme génétique
for index, position in enumerate(meilleure_solution_genetique):
    folium.Marker(
        location=[position[0], position[1]],
        tooltip=str(index),
        icon=folium.Icon(color="darkgreen", icon="cloud"),
    ).add_to(map)

# Ajout de la polyline pour connecter les points du résultat de l'algorithme génétique
polyline_genetique = folium.PolyLine(
    locations=meilleure_solution_genetique, color='darkgreen'
)
polyline_genetique.add_to(map)

# Sauvegarde de la carte au format HTML
map.save("index.html")
