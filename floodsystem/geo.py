# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
from .haversine import haversine
from .station import MonitoringStation
from .datafetcher import fetch, fetch_latest_water_level_data,\
     fetch_measure_levels, fetch_station_data, dump, load

def station_by_distance(stations, p):
    stations = build_station_list()
    d_list = []
    lon1, lat1 = p[0],p[1]
    for station in stations:
        names = station.name
        coords = station.coord
        lon2, lat2 = coords[0], coords[1]
        distance = haversine(lon1, lat1, lon2, lat2)
        d_tuple = (names, distance)
        d_list.append(d_tuple)
        d_list = sorted_by_key(d_list, 1)
    return d_list
    

def station_within_radius(stations, centre, r):
    stations = build_station_list()
    r_list = []
    lon1, lat1 = centre[0],centre[1]
    for station in stations:
        names = station.name
        coords = station.coord
        lon2, lat2 = coords[0], coords[1]
        distance = haversine(lon1, lat1, lon2, lat2)
        if distance <= r:
            r_list.append(names)
        else:
            continue
    return r_list


def rivers_with_station(stations):
    stations = build_station_list()
    rs_list = []
    for station in stations:
        rivers = station.river
        rs_list.append(rivers)
    rs_list.sort()
    river_list = set(rs_list)
        # if rivers in rs_list:
        #     continue
        # else:
        #     rs_list.append(rivers)
    return river_list


def stations_by_river(stations):
    sr_dict = {}
    for station in stations:
        rivers = station.river
        names = station.name
        if rivers in sr_dict:
            sr_dict[rivers].append(names)
            sr_dict[rivers].sort()
        else:
            sr_dict[rivers] = [names]
    return (sr_dict)



#Task1E
def rivers_by_station_number(stations, N):

    #dictionary in which key = river, value = station_no
    rivers_station_no = {}

    #for loop to cycle through all stations, adding a key value pair of river and station no
    for station in stations:
        if station.river in rivers_station_no:
            rivers_station_no[station.river] += 1
        else:
            rivers_station_no[station.river] = 1

    #sort the dictionary to give river with descending order of station no
    rivers_station_no = sorted(rivers_station_no.items(), key=lambda x:x[1], reverse=True)

    #appending top 9 rivers with most number of station
    river_list = []
    count = 0
    for x in range(9):
        if count <= N:
            river_list.append(list(rivers_station_no)[x])
            count += 1

    #cycle through all rivers, adding rivers with station number same as rank 9 river
    for pair in rivers_station_no:
        if pair[-1] == river_list[-1][-1]:
            river_list.append(pair)

    #remove river at index 8 (rank 9) to remove double count
    river_list.pop(8)

    return river_list