from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import *
from clock_image_preparer import generate_clock
import time
import logging
import datetime

def main():
	now = datetime.datetime.now()
	log_date = now.strftime("%Y-%m-%d %H:%M")
	log_message = '{} - {}'.format(log_date, 'Clock image was updated')
	
	client = TelegramClient('AvaChangerSession', api_id, api_hash)
	client.start()
	
	update_clock(client)
	t0 = time.time()
	first_launch = True
	while True:
		now = datetime.datetime.now()
		log_date = now.strftime("%Y-%m-%d %H:%M")
		logging.basicConfig(filename='logs/{}.log'.format(now.strftime('%Y-%m-%d'),level=logging.INFO))
		
		if first_launch:
			logging.info('{} - {}'.format(log_date, 'Updating was started'))
			first_launch = False
			print('Updating was started')
			
		t1 = time.time()
		if (t1-t0) >= 60.0:
			try:
				update_clock(client)
				logging.info('{} - {}'.format(log_date, log_info_message))
			except Exception as e:
				print('Exception: {}'.format(str(e)))
				logging.warning('{} - {}. Details: {}'.format(log_date, log_warning_message, str(e)))
				continue
			t0 = t1 
		
	
def upload_new_clock(client):
	file = client.upload_file(generate_clock())
	client(UploadProfilePhotoRequest(file))
	
def delete_photos(client):
	client(DeletePhotosRequest(client.get_profile_photos('me')))
	
def get_dialogs(client):
	for dialog in client.iter_dialogs():
		print(dialog.name, 'has ID', dialog.id)

def update_clock(client):
	delete_photos(client)
	upload_new_clock(client)

if __name__ == '__main__':
	main()
