
def update_server_config(file_path, key, value):
   
   with open(file_path, "r") as file:
       lines = file.readlines()


   with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key+ " = "+value + "\n")
            else:
                file.write(line)


update_server_config("C:/Users/AVW0AJ744/Desktop/python-learning/python-for-devops/Day-12/server.conf", "MAX_CONNECTIONS", "1000")