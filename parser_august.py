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
    '8/12/2017': sat_times,
    '8/11/2017': fri_times,
    '8/10/2017': thurs_times,
    '8/9/2017': wed_times,
    '8/8/2017': tues_times,
    '8/7/2017': mon_times,
    '8/6/2017': sun_times
}

with open('Divvy_Trips_2017_Aug0612.csv') as csvfile:
    divvy_week = csv.DictReader(csvfile)
    for row in divvy_week:
        # grab date from start time
        ride_date = dict(row)['start_time'].split()[0]
        ride_length = int(dict(row)['tripduration'])
        date_dict[ride_date].append(ride_length)

with open("averages_august17.csv", mode="w") as csv_file:
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
