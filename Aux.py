from random import randint, uniform
from copy import deepcopy
from sys import argv
import numpy as np

def BinSearch(prob,p,imin,imax):
	imid = (imin+imax)/2
	if imid == len(prob)-1 or imid == 0:
		return imid
	if p > prob[imid] and p <= prob[imid+1]:
		return imid+1
	elif p < prob[imid]:
		imid = BinSearch(prob,p,imin,imid)
	else:
		imid = BinSearch(prob,p,imid,imax)
	return imid

def Inputs (arqStr):
	arq = open(arqStr,"r")
	x, y = [], []
	for line in arq:
		lin = line.strip().split()
		x.append(map(float,lin[:-1]))
		y.append(lin[-1])
	return x,y