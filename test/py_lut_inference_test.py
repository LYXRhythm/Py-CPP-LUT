import cv2
import numpy as np
import time
from pathlib2 import Path

import os
import sys
import torch
#
sys.path.append(r"/home/guest/LUT/PyApplyLUT-main/")
from python.PyApplyLUT import PyApplyLUT
from python.lut_tools import cube_to_npy

def convert(imgpath, lutpath, save_name):
	INPUT_IMG = Path(imgpath)
	LUT_FILE = Path(lutpath)

	img = cv2.imread(INPUT_IMG.as_posix())
	img = img / 255
	img = torch.from_numpy(img)

	print(type(img))
	# apply lut 
	# method 1 load from .cube file
	alut = PyApplyLUT(lut_file=LUT_FILE)
	start = time.time()
	new_img = alut.apply_lut(img)
	new_img = new_img * 255
	end = time.time()
	print("time = ", end - start)
	
	cv2.imwrite(save_name, new_img.numpy())
	return 

print("sdf")
LUT_FILE = './test/Foodie-cube/1.cube'
INPUT_IMG = './test/bird.png'
convert(INPUT_IMG, LUT_FILE, "./result.jpg")

