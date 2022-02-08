from floodsystem.geo import station_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.haversine import haversine
#from floodsystem.station import MonitoringStation
#from floodsystem.utils import sorted_by_key  # noqa
#from floodsystem import datafetcher

# def station_by_distance(stations, p):
#     stations = build_station_list()
#     d_list = []
#     for station in stations:
#         names = station.name
#         distance = haversine(p, station.coord)
#         d_tuple = (names, distance)
#         d_list.append(d_tuple)
#     d_list.sort()
#     return d_list

# centre = (52.2053, 0.1218)
# r = 10
stations = build_station_list()
# Station_list = []
# lon1, lat1 = p[0],p[1]
print(station_within_radius(stations, (52.2053, 0.1218), 10))