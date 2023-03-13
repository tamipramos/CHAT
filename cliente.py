import urwid

def main():
    # Crea un widget Edit y lo coloca en un Frame
    widget_edit = urwid.Edit(multiline=True)
    widget_frame = urwid.Frame(urwid.Filler(widget_edit))

    # Crea un widget Pile que contiene el Frame y un widget Text
    widget_text = urwid.Text("Presione Ctrl-C para salir.")
    widget_pile = urwid.Pile([widget_frame, widget_text])

    # Crea un widget BoxAdapter para que el widget Pile ocupe toda la pantalla excepto la última línea
    widget_adapter = urwid.BoxAdapter(widget_pile, height=("relative", 100))

    # Crea un widget Divider y lo coloca en la última línea de la pantalla
    widget_divider = urwid.Divider()
    widget_footer = urwid.Pile([widget_divider, urwid.Text("Escriba su mensaje y presione Enter.")])
    widget_footer_adapter = urwid.BoxAdapter(widget_footer, height=("pack", 2))

    # Crea un widget Overlay que contiene el widget BoxAdapter y el widget Divider
    widget_overlay = urwid.Overlay(widget_adapter, widget_footer_adapter, align="center", width=("relative", 100), height=("relative", 100), valign="bottom")

    # Ejecuta el bucle principal de Urwid
    urwid.MainLoop(widget_overlay).run()

if __name__ == "__main__":
    main()