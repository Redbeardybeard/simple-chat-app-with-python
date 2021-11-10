import socket


server_address = (ip,port) = "localhost" , 5050

socket_af = socket.AF_INET
socket_type = socket.SOCK_STREAM


with socket.socket(socket_af,socket_type) as s:
    s.bind(server_address)
    s.listen()

    while True:
        print('listening for new connections ...')
        active_socket, client_info = s.accept()
        print(f'connected to client {client_info}.')

        with active_socket:
            data = active_socket.recv(1024)
            print(f'data recvd : {data}\n echoing data back to client ...')
            active_socket.sendall(data)
            print('done.')
            

        


        





