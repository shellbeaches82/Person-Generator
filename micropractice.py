import os.path
import csv
import time
import random
from tkinter import *
import tkinter as tk


with open("inputState.csv", 'r') as file:
    data = csv.reader(file)


with open('stateFile.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["state", "pop"])
    writer.writerow(['ak', "29000"])
