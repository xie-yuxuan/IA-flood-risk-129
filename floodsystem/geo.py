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
    return d_list
    

def station_within_radius(stations, centre, r):
    stations = build_station_list()
    r_list = []
    lon1, lat1 = centre[0],centre[1]
    #coord = station.coord
    #r = haversine(centre, station.coord)
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
        names = station.name
        rivers = station.river
        rs_list.append(rivers)
        rs = set (rs_list)
    return rs


def stations_by_river(stations):
    stations = build_station_list()
    sr_list = []
    sr_dict = {}
    nameList = []
    riverList = []
    for station in stations:
        names = station.name
        rivers = station.river
        riverList.append(rivers)
        name_list = []
        for station in stations:
            if station.river == rivers:
                name_list.append(station.name)
            else:
                continue
        nameList.append(name_list)
    sr_dict = dict(zip(riverList, nameList))
    sr_dict = set(sr_dict)
    return sr_dict

