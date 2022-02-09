from floodsystem.stationdata import build_station_list
from floodsystem.haversine import haversine
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.geo import stations_by_river, rivers_with_station

def run():
    """Requirements for Task 1A"""

    #part a
    # Build list of stations
    stations = build_station_list()

    #list of rivers with at least one station
    r_list = list(rivers_with_station(stations))

    #number of the rivers
    print(len(r_list))

    #the names of first the rivers
    print(r_list[:10])


    #part b
    #dictionary of rivers with their monitoring stations
    sta = stations_by_river(stations)

    #find the wanted rivers by their names
    print ('River Aire:', sta['River Aire'])
    print ('River Cam:', sta['River Cam'])
    print ('River Thames:', sta['River Thames'])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()


