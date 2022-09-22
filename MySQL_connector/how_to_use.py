from mysql.connector import connect #pip install mysql-connector-python
from connector import user

# How create multiple connections?
connection_1 = user(username_1, password_1)
connection_2 = user(username_2, password_2)
connection_3 = user(username_3, password_3)

# login with multiple users simultaneosly
user1 = user(connection_1)
user2 = user(connection_2)

#######let's assume we are user1#########

# fetching existing database
user1.show()
#    output:
#.   >>Showing datases...
#.   >>(school_database,)
#.   >>(Office_database,)
#.   >>(System,)

# creating new database
user1.create("Hospital_database")
#    output:
#.   >>database is created

# using existing database
my_school = user1.use("school_database")
#    output:
#.   >>using school_database ...

# creating table
student = input("enter table title\n")
Student_Records = my_school.create(student, "name c(10) PRIMARY KEY, id v(10) , roll_no i(2)")
# optional_shortcuts i -> int, char -> c, v -> varchar

Student_Records.show() # prints table
# and many more features like 
# item(name) select column
# drop(name) drop table
# desc(name) describe table/database
# is_exist(name) existence command
# insert(name) update command
# add(name) update command
# etc....
