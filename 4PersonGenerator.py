from tkinter import *
import tkinter as tk
import csv
import os.path
import random
import subprocess
import time


options = ["AK","AZ","CO","HI","ID","MT","NV","OR","UT","WA"]
x = random.randint(0, 9)

#opening a new file with state and year info for population microservice
with open('inputState.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["input_state", "input_year"])
    writer.writerow([options[x], "2019"])

#runs population microservice
subprocess.run("python micropractice.py", shell=True)
#subprocess.run("python dem.py", shell=True)

#pauses person microservice until stateFile is written
while not os.path.exists('stateFile.csv'):
    time.sleep(1)

#opening file made by population microservice with state and population information in 2019
with open('stateFile.csv', 'r') as file:  # code referenced from: https://www.programiz.com/python-programming/csv
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        state = line[0]
        pop = int(line[1])

stateFile = state + '.csv'
with open('address_data/' + stateFile, 'r') as file:  #code referenced from: https://www.programiz.com/python-programming/csv
    all_data = csv.reader(file)
    next(all_data)
    with open('outputFinal.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["input_state","input_number_to_generate","output_content_type","output_content_value"])
        data = []
        for line in all_data:
            data.append(line)
        count = pop *.01
        while count >0:
            x = random.randint(1, 280000)
            writer.writerow([state, count, "street address", data[x][2] + " " + data[x][3] + data[x][4] + data[x][5] + data[x][6] + data[x][7] + " " + data[x][8]])
            count -=1