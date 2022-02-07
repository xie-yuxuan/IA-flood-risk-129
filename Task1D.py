from floodsystem.stationdata import build_station_list
from floodsystem.haversine import haversine
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.datafetcher import fetch, fetch_latest_water_level_data,\
     fetch_measure_levels, fetch_station_data, dump, load
from floodsystem.geo import station_by_distance, stations_by_river, \
    rivers_with_station


stations = build_station_list()
x = 0
river_list = []
for station in stations:
    rivers = station.river
    if len(geo.rivers_with_station(station)) == 1:
        x += 1
        river_list.append(rivers)
    else:
        continue
river_list.sort()
print(river_list[:10])

for station in stations:
    if station.name in ['River Aire', 'River Cam', 'River Thames']:
        Aire = (geo.stations_by_river['River Aire'])
        Cam = (geo.stations_by_river['River Cam'])
        Thames = (geo.stations_by_river['River Thames'])
        Aire.sort()
        Cam.sort()
        Thames.sort()
        print ('River Aire:', Aire)
        print ('River Cam:', Cam)
        print ('River Thames:', Thames)


