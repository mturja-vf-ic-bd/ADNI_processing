from sys import argv
import os
from os.path import isfile, join
from matplotlib import pyplot as plt
import numpy as np
import math

mat_list = []
os.chdir(argv[1])
files = [f for f in os.listdir(os.getcwd()) if isfile(f)]
files.sort()
files.sort(key=len)
nFile = len(files)

for file in files:
	print file
	a = []
	fin = open(join(os.getcwd(), file), 'r')
	for line in fin.readlines():
		a.append( [ float(x) for x in line.split()] )

	a = np.asmatrix(a)
	#a /= a.sum(axis = 1)
	mat_list.append(a)

distances = [] # Calculate euclidean distance from the first one to all the other ones
for i in range(1, len(mat_list)):
	d = np.power((mat_list[i] - mat_list[i-1]), 1)
	print d.sum()
	distances.append(d.sum())

plt.plot(distances)
plt.show()