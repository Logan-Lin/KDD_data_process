from csv_process import csv_write
from data_export import current_data_fetch
from utility import data_regularization


aq_row = ["PM2.5", "PM10", "NO2", "CO", "O3", "SO2"]
head_row = ["aq_station", "time"] + aq_row + ["temperature", "pressure", "humidity", "wind_direction", "wind_speed"]
for i in range(34):
    head_row.append("near_aq_factor_" + str(i))
    head_row = head_row + aq_row


def fetch_period_train_sets(station_id, start_time, end_time):
    data_matrix = []
    for time_string in data_regularization.get_time_string(start_time, end_time):
        try:
            data_matrix.append(current_data_fetch.fetch_train_set(station_id, time_string))
            print("Finished fetching", station_id, time_string, "data")
        except:
            print("Data loss at", time_string)
    return data_matrix


data_matrix = fetch_period_train_sets("aotizhongxin_aq", "2017-06-01 00:00:00", "2017-06-01 23:00:00")
csv_write.write_csv(head_row, data_matrix, "test.csv")
