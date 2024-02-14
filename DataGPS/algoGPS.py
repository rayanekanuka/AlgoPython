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

# ALGO DES PLUS PROCHES VOISINS_________________________________________________________________________________________

visited = [False] * len(positions)
path = []


#Fonction pour calculer les distances entre deux points V1
def distance(i, j):
    gap = haversine(i, j)
    gap = round(gap, 4)
    return gap

# def distance(point1, point2):
#     coords_1 = float(point1)
#     coords_2 = float(point2)
#     return geopy.distance.geodesic(coords_1, coords_2).km


# Fonction pour trier les positions par distance (matrice de distance)
matrix = [[distance(positions[i], positions[j]) for j in range(len(positions))] for i in range(len(positions))]
print("Matrice de distance :", matrix, "\n")


def totaldistance(path):
    total = 0
    for i in range(0, len(path) - 1):
        print(path[i], path[i+1])
        total += distance(path[i], path[i + 1])
        total = round(total, 4)
    return total


total = totaldistance(path)
print("La distance est égale à : ", total, "Km \n")

# Fonction du chemin le plus court non visité
def shortest_unvisited(current_town):
    visited[current_town] = True
    smallest = float("inf")
    i_smallest = 0

    for i in range(len(matrix)):
        if not visited[i]:
            if matrix[current_town][i] < smallest:
                smallest = matrix[current_town][i]
                i_smallest = i

    return i_smallest


shortest_unvisited(0)

# Index du chemin le plus court pour chaque ville
current_index = 0
path.append(current_index)
for i in range(len(matrix)):
    index_town = shortest_unvisited(current_index)
    # print("Ceci est l'index du chemin le plus court ", index_town)
    path.append(index_town)
    current_index = index_town

print("Résultat du plus proche voisin :", path, "\n")


# ALGO 2-OPT____________________________________________________________________________________________________________
def swap(list):
    temp = []
    while list:
        temp.append(list.pop())
    return temp


# # Fonction qui récupère un csv et le transforme en objet python
# def loadFile():
#     positions.clear()
#     with open('DataGPS/70villes.csv') as file:
#         csvreader = csv.reader(file)
#         next(csvreader)  # skip header line
#         for row in csvreader:
#             lat = float(row[0])
#             lon = float(row[1])
#             positions.append([lat, lon])
#     return positions


# AFFICHAGE

m = folium.Map([45.166672, 5.71667], tiles="cartodb positron", zoom_start=14)

# Point de départ le Campus
folium.Marker(
    location=[45.184599534292026, 5.731326584660483],
    tooltip="Le Campus Numérique",
    icon=folium.Icon(color="red", icon=""),
).add_to(m)

# Ajout des marqueurs sur la map
for index, position in enumerate(positions):
    folium.Marker(
        location=[position[0], position[1]],
        tooltip=str(index),
        icon=folium.Icon(color="green", icon="cloud"),
    ).add_to(m)


# Ajout de la polyline pour connecter les points via des paramètres directement dedans
def chemin(currentpath):
    polylinepath = []
    for i in currentpath:
        coordinate = positions[i]
        latitude = coordinate[0]
        longitude = coordinate[1]
        polylineCoordinate = (latitude, longitude)
        polylinepath.append(polylineCoordinate)

    polyline = folium.PolyLine(
        locations=polylinepath, color='grey')
    polyline.add_to(m)


chemin(path)

m.save("index.html")
