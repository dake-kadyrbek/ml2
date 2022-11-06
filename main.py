import pandas as pd, numpy as np
import random, requests
from bs4 import BeautifulSoup
from faker import Faker
import string
import csv

def randomString(stringLength = 15):
    l = string.ascii_lowercase
    return ''.join(random.choice(l) for i in range(stringLength))

def create_dataset():
	className = ['class1','class2','class3']
	data = []

	names = 1500

	for n in range(names):
		row = [randomString(), random.choice(className),  n + np.random.normal(0, 0.2), n + np.random.normal(0, 0.2), n + np.random.normal(0, 0.2), n]
		data.append(row)
		random.shuffle(data)

	_data = ""

	for d in data:
		_data += str(d) + "\n"

	file1 = open("file.txt", "w")
	file1.writelines(_data)
	file1.close()

	print(_data)

if __name__=='__main__':
	create_dataset()
