from sklearn.neural_network import MLPClassifier
import numpy as np
from glob import glob
import time

path = '/home/marshallee/Documents/classification/data/'
targets = [
	'cod-ma',
	'leukemia',
	'liver-disorders',
	'sector',
	'dna',
	'shuffle',
	'vowel',
	'SVHN'
]
solvers = ['lbfgs','sgd', 'adam']
actives = ['identity', 'logistic', 'tanh', 'relu']

def readData(path):
	data = np.load(path)
	label = data[:,0]
	data = data[:,1:]
	return data,label



if __name__ == '__main__':
	X = np.array([[0,0],[1,1]])
	y = np.array([0,1])
	clf  = MLPClassifier(solver = 'lbfgs', alpha = 1e-5, hidden_layer_sizes = (5,2), random_state = 1)
	clf.fit(X,y)
	print(clf.predict([[-1,-1],[2,2]]))

	'''
	for target in targets:
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
	'''

	clip = 10
	for target in targets[7:8]:
		data_dir = path + target
		print('****************************')
		print('target: ', target)
		train_path = glob(data_dir+'/*-train.npy')[0]
		test_path = glob(data_dir+'/*-test.npy')[0]
		train_data,train_label = readData(train_path)
		test_data,test_label = readData(test_path)
		'''np.random.seed(233)
								np.random.shuffle(train_data)
								np.random.seed(233)
								np.random.shuffle(train_label)
								np.random.seed(233)
								np.random.shuffle(test_data)
								np.random.seed(233)
								np.random.shuffle(test_label)'''
		d = int(train_data.shape[1])
		print('train num: ',train_data.shape[0])
		print('test num: ', test_data.shape[0])
		print('dimension: ',train_data.shape[1])
		'''trainData = train_data[:clip]
								trainLabel = train_label[:clip]
								testData = test_data[:1]
								testLabel = test_label[:1]
								del train_data
								del train_label
								del test_data
								del test_label'''

		for active in actives:
			print('-------------------------')
			print('active is: ', active)
			clf = MLPClassifier(solver = 'adam', activation = active, learning_rate = 'adaptive', alpha = 1e-5, hidden_layer_sizes = (100,), random_state = 1, max_iter = 2000)
			start_time = time.time()
			print('start to fit...')
			clf.fit(train_data[:100],train_label[:100])
			#clf.fit(trainData,trainLabel)
			print('fitting finished...')
			print('time for fitting (s): ',time.time()-start_time)
			print('start to predict...')
			pred = clf.predict(test_data)
			print('predict finished...')
			accu = (pred == test_label).astype(np.float32)
			accu_rate = np.sum(accu) / test_label.shape[0]
			print('accuracy rate is ', accu_rate)