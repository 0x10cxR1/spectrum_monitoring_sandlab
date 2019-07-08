#!/bin/bash

python LSTM.py \
	--cmd train \
	--training_path /mnt/data/zhijing/spectrum_anomaly/campus/880M_mix.txt \
	--validation_path /mnt/data/zhijing/spectrum_anomaly/campus/880M_mix.txt \
	--testing_path /mnt/data/zhijing/spectrum_anomaly/campus/880M_mix.txt \
	--oldmodel_path /home/zhijing/spectrum_anomaly/LSTM/result/mix_880M_200k.h5 \
	--oldmodel_weight_path /home/zhijing/spectrum_anomaly/LSTM/result/880M_mix_weights.h5 \
	--model_path /home/zhijing/spectrum_anomaly/LSTM/result/new_model.h5 \
	--weight_path /home/zhijing/spectrum_anomaly/LSTM/result/new_weights.h5 \
	--batch_size 64 \
	--timesteps 50 \
	--predict_steps 25 \
	--data_dim 128 \
	--epochs 10 \
	--hidden_size 64 \
	--train_num 500000 \
	--valid_num 5000 \
	--test_num 10000 \
	--testing_res /home/zhijing/spectrum_anomaly/LSTM/test_res.txt \
	--testing_res_CDF /home/zhijing/spectrum_anomaly/LSTM/test_res_CDF.txt \