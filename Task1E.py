from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Implement a function that determines the N rivers with the greatest number of monitoring stations"""

    #List of stations
    stations = build_station_list()

    #Print a list of N rivers with greatest number of monitoring systems
    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()