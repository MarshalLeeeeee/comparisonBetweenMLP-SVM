from sklearn import svm
import numpy as np
from glob import glob

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
	'SVHN'
]
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

def readData(path):
	data = np.load(path)
	label = data[:,0]
	data = data[:,1:]
	return data,label

def min(a,b):
	if a < b:
		return a
	else:
		return b

if __name__ == '__main__':
	X = np.array([[1,1,1],[0,0,0]])
	label = X[:,0]
	data = X[:,1:]
	clf = svm.SVC()
	clf.fit(data,label)
	pred = clf.predict(data)
	print(label.shape)
	print(data.shape)


	for i in range(8,9):
		target = targets[i]
		data_dir = path + target
		print('******************************')
		print('data dir: ',data_dir)
		print('------------------------------')

		train_path = glob(data_dir+'/*-train.npy')[0]
		test_path = glob(data_dir+'/*-test.npy')[0]
		train_data,train_label = readData(train_path)
		test_data,test_label = readData(test_path)
		d = int(train_data.shape[1])
		
		# kernel: linear, poly, rbf, sigmoid
		# degree (for poly)
		for kernel in kernels:
			print('kernel used: ', kernel)
			clf = svm.SVC(kernel = kernel)
			if kernel == 'poly':
				clf.degree = min(50,d/2)
			print('start to fit...')
			clf.fit(train_data,train_label)
			print('fitting finished...')
			print('start to predict...')
			pred = clf.predict(test_data)
			print('predict finished...')
			accu = (pred == test_label).astype(np.float32)
			accu_rate = np.sum(accu) / test_label.shape[0]
			print('accuracy rate is ', accu_rate)