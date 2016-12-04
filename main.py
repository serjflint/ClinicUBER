import mysql.connector
import numpy as np

time_range = 30

def build_graph(trip, current_trips):
    vertices = []
    for st in current_trips:
        if st[1] == trip[1]:
            vertices.append(st)

    l = len(vertices)
    edges = np.zeros([l, l + 1])
    for i in range(l):
        for j in range(l):
            if i != j:
                edges[i, j] = googleAPI.getDistance(vertices[i][0], vertices[j][0])
        edges[i, l] = googleAPI.getDistance(vertices[i][0], vertices[i][1])

    return {
        'v' : vertices,
        'e' : edges
    }

cnx = mysql.connector.connect(user='user', password="password", database='database')
cursor = cnx.cursor()

query = "SELECT capacity, location FROM cars "

cursor.execute(query)

locations = []
capacities = []
cars = []

for (capacity, location) in cursor:
    locations.append(location)
    capacities.append(capacity)

for i in range(16):
    cars.append(locations)

query = "SELECT start, end, appt FROM trips"

cursor.execute(query)

trips = []

for (start, end, appt) in cursor:
    trips.append([start, end, appt])

timelist = []
# make timelist
current_trips = []

for t in timelist:
    current_trips.clear()
    for trip in trips:
        if t - time_range < trip[2] <= t:
            current_trips.append(trip)
    for trip in current_trips:
        graph = build_graph(trip, current_trips)

        car_weight = []
        for car in cars:




cursor.close()
cnx.close()
