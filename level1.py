# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:53:40 2021

@author: Cheng
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:05:56 2021

@author: 417-02
"""

import numpy as np
np.set_printoptions(threshold=np.inf)
import os
import re
import math
from scipy import io
from CPSC2019_challenge import CPSC2019_challenge
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
try:
    from keras.models import model_from_json
except:
    from tensorflow.keras.models import model_from_json
import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600
def pp(data):
    x = np.max(data)
    if x>20:
        b = np.argwhere(data>20)
        for k in b[:,0]:
            if k>0:
                data[k] = data[k-1]
    return data
def load_ans(index, fs_):
    '''
    Please modify this function when you have to load model or any other parameters in CPSC2019_challenge()
    '''
    def is_mat(l):
        return l.endswith('.mat')
    #ecg_files = list(filter(is_mat, os.listdir(data_path_)))
    #rpos_files = list(filter(is_mat, os.listdir(rpos_path_)))
    model1 = model_from_json(open('E:/cpsc2019cai/models/CNN.json').read())
    model1.load_weights('E:/cpsc2019cai/models/CNN.h5')
    model2 = model_from_json(open('E:/cpsc2019cai/models/CRNN.json').read())
    model2.load_weights('E:/cpsc2019cai/models/CRNN.h5')
    #HR_ref = []
    #R_ref = []
    HR_ans = []
    R_ans = []
    
    data_path_ = 'E:/train/train/data/'    
    ecg_file = 'data_' + index + '.mat'

    #ref_path = os.path.join(rpos_path_, rpos_file)
    ecg_path = os.path.join(data_path_, ecg_file)

    ecg_data = io.loadmat(ecg_path)['ecg'].squeeze()
    #print(ecg_data.shape)
    ecg_data = pp(ecg_data)
    #r_ref = io.loadmat(ref_path)['R_peak'].squeeze()
    #r_ref = r_ref[(r_ref >= 0.5*fs_) & (r_ref <= 9.5*fs_)]

    #r_hr = np.array([loc for loc in r_ref if (loc > 5.5 * fs_ and loc < len(ecg_data) - 0.5 * fs_)])
    result1 = model1.predict(ecg_data.reshape(1,5000,1))
    result2 = model2.predict(ecg_data.reshape(1,5000,1))
    result = (result1[0,:,0]+result2[0,:,0])/2
    #print(result)
    hr_ans, r_ans = CPSC2019_challenge(result)
    try:
        hr_ans, r_ans = CPSC2019_challenge(result)
    except:
        hr_ans = 80
        r_ans = np.array([0])
    #HR_ref.append(round( 60 * fs_ / np.mean(np.diff(r_hr))))
    #R_ref.append(r_ref)
    HR_ans.append(hr_ans)
    R_ans.append(r_ans)

    return R_ans, HR_ans

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(R_ans, HR_ans):
	try:
		name = R_ans
		desc = HR_ans

		final_str = 'R: %s \nHR: %s' % (name, desc)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_dignosisi(index):
    FS = 500
    R_ans, HR_ans = load_ans(index, FS)
    a = format_response(R_ans, HR_ans)
    return a


'''
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='medical.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=1)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="基本信息", font=40, command=lambda: get_dign(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

button1 = tk.Button(frame, text="诊断", font=20, command=lambda: get_weather(entry.get()))
button1.place(relx=0.6,rely=1, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=1)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
'''