import socket
import threading
import functools
global IP, PORT, NICKNAME, PASSWORD
IP:str=input(f'Introduzca IP: ')
PORT:int=int(input(f'Introduzca Puerto: '))
NICKNAME:str=input('Introduzca Nickname: ')
PASSWORD:str=input('Introduzca contraseña: ')
class Client(object):
    '''
    ### Crea un cliente para una conexión TCP con un servidor.
    __
    #### `Client(IP, PUERTO, NOMBRE_DE_USUARIO)` -> socket
    '''
    __instance = None
    def __init__(self, 
               __SERVER_IP__:str=IP, 
               __SERVER_PORT__:int=PORT, 
               __CLIENT_NICKNAME__:str=NICKNAME):
        
        if Client.__instance != None:
            raise Exception("Ya se ha creado una instancia de Client")
        else:
            Client.__instance = self # almacenar la única instancia    
            self.server_ip=__SERVER_IP__
            self.server_port=__SERVER_PORT__
            self.client_nickname=__CLIENT_NICKNAME__
            self.Mesagge_Controller=Messages(None)
            
    @classmethod
    def getInstance(cls,
                __SERVER_IP__:str =IP, 
               __SERVER_PORT__:int = PORT, 
               __CLIENT_NICKNAME__:str= NICKNAME):
        if cls.__instance == None:
            cls(__SERVER_IP__, __SERVER_PORT__, __CLIENT_NICKNAME__)
        return cls.__instance
    
    def __create_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def get_socket(self):
        return self.__create_socket()
        
    def get_nickname(self):
        if self.client_nickname != None:
            return self.client_nickname
        else:
            print('No ha especificado ningún nombre de usuario.')
            
    def connect_to_server(self):
        '''
        ### Coge `Client.create_socket()` o un `socket` como argumento.
        __
        #### EJEMPLO:
        `Client.connect_to_server(Client.create_socket())`
        '''
        return self.__create_socket().connect((self.server_ip, self.server_port))
    
class Messages(object):
    def __init__(self,
                 __MESSAGE__:str|None):
        
        self.socket=Client().getInstance().get_socket()
        self.message=__MESSAGE__
        self.nickname=Client().getInstance().get_nickname()
        
    def send_message(self):
        # Enviar mensajes al servido
        while True and self.message != None:
            self.socket.sendall(f'{self.nickname}: {self.message}'.encode())

    def receive_messages(self):
        # Recibir mensajes del servidor
        while True:
            msg = self.socket.recv(1024)
            print(msg.decode())

client=Client(IP, PORT, NICKNAME).getInstance()
'''
class Start_Thread(object):
    def __init__(self,
                 *args,
                 **kwargs):
        
    def __receive_thread(self):
        receive_thread = threading.Thread(target=Client.getInstance, kwargs={'sock': client_socket})
        return receive_thread

    def __send_thread(self):
        send_thread = threading.Thread(target=Messages().send_message)
    
    def __start_threads(self, *args):
        for i in list(args):
            i.start()

    
client = Client('192.168.16.113', 8080)
client_socket = client.connect_to_server()


__GLOBAL_SERVER_STATUS=False

def is_server_online(sock):
    while True:
        try:
            sock.connect_ex(sock.getsockname())
            __GLOBAL_SERVER_STATUS=True
            return __GLOBAL_SERVER_STATUS
        except:
            __GLOBAL_SERVER_STATUS=False
            return __GLOBAL_SERVER_STATUS

def check_server_status_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sock=kwargs.get('sock')
            if is_server_online(sock):
                return func(*args, **kwargs)
            else:
                print("No se pudo establecer conexión con el servidor")
                sock.close()
                return None
        return wrapper


        
@check_server_status_deco

        
@check_server_status_deco
def send_messages(sock, nickname):


# Configuración del cliente
host = '192.168.16.113'
port = 8080


client_socket.connect((host, port))
# Ingresar un apodo o nickname
nickname = input("Ingresa tu apodo: ")
client_socket.send(nickname.encode())

# Iniciar los hilos para recibir y enviar mensajes

'''