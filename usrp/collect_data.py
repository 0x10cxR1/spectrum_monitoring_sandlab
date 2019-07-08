import os
import time
import sys

device = sys.argv[1]
band = sys.argv[2]#882.5
bandwidth = sys.argv[3]#5 for 5M

def run_cmd(skip_time, device):
	try:
		while True:
			cur_time = int(time.time())
			os.system('uhd_rx_cfile -f '+band+' --samp-rate='+bandwidth+'000000 -m '+str(cur_time)+'_'+band+'M_'+bandwidth+'m.dat -N 200000000')

			time.sleep(skip_time*60)

			os.system('mv '+str(cur_time)+'_'+band+'M_'+bandwidth+'m.dat '+device)
			
	except KeyboardInterrupt:
		pass

run_cmd(5)
