import socket


socket_af = socket.AF_INET
socket_type = socket.SOCK_STREAM
address = (ip, port) = "192.168.1.29", 9999


with socket.socket(socket_af,socket_type) as s:
    s.connect(address)
    data = "hello from the python side!"
    b_data = bytes(data.encode('utf-8'))
    s.sendall(b_data)
    while True:
        
        git_gud_son = s.recv(8)
        if bytes("tailer".encode('utf-8')) in git_gud_son:
            break
        print(git_gud_son)


    # print(git_gud_son)

