import pickle
import numpy as np
from sklearn import svm
from sklearn import linear_model
import matplotlib.pyplot as plt

path = '/home/marshallee/Documents/classification/data/cifar/cifar-10-batches-py/'
fileList = ['data_batch_1','data_batch_2','data_batch_3','data_batch_4','data_batch_5','test_batch']

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

if __name__ == '__main__':
	data_batch = []
	for i in range(5):
		file_path = path + fileList[i]
		data_batch.append(unpickle(file_path))
	test_batch = unpickle(path + fileList[5])
	
	train_data = np.concatenate((np.array(data_batch[0][b'data']),np.array(data_batch[1][b'data'])),axis = 0)
	train_label = np.concatenate((np.array(data_batch[0][b'labels']),np.array(data_batch[1][b'labels'])),axis = 0)
	for i in range(2,5):
		train_data = np.concatenate((train_data,np.array(data_batch[i][b'data'])),axis = 0)
		train_label = np.concatenate((train_label,np.array(data_batch[i][b'labels'])),axis = 0)
	print(train_data.shape)
	print(train_label.shape)

	test_data = np.array(test_batch[b'data'])
	test_label = np.array(test_batch[b'labels'])
	print(test_data.shape)
	print(test_label.shape)

	'''
	demo_pic = np.reshape(train_data[1],(3,32,32))
	demo_pic_red = demo_pic[0][:,:,np.newaxis]
	demo_pic_green = demo_pic[1][:,:,np.newaxis]
	demo_pic_blue = demo_pic[2][:,:,np.newaxis]
	demo = np.concatenate((demo_pic_red,demo_pic_green,demo_pic_blue),axis=2)
	print(demo.shape)
	plt.imshow(demo)
	plt.axis('off')
	plt.show()
	exit(0)
	'''
	
	#clf = svm.SVC(cache_size = 2048)
	#clf.fit(train_data[:20000],train_label[:20000])

	clf = linear_model.SGDClassifier(alpha=1e-2)
	for i in range(5000):
		clf.partial_fit(train_data[(i%500)*100:(i%500+1)*100],train_label[(i%500)*100:(i%500+1)*100],classes = np.unique(train_label))
	pred = clf.predict(test_data)
	accuracy = np.mean((pred == test_label).astype(np.float32))
	print('accuracy: ', accuracy)