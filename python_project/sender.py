import socket
S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# target_ip = "10.1.0.94"  #ranjeet sir ip
# target_ip = "10.1.0.47" # daman ip
target_ip = "127.0.0.1"
PORT_NO = 2525
target_address = (target_ip, PORT_NO)


while True:
    message = input("please write a message : ")
    encrypted_message = message.encode('ascii')
    S.sendto(encrypted_message, target_address)
    print("you have successfully sent the message!")

