#Database connection details
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2912#Rambo",
    database="new_pythondb")
cur_obj=conn_obj.cursor()

#Define function data_entry_sql
def data_entry_sql(full_name,address,phone_number,user_id,password):
    sql = "INSERT INTO cust_details (full_name, address, phone_number, user_id, password) VALUES (%s, %s, %s, %s,%s)"
    data = (full_name,address,phone_number,user_id,password)

    try:
        cur_obj.execute(sql, data)
        print("Your registration has been completed, now try to login....")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

#Define function data_retrieve
def data_retrieve(user_id):
    query = f"select * from cust_details WHERE user_id=\'{user_id}\'"
    #print(query)
    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result
def user_registration():
    full_name = input("Please enter your full name---->")
    address = input("Please enter your address---->")
    phone_number = input("Please enter your phone_number---->")
    user_id = input("Please enter your user_id---->")
    password = input("Please enter your password---->")
    data_entry_sql(full_name, address, phone_number, user_id, password)
cust_choice=input("1 - login \n2-  new user registration -> \n enter your choice ->")
if cust_choice=='1':
    #login
    user_id = input("Please enter your user_id---->")
    password = input("Please enter your password---->")
    result_from_db=data_retrieve(user_id)
    #print(result_from_db)
    if result_from_db:
        password_db=result_from_db[-1]
        if password==password_db:
            print("Access granted....")
        else:
            print("Access denied..")
    else:
        pass #user does not exist ,pls registered yourself
        print("You are new customer to us, Pls register yourself")
        user_registration()
        user_id = input("Please enter your user_id---->")   
        password = input("Please enter your password---->")
        result_from_db = data_retrieve(user_id)
        if result_from_db:
            password_db = result_from_db[-1]
            if password == password_db:
                print("Access granted....")
            else:
                print("Access denied..")
elif cust_choice=='2':
    #new user registration
    user_registration()
    user_id = input("Please enter your user_id---->")
    password = input("Please enter your password---->")
    result_from_db = data_retrieve(user_id)
    if result_from_db:
        password_db=result_from_db[-1]
        if password==password_db:
            print("Access granted....")
        else:
            print("Access denied..")

else:
    print("Invalid input, pls try again....")

conn_obj.close()