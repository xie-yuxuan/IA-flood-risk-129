
from floodsystem.stationdata import build_station_list
from floodsystem.haversine import haversine
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem import datafetcher

def station_by_distance(stations, p):
    stations = build_station_list()
    d_list = []
    for station in stations:
        names = station.name
        distance = haversine(p, station.coord)
        d_tuple = (names, distance)
        d_list.append(d_tuple)
    d_list.sort()
    return d_list

p = (10.234, 57.896)
stations = build_station_list()
Station_list = []
for station in stations:
        names = station.name
        coords = station.coord
        distance = haversine(p, coords)
        towns = station.town
        tuples = (names, towns, distance)
        Station_list.append(tuples)
Station_list = sorted_by_key(Station_list, 2)
print('the 10 closest entries:', Station_list[:10])
print('the 10 furthest entries:', Station_list[-10:])



    


