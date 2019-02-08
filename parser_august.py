"""
Parse through files with Divvy raw data.
Group trips by day in order to average trip time.
"""

import csv
import pandas as pd
from statistics import mean

# create place to store ride durations for each day
sun_times = []
mon_times = []
tues_times = []
wed_times = []
thurs_times = []
fri_times = []
sat_times = []

# dictionary of dates and lists so that
# loop below can classify ride duration by day
date_dict = {
    '8/12/2017': sat_times,
    '8/11/2017': fri_times,
    '8/10/2017': thurs_times,
    '8/9/2017': wed_times,
    '8/8/2017': tues_times,
    '8/7/2017': mon_times,
    '8/6/2017': sun_times
}

# open CSV containing all trip data from February 4-10, 2018
with open('Divvy_Trips_2017_Aug0612.csv') as csvfile:
    divvy_week = csv.DictReader(csvfile)
    for row in divvy_week:
        # grab date of ride from start time
        ride_date = dict(row)['start_time'].split()[0]
        # grab length of ride and turn into integer
        ride_length = int(dict(row)['tripduration'])
        # use ride date to fetch appropriate list from dict, append ride length
        date_dict[ride_date].append(ride_length)


day_lists = [sun_times, mon_times, tues_times, wed_times,
             thurs_times, fri_times, sat_times]
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']
avg_ride_times = []

for day in day_lists:
    daily_average = round(mean(day) / 60, 1)
    avg_ride_times.append(daily_average)

d = {'day': days, 'ride_length': avg_ride_times}
df = pd.DataFrame(data=d)
df.to_csv('avgs_aug17.csv', index=False)
