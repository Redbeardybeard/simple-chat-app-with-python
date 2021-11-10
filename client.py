import socket


server_address = (ip,port) = "localhost" , 5050

socket_af = socket.AF_INET
socket_type = socket.SOCK_STREAM


with socket.socket(socket_af, socket_type) as s:
    print(f'client connecting to {server_address}')
    s.connect(server_address)

    data = "hey there"
    b_data = bytes(data.encode('utf-8'))
    print(f'sending data : {data}')

    s.sendall(b_data)


    print('listening for replies...')
    rcvd_data = s.recv(1024)

    print(f'recieved data = {rcvd_data}')

    print('closing connection. goodbye!')
    
    
    


