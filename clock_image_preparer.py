import os
import shutil
from clock_image_generator import generate_clock_image
from config import *

def generate_clock():
	delete_old_files(full_path)
	return generate_new_file()
	
def delete_old_files(data_path):
	if os.path.exists(data_path):
		os.remove(data_path)
	
def generate_new_file():
	return generate_clock_image()