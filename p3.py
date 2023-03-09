import socket
import threading

def handle_client(conn, addr):
    # Manejar la conexión con un cliente
    print(f"Nuevo cliente conectado: {addr}")

    # Pedir el apodo del cliente
    conn.sendto("Ingresa tu apodo: ".encode(), addr)
    nickname = conn.recv(1024).decode()

    while True:
        # Recibir mensaje del cliente
        msg = conn.recv(1024)
        if not msg:
            # Si no hay mensaje, significa que la conexión se cerró
            print(f"Cliente desconectado: {addr}")
            break

        # Imprimir mensaje del cliente en la consola del servidor
        print(f"{nickname}: {msg.decode()}")

        # Reenviar el mensaje a todos los clientes
        for c in clients:
            if c != conn:
                c.sendall(f"{nickname}: {msg}".encode())

    # Cerrar la conexión con el cliente
    conn.close()
    clients.remove(conn)

# Configuración del servidor
host = '192.168.16.113'
port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen()

clients = []

print(f"Servidor escuchando en {host}:{port}")
try:
    while True:
        # Esperar a que un cliente se conecte
        conn, addr = server_socket.accept()
        # Agregar el cliente a la lista de clientes
        clients.append(conn)

        # Iniciar un nuevo hilo para manejar la conexión con el cliente
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
except KeyboardInterrupt:
    exit(1)