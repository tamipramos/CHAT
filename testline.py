import curses
import shutil
columns, rows = shutil.get_terminal_size()
def chat(stdscr):
    # Configurar curses para usar colores
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # Configurar la ventana para permitir el desplazamiento vertical
    stdscr.scrollok(True)

    # Imprimir algunos mensajes de chat
    stdscr.addstr("Usuario1: Hola\n")
    
    # Permitir que la ventana se desplace automáticamente hacia abajo
    stdscr.scrollok(True)

    # Esperar la entrada del usuario
    print(f"La consola tiene un ancho de {columns} y una altura de {rows}")

# Inicializar curses y ejecutar la función chat
curses.wrapper(chat)



