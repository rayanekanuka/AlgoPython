import csv

import folium
import math

positions = [
    {"lat": 45.171112, "lng": 5.695952},
    {"lat": 45.183152, "lng": 5.699386},
    {"lat": 45.174115, "lng": 5.711106},
    {"lat": 45.176123, "lng": 5.722083},
    {"lat": 45.184301, "lng": 5.719791},
    {"lat": 45.184252, "lng": 5.730698},
    {"lat": 45.170588, "lng": 5.716664},
    {"lat": 45.193702, "lng": 5.691028},
    {"lat": 45.165641, "lng": 5.739938},
    {"lat": 45.178718, "lng": 5.744940},
    {"lat": 45.176857, "lng": 5.762518},
    {"lat": 45.188512, "lng": 5.767172},
    {"lat": 45.174017, "lng": 5.706729},
    {"lat": 45.174458, "lng": 5.687902},
    {"lat": 45.185110, "lng": 5.733667},
    {"lat": 45.185702, "lng": 5.734507},
    {"lat": 45.184726, "lng": 5.734666},
    {"lat": 45.184438, "lng": 5.733735},
    {"lat": 45.184902, "lng": 5.735256},
    {"lat": 45.174812, "lng": 5.698095},
    {"lat": 45.169851, "lng": 5.695723},
    {"lat": 45.180943, "lng": 5.698965},
    {"lat": 45.176205, "lng": 5.692165},
    {"lat": 45.171244, "lng": 5.689872}
]

visited = [False] * len(positions)

print("Voici les points GPS")
print(positions)


# Fonction pour calculer les distances entre deux points
def distance(point1, point2):
    fx = point1["lat"] - point2["lat"]
    fy = point1["lng"] - point2["lng"]
    return math.sqrt(fx * fx + fy * fy)


# Fonction pour trier les positions par distance (matrice de distance)
matrix = [[distance(positions[i], positions[j]) for j in range(len(positions))] for i in range(len(positions))]

print(matrix)
print("--------------------------")


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

# Index de la plus petite distance à index non visité
current_index = 0
for i in range(len(matrix)):
    index_town = shortest_unvisited(current_index)
    print("Ceci est l'index du chemin le plus court ", index_town)
    current_index = index_town


def loadFile():
    positions.clear()
    with open('DataGPS/70villes.csv') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            lat = float(row[0])
            lon = float(row[1])
            positions.append([lat, lon])
    return positions


# AFFICHAGE

m = folium.Map([45.184644905978466, 5.731326584660483], zoom_start=14)

folium.Marker(
    location=[45.184599534292026, 5.731326584660483],
    tooltip="Le Campus Numérique",
    # popup="Le Campus Numérique",
    icon=folium.Icon(color="red", icon=""),
).add_to(m)

m.save("index.html")