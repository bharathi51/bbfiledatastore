from filedatastore_BB import main_ex 
import oprt
from time import sleep
import threading

class mock_unit:
	client = "me"
	key = "testinfg"
	key_int = 12
	key_more_than_32 = "be happy and stay home stay safe:)"
	value_dict = {"myproject" : 
	{ 
   "feel":"great",
   "location":"hyderad",
   "products":{ 
      "Product-1":"first_project",
      "Product-2":"second_projct",
      "Product-3":"third_project"
   }
   }
   }
	value_json_type = { "student":"rani", "status":"fresher", "role":"software_developer" }
	value_string = "bvcsdjh dhfdhfdh aisijf fdfhdjbfjgkfj sdh"
	ttl_value = 10


def create(mock):
	print(main_ex.create(mock.client, mock.key, mock.value_json_type)+"\n")			#Expect Success
	print(main_ex.create(mock.client, mock.key_int, mock.value_json_type)+"\n")		#Expect Key error	
	print(main_ex.create(mock.client, mock.key, mock.value_dict)+"\n")				#Expect Key already present
	print(main_ex.create(mock.client, mock.key_more_than_32, mock.value_json_type)+"\n")#Expect Key error
	print(main_ex.create("our", mock.key_int, mock.value_dict)+"\n")				#Expect key error
	print(main_ex.create(mock.client, "Employer", mock.value_string)+"\n")			#Expect value error
	print(main_ex.create(mock.client, "selse", mock.value_dict, ttl = mock.ttl_value)+"\n")	#Expect Success


def read(mock):
	print(main_ex.read(mock.client, mock.key)+"\n")									#Expect Success
	print(main_ex.read(mock.client, mock.key_int)+"\n")								#Expect Key error
	print(main_ex.read("check", mock.key)+"\n")										#Expect Client not found error
	print(main_ex.read(mock.client, "selse")+"\n")								#Expect Success since TTL is still intact
	print("\nwaiting...\n")
	sleep(31)
	print(main_ex.read(mock.client, "selse")+"\n")								#Expect TTL error


def delete(mock):
	print(main_ex.delete(mock.client, mock.key)+"\n")									#Expect Success
	print(main_ex.delete(mock.client, mock.key_more_than_32)+"\n")					#Expect Key not exists
	print(main_ex.delete("l24hey", mock.key)+"\n")									#Expect Client not found error
	print(main_ex.delete(mock.client, "selse")+"\n")								#Expect TTL error


def create_2(mock):
	print(main_ex.create("creatnew", mock.key, mock.value_json_type)+"\n")


def append_2(mock):
	print(main_ex.create("checking1", mock.key, mock.value_dict)+"\n")
	print(main_ex.delete("checking2", mock.key)+"\n")


def mock_unit_begin(mock):
	
	print( "\n\n*************** Create mode mock test units ***************\n\n")
	create(mock)
	print( "\n\n*************** Read mode mock test units ***************\n\n")
	read(mock)
	print( "\n\n*************** Delete mode mock test units ***************\n\n")
	delete(mock)
	print( "\n\n*************** Reset mode mock test units ***************\n\n")
	print(main_ex.reset(mock.client))
	print(main_ex.reset("87Lane"))

if __name__ == "__main__": 
    
    print("\n######## General Test ########\n")
    mock = mock_unit()
    mock_unit_begin(mock)

    print("\n######## Thread-Safe Code Test ########\n")
    # creating thread 
    t1 = threading.Thread(target=create_2, args=(mock,)) 
    t2 = threading.Thread(target=append_2, args=(mock,)) 
  
    t1.start() 
    t2.start() 
   
    t1.join() 
    t2.join() 
  
    # both threads completely executed 
    print("Thread-safe Testing done")

