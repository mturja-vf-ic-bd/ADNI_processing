from sys import argv
import os
from os.path import isfile, join
from matplotlib import pyplot as plt
import numpy as np

mat_list = []
os.chdir(argv[1])
files = [f for f in os.listdir(os.getcwd()) if isfile(f)]
nFile = len(files)

for file in files:
	print file
	a = []
	fin = open(join(os.getcwd(), file), 'r')
	for line in fin.readlines():
		a.append( [ float(x) for x in line.split()] )

	a = np.asmatrix(a)
	dim = np.size(a)
	mat_list.append(a.flatten().tolist())

element_list = [[mat_list[i][0][j] for i in range(0, nFile)] for j in range(0, dim)]
std_dev = [np.std(element_list[i]) for i in range(0, dim)]

bins =  [i * 50 for i in range(0, 100)]
hist, bins = np.histogram(std_dev, bins)
plt.hist(std_dev, bins = bins)
plt.title("Seed variance")
plt.show()


