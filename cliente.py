import socket
import threading

def receive_messages(sock):
    # Recibir mensajes del servidor
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

def send_messages(sock, nickname):
    # Enviar mensajes al servidor
    while True:
        msg = input(f'{nickname}: ')
        sock.sendall(msg.encode())

# Configuración del cliente
host = '192.168.16.113'
port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Ingresar un apodo o nickname
nickname = input("Ingresa tu apodo: ")
client_socket.sendall(nickname.encode())

# Iniciar los hilos para recibir y enviar mensajes
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client_socket,nickname))
send_thread.start()
