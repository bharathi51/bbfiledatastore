# bbfiledatastore
This repository consists of files on key-value data store 
operations performed are :

  1 for Create (--client --key  --ttl(optional) --value --filepath(optional)) 
	2 for Read (--client --key --filepath(optional)) 
	3 for Delete (--client --key --filepath(optional)) 
	4 for Reset (--client --filepath(optional))
  
 init.py :
  all initialization of operations 
  
  
 oprt.py :
 performed all operations
 
 all_functional_requirements_testing.py:
 
As per the given problem statement performed all operations

_____________________________________________________OUTPUT_OF_ALL_FUNCTIONAL_REQUIREMENT_TESTING________________________________________________________________________________



######## General Test ########



*************** Create mode mock test units ***************


Create Operation Done

Error Status : Key's datatype should be String

Error Status : Key | testinfg | already exist , value - {'student': 'rani', 'status': 'fresher', 'role': 'software_developer'} 

Error Status : Character limit for Key is 32, But it has 34

Error Status : Key's datatype should be String

Error Status : Value's datatype should be JSON object (Dict)

Create Operation Done



*************** Read mode mock test units ***************


For key | testinfg | value  - {'student': 'rani', 'status': 'fresher', 'role': 'software_developer'} 

Key | 12 | not found for client - me 

Error Status : check - Client_file_doesnot_exist

For key | selse | value  - {'myproject': {'feel': 'great', 'location': 'hyderad', 'products': {'Product-1': 'first_project', 'Product-2': 'second_projct', 'Product-3': 'third_project'}}} 


waiting...

Error Status : TTL Value for the Key - selse expired for the client - me



*************** Delete mode mock test units ***************


Error Status : For key | testinfg | value - is deleted

Key | be happy and stay home stay safe:) | not found for client - me 

Error Status : l24hey - Client_file_doesnot_exist

Error Status : TTL Value for the Key - selse expired for the client - me



*************** Reset mode mock test units ***************


File removed!!!! - me
87Lane - Client_file_doesnot_exist

######## Thread-Safe Code Test ########

Create Operation Done
Create Operation Done


Error Status : checking2 - Client_file_doesnot_exist

Thread-safe Testing done


______________________________________________________OUTPUT OF TETREAD111.PY______________________________________________________________________________________



select 1.create 
 2.read 
3.delete 
1
enter keyuser
enter value1
Error Status : Value's datatype should be JSON object (Dict)
select 1.create 
 2.read 
3.delete 
1
enter keyuser
enter value{"hi":"1"}
Create Operation Done
select 1.create 
 2.read 
3.delete 
1
enter keyuser1
enter value{"hello":"2"}
Create Operation Done
select 1.create 
 2.read 
3.delete 
2
enter keyuser
For key | user | value  - {'hi': '1'} 
select 1.create 
 2.read 
3.delete 
2
enter keyuser1
For key | user1 | value  - {'hello': '2'} 
select 1.create 
 2.read 
3.delete 
3
enter keyuser
Error Status : For key | user | value - is deleted
select 1.create 
 2.read 
3.delete 
2
enter keyuser
Key | user | not found for client - Access_store 
select 1.create 
 2.read 
3.delete 
1
enter keyuser 
enter value{"hi":"1"}
Create Operation Done
select 1.create 
 2.read 
3.delete 
1
enter keyuser
enter value{"hauer":"2"}
Create Operation Done
select 1.create 
 2.read 
3.delete 
1
enter keyuser
enter value{"hi":"1"}
Error Status : Key | user | already exist , value - {'hauer': '2'} 
select 1.create 
 2.read 
3.delete 

