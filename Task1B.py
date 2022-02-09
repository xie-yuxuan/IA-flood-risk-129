
from floodsystem.stationdata import build_station_list
from floodsystem.haversine import haversine
from floodsystem.geo import station_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key  # noqa

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    #introduce the coordinates p
    p = (52.2053, 0.1218)

    #list of stations from near to far
    staList = []
    staList = station_by_distance(stations, p)
    print('the 10 closest entries:', staList[:10])
    print('the 10 furthest entries:', staList[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()



    


