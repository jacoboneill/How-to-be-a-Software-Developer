import sys
import os

url = f"{sys.argv[2]}&t="
fp = sys.argv[1]

with open(fp) as f:
    times = [[int(intt) for intt in t.split(':')] for t in f.readlines()]
    for time in times:
        seconds = (time[0] * 60 + time[1])*60 + time[2]
        print(f'[ Chapter]({url}{seconds}s)')


# seconds = (int(time[0])*60 + int(time[1]))*60 + int(time[2])

# print(seconds)