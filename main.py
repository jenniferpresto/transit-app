from nyct_gtfs import NYCTFeed
from datetime import datetime, timedelta
import json

# References:
# Library: https://github.com/Andrew-Dickinson/nyct-gtfs?tab=readme-ov-file
# Google: https://developers.google.com/transit/gtfs-realtime/examples/vehicle-positions

with open("config.json") as config_file:
    config_json = json.load(config_file)
    print(str(config_json))
    HOME_STATION_ID = config_json["home_station"]
    TRAIN_1 = config_json["train_1"][0]
    TRAIN_2 = config_json["train_2"][0]
    LINE_IDS_1 = config_json["train_1"]
    LINE_IDS_2 = config_json["train_2"]

print("Home station: {}".format(HOME_STATION_ID))

def get_trains():
    current_time = datetime.now()
    print(current_time)
    feed1 = NYCTFeed(TRAIN_1)
    trains1 = feed1.filter_trips(line_id=LINE_IDS_1, headed_for_stop_id=[HOME_STATION_ID])
    feed2 = NYCTFeed(TRAIN_2)
    trains2 = feed2.filter_trips(line_id=LINE_IDS_2, headed_for_stop_id=[HOME_STATION_ID])
    print("Num trains: {}".format(len(trains1)))
    if len(trains1):
        print("Next train: {}".format(str(trains1[0])))
        print("{} remaining stops".format(len(trains1[0].stop_time_updates)))
    future_stops_1 = []
    future_stops_2 = []

    for train in trains1:
        for stop in train.stop_time_updates:
            if stop.stop_id == HOME_STATION_ID and stop.arrival > current_time:
                print(str(stop))
                future_stops_1.append(stop)
                continue

    for train in trains2:
        for stop in train.stop_time_updates:
            if stop.stop_id == HOME_STATION_ID and stop.arrival > current_time:
                print(str(stop))
                future_stops_2.append(stop)
                continue

    future_stops_1.sort(key=lambda x: x.arrival)
    future_stops_2.sort(key=lambda x: x.arrival)
    print("Future trains on lines {}".format(LINE_IDS_1))
    for stop in future_stops_1:
            time_remaining = stop.arrival - current_time
            print("arrival time: {}, remaining: {}, which is {} seconds".format(stop.arrival, timedelta(seconds=round(time_remaining.total_seconds())), round(time_remaining.total_seconds())))
    
    print("\nFuture trains on lines {}".format(LINE_IDS_2))
    for stop in future_stops_2:
            time_remaining = stop.arrival - current_time
            print("arrival time: {}, remaining: {}, which is {} seconds".format(stop.arrival, timedelta(seconds=round(time_remaining.total_seconds())), round(time_remaining.total_seconds())))


if __name__ == "__main__":
    get_trains()