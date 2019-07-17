EXPLANATION:
This preprocessing step does three things:

1. **It downsamples the IQ samples (saved in .dat files) for two reasons.** First, downsampling makes the LSTM model simpler and save a lot of computation. Second, this can mimic the duty-cycle of specturm monitoring device. Imagine that only one monitoring device is used to scan 10 LTE channels. Then only 1/10 of IQ sampled can be collected used for each channel.

2. **Compute the FFT amplitude**. We use FFT amplitude as features to train LSTM. Therefore, amplitude is computed and saved in .txt files. 

3. ***Generate features as ML inputs**. From the sampled USRP data, we generate ML inputs by splitting the data into 100(25.6ms, observation) + 25(6.4ms, prediction) spectrum sequence, and then do normalization.



USAGE:
1&2. To use this code, you can run the following command, where DATAPATH is the place where the collected .dat files are saved. See data readme for the DATAPATH.

```Parse Data 
python downsample_parse_data.py DATAPATH
```

Most likely, you don't need to change the code, unless you need to change the downsample rate (10), number of FFT points (128), maximum number of blocks, block size. See the comments in code for details. 


```Plot Figure (visualize the FFT amplitude)
python plot_spectrogram.py DATE BAND SAMP_RATE LOC DATA_TYPE
```

See Zhujun's folder on rocket



3. Run the following command, where DATAPATH is the data path, BAND is the LTE frequency, OUT_FILENAME is the result path, NOR_METHOD is the normalization method, 1 is w/o normalization, 2 is max-min, 3 is standard (used in the paper).

```Generate features
python get_feature.py DATAPATH BAND OUT_FILENAME NOR_METHOD
```
