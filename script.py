import pandas as pd
import glob
import sys

present = 0
roll_number = sys.argv[1]
total_days = 0

for filename in glob.glob('*.csv'):
    df = pd.read_csv(filename, names = ['Roll Number', 'Time'], encoding = 'utf_16_le')
    number = df['Roll Number'].str.find(roll_number).values
    if 0 in number:
        present += 1
    
    total_days += 1
    
percentage_present = (present / total_days) * 100

f = open('present.txt', mode='w+')
f.write("Number of days present: " + str(present) + "\n")
f.write("Attendance Percentage: " + str(percentage_present) + " %")
f.close()