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
#from . import datafetcher
from floodsystem.datafetcher import fetch, fetch_latest_water_level_data,\
     fetch_measure_levels, fetch_station_data, dump, load

def station_by_distance(stations, p):
    stations = build_station_list()
    d_list = []
    for station in stations:
        names = station.name
        distance = haversine(p, station.coord)
        d_tuple = (names, distance)
        d_list.append(d_tuple)
    return d_list
    

def station_within_radius(stations, centre, r):
    stations = build_station_list()
    r_list = []
    r = haversine(centre, station.coord)
    for station in stations:
        names = station.name
        distance = haversine(centre, station.coord)
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
        rs_list.append(names)
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
    return sr_dict

