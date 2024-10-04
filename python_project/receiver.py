import socket
import os
from datetime import datetime
S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

base_folder = (r"C:\Users\ashis\OneDrive\Desktop\upflairs AI-ML class notes\python_project")
data_folder_path = os.path.join(base_folder, "Data")
os.makedirs(data_folder_path, exist_ok=True)

# ip_address = "10.1.0.135"
ip_address = "127.0.0.1"    
PORT_NO = 2525 #range (0 - 65353)
complete_address = (ip_address,PORT_NO) #created a tuple

S.bind(complete_address)

print("hey data is receiving...")
while True:
    data = S.recvfrom(100) # receive only 100 characters at a time or say 100 packets
    message = data[0]
    ip_address = data[1][0]
    decrypted_message = message.decode('ascii')

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    message_with_time = f"{current_time} : {decrypted_message}"
    print(message_with_time, ">>>>", ip_address)
    # print(decrypted_message,">>>>", ip_address) # message_without_time

    file_path = os.path.join(data_folder_path, f"{ip_address}.txt")

    with open(file_path,'a') as file:
        # file.write(decrypted_message)
        file.write(message_with_time)

