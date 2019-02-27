import numpy as np
import os
import re
import random

path = '/home/marshallee/Documents/classification/data/'
targets = [
	'cod-ma',
	'leukemia',
	'liver-disorders',
	'rcv1-multiclass',
	'real-sim',
	'dna',
	'shuffle',
	'vowel',
	'sector',
	'SVHN'
]
normFlag = [True,True,True,True,True,True,False,False,False,False]
feature = [9,7130,6,47237,20959,181,10,11,55198,3073]
probs = [1.0,1.0,1.0,0.02,0.5,1.0,1.0,1.0,1.0,1.0]


def makeData(path, dimension, norm = True, prob = 1.0):

	# collect the data
	data = []
	fileList = os.listdir(path)
	pattern = re.compile('[0-9]+:')
	for file in fileList:
		print(file)
		with open(os.path.join(path,file),'r') as f:
			cnt = 0
			for line in f.readlines():
				r = random.random()
				if(r > prob):
					continue
				#line = re.sub(pattern,'',line)
				line = re.sub('\n','',line)
				line = re.sub('  ',' ',line)
				line = re.sub(' $','',line)
				line = re.sub(':',' ',line)
				line = '0 '+ line
				line = line.split(' ')
				#print(line)
				#print('len: ', len(line))
				subdata = np.zeros(dimension)
				for n in range(int(len(line)/2)):
					subdata[int(line[2*n])] = float(line[2*n+1])
				#data.append(line)
				data.append(subdata)
				cnt += 1
				if (cnt % 5000 == 0):
					print('cnt: ',cnt)
				#print(len(line))
	data = np.array(data)
	print('read finished...')

	# sort data according to the class
	print(data)
	print(data[0])
	print(data[0].shape)
	
	data = data[data[:,0].argsort()]
	classType = np.unique(data[:,0])
	print(classType)

	# count the sample number of each class
	classNum = np.zeros(classType.shape[0])
	for i in range(classType.shape[0]):
		classNum[i] =  np.sum(classType[i] == data[:,0])
	print(classNum)

	# normalize
	if norm:
		mean = np.mean(data,axis=0)
		mean[0] = 0
		std = np.std(data,axis=0)
		std[0] = 1
		std = std + (std==0).astype(np.float32)
		data = (data-mean) / std
	print('normalize finished...')

	# segment train and test data and save
	prop = 0.9
	trainData = data[:int(classNum[0]*prop),:]
	testData = data[int(classNum[0]*prop):int(classNum[0]),:]
	print(trainData.shape[0])
	print(testData.shape[0])
	step = int(classNum[0])
	for i in range(1,len(classNum)):
		trainData = np.concatenate((trainData,data[step:step+int(classNum[i]*prop),:]),axis=0)
		testData = np.concatenate((testData,data[step+int(classNum[i]*prop):step+int(classNum[i]),:]),axis=0)
		step += int(classNum[i])
	print(trainData.shape[0])
	print(testData.shape[0])
	fileName = path.split('/')[-1]
	print(fileName)
	np.random.seed(233)
	np.random.shuffle(trainData)
	np.random.seed(233)
	np,random.shuffle(testData)
	np.save(os.path.join(path,fileName+'-train.npy'),trainData[:720])
	np.save(os.path.join(path,fileName+'-test.npy'),testData[:80])
	print('save finished...')

	return (data,classType,classNum)

if __name__ == '__main__':

	x = [[1,2,3],[5,4,7],[8,7,1]]
	y = [1,2,0,2,0,0,0,1]
	x = np.array(x)
	y = np.array(y)
	print(np.mean(x,axis=0))
	print(x - np.mean(x,axis=0))
	print((y == 0).astype(np.float32))

	'''
	for i in range(8):
		data,classType,classNum = makeData(path+targets[i],normFlag[i])
	'''
	i = -1
	data,classType,classNum = makeData(path+targets[i],feature[i],normFlag[i],probs[i])
