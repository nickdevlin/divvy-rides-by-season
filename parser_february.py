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
    '2018-02-04': sun_times,
    '2018-02-05': mon_times,
    '2018-02-06': tues_times,
    '2018-02-07': wed_times,
    '2018-02-08': thurs_times,
    '2018-02-09': fri_times,
    '2018-02-10': sat_times
}

# open CSV containing all trip data from February 4-10, 2018
with open('Divvy_Trips_2018_Feb0410.csv') as csvfile:
    divvy_week = csv.DictReader(csvfile)
    for row in divvy_week:
        # grab date of ride from start time
        ride_date = dict(row)['Local Start Time'].split()[0]
        # grab length of ride and turn into integer
        ride_length = float(dict(row)['Duration In Seconds'].replace(',', ''))
        # use ride date to fetch appropriate list from dict, append ride length
        date_dict[ride_date].append(ride_length)

# set up lists for pandas use
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
df.to_csv('avgs_feb18.csv', index=False)
