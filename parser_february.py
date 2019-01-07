"""
Parse through files with Divvy raw data.
Group trips by day in order to average trip time.
"""

import csv
from statistics import mean

sun_times = []
mon_times = []
tues_times = []
wed_times = []
thurs_times = []
fri_times = []
sat_times = []

date_dict = {
    '2018-02-04': sun_times,
    '2018-02-05': mon_times,
    '2018-02-06': tues_times,
    '2018-02-07': wed_times,
    '2018-02-08': thurs_times,
    '2018-02-09': fri_times,
    '2018-02-10': sat_times
}

with open('Divvy_Trips_2018_Feb0410.csv') as csvfile:
    divvy_week = csv.DictReader(csvfile)
    for row in divvy_week:
        # grab date from start time
        ride_date = dict(row)['Local Start Time'].split()[0]
        ride_length = float(dict(row)['Duration In Seconds Uncapped'].replace(',',''))
        date_dict[ride_date].append(ride_length)

with open("averages_february18.csv", mode="w") as csv_file:
    avg_writer = csv.writer(
        csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    avg_writer.writerow(["Sunday", round(mean(sun_times) / 60, 1)])
    avg_writer.writerow(["Monday", round(mean(mon_times) / 60, 1)])
    avg_writer.writerow(["Tuesday", round(mean(tues_times) / 60, 1)])
    avg_writer.writerow(["Wednesday", round(mean(wed_times) / 60, 1)])
    avg_writer.writerow(["Thursday", round(mean(thurs_times) / 60, 1)])
    avg_writer.writerow(["Friday", round(mean(fri_times) / 60, 1)])
    avg_writer.writerow(["Saturday", round(mean(sat_times) / 60, 1)])
