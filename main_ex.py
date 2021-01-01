from filedatastore_BB import oprt
import logging
import threading
import json  

logging.basicConfig(filename='logfile_of_application.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

lock = threading.RLock()

def create(client, key, value, **kwargs):
	ttl_value = kwargs.get('ttl', None)
	
	filepath = kwargs.get('filepath', ".//")
	with lock:
		if isinstance(value, str):
			try:
				value = json.loads(value)
			except:
				value = value
		
		status = oprt.create_operation(client, key, value, filepath = filepath , ttl = ttl_value)
		
		if 'successfull' in status:
			return "Create Operation Done"
		elif 'denied' in status:
			logging.error(status)
			return "Error occurred while creating : " + status
		else:
			logging.error(status)
			return "Error Status : " + status


def delete(client, key, **kwargs):
	filepath = kwargs.get('filepath', ".//")
	with lock:
		status = oprt.delete_operation(client, key, filepath = filepath)
		if 'Deleted' in status:
			return status
		elif 'not found' in status:
			logging.error(status)
			return status
		else:
			logging.error(status)
			return "Error Status : " + status


def read(client, key, **kwargs):
	filepath = kwargs.get('filepath', ".//")
	with lock:
		status = oprt.read_operation(client, key, filepath = filepath)
		if 'not found' in status:
			logging.error(status)
			return status
		elif 'value' in status:
			return status
		else:
			logging.error(status)
			return "Error Status : " + status


def reset(client, **kwargs):
	filepath = kwargs.get('filepath', "")
	with lock:
		status = oprt.reset_operation(client, filepath = filepath)
		logging.info(status)
		return status

