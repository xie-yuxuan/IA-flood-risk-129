from floodsystem.geo import station_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.haversine import haversine
from floodsystem.station import MonitoringStation

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    #station within 10 km from required coordinates
    print(station_within_radius(stations, (52.2053, 0.1218), 10))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()