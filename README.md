# coudnt-test-examples

# populate cloudant
Easy way to populate all data (.json files) in a directory to a specific cloudant database.

Give the directory with .json files as argument then you will be asked for your credentials (username, password and host) 
and the database name (if database not exist it will be created!, else the documents will be added on the existing database)

Command to run:
'python .\populate_database.py .\path_to_directory'

# find docs
Find a specific doc on your cloundant database.

Run the code then you will be asked for your crendentials (username, password and host), database name, 
a list of property names (separated by ';') and a list of respectiver property values (also separeted by ';' and must has the same length of property name list).

Command to run:
'python .\find_doc.py'