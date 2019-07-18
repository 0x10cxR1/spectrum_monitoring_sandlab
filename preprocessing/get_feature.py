"""
	Extract features from USRP data (normalization)
"""
import sys, os
import glob
import numpy as np 


def max_min(sequence, max_data, min_data):
	"""
		max-min normalization
	"""
	# max_data = max(sequence)
	# min_data = min(sequence)
	gap = max_data - min_data
	if gap == 0:
		raise Exception('Bad data')
		#ret = [1 for i in range(len(sequence))]
	else:
		ret = []
		for i in range(len(sequence)):
			ret.append((sequence[i] - min_data)/gap)
	return ret


def standard(sequence, mean_data, std_data):
	"""
		standard normalization
	"""
	# mean_data = np.mean(sequence)
	# std_data = np.std(sequence)
	if std_data == 0:
		raise Exception('Bad data')
		#ret = [1 for i in range(len(sequence))]
	else:
		ret = []
		for i in range(len(sequence)):
			ret.append((sequence[i] - mean_data)/std_data)
	return ret



def extract_method1(filename, out, timestamps, predict_len):
	"""
		extarct method I: w/o normalization
	"""
	data = []
	with open(filename, 'r') as f:
		for line in f:
			a = line.split()
			data.extend([float(a[i]) for i in range(len(a))])
			if len(data) == (timestamps + predict_len)*128:
				for d in data:
					out.write('%s ' %d)
				out.write('\n')

				"""
					to sample more data
				"""
				data = []



def extract_method2(filename, out, timestamps, predict_len):
	"""
		extarct method II: w/ max-min normalization
	"""
	data = []
	with open(filename, 'r') as f:
		for line in f:
			a = line.split()
			data.extend([float(a[i]) for i in range(len(a))])
			if len(data) == timestamps*128:
				max_data = max(data)
				min_data = min(data)
			if len(data) == (timestamps + predict_len)*128:
				data = max_min(data, max_data, min_data)
				for d in data:
					out.write('%s ' %d)
				out.write('\n')

				"""
					to sample more data
				"""
				data = []



def extract_method3(filename, out, timestamps, predict_len):
	"""
		extarct method III: w/ standard normalization
	"""
	data = []
	with open(filename, 'r') as f:
		for line in f:
			a = line.split()
			data.extend([float(a[i]) for i in range(len(a))])
			if len(data) == timestamps*128:
				mean_data = np.mean(data)
				std_data = np.std(data)
			if len(data) == (timestamps + predict_len)*128:
				data = standard(data, mean_data, std_data)
				for d in data:
					out.write('%s ' %d)
				out.write('\n')

				"""
					to sample more data
				"""
				data = []



def main():
	"""
		use the previous 100 (100*128) spectrum to predict the next 25 (25*128) spectrum
	"""
	path = sys.argv[1]
	band = sys.argv[2]
	out = open(sys.argv[3], 'w')
	method = int(sys.argv[4])
	timestamps = 100
	predict_len = 25
	for filename in glob.glob(path+'*'+band+'*.txt'):
		print(filename)
		if method == 1:
			extract_method1(filename, out, timestamps, predict_len)
		elif method == 2:
			extract_method2(filename, out, timestamps, predict_len)
		else:
			extract_method3(filename, out, timestamps, predict_len)


if __name__ == '__main__':
    main()
