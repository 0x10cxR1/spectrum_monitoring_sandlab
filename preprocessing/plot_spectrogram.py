import numpy as np
import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
date = str(sys.argv[1])
band = sys.argv[2]
samp_rate = sys.argv[3]
loc = sys.argv[4]
data_type = sys.argv[5]

filename ='./'+date+'/parsed/'+ date+'_'+band+'_'+samp_rate+'_'+loc+'_'+data_type+'_ap.txt'


# filename = '../data/0125/test_all.txt'
# fig_name = '../data/0125/0125_882m_5m_loc1.png'

time_step = 1000 # how many points to plot in one image
Slen = 128
fid = open(filename,'r')
image_num = 40    
ncols = image_num//8

# 5M sampling rate, we can compute one image is about 1s
# 1000*128*40/(5*10^6)
time_duration = 60 # one image is about 1s, so # of images = time duration (s)
start_point = 12800
line_count = 0
path = './'+date+'/spectrogram/'+ date+'_'+band+'_'+samp_rate+'_'+loc
if not os.path.exists(path):
	os.makedirs(path)



for i in range(0,start_point):
	fid.readline()
for time in range(0,time_duration):
	fig_name = path+'/'+data_type+'_'+str(time+1)+'s.png'
	fig,axes = plt.subplots(nrows=8,ncols=ncols,sharex=True)
	for index in range(0,image_num):
	        data = []
	        for i in range(0,time_step*Slen):
	                line = fid.readline()
			line_count += 1
	                amplitude, phase = line.split()
	                data.append(float(amplitude))
	                # print(data)

	        data_array = np.array(data).reshape((time_step,Slen)).T
	        im = axes[index%8,index/8].imshow(data_array,cmap='jet',vmin=-70,vmax=-20,aspect='auto')
	fig.colorbar(im, ax=axes.ravel().tolist())
	fig.title(date+'_'+band+'_'+samp_rate+'_'+loc)
	fig.xticks([0 200 400 600 800 1000], [0 5.12 10.24 15.36 20.48 25.6], rotation='vertical')
	fig.xlabel('time(ms)')
	fig.ylabel('frequency')
	fig.savefig(fig_name)
	plt.close(fig)
# plt.show()
print('total line counts: {0}').format(line_count)
