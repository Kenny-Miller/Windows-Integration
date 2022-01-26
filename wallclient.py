import socket
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

hostname = socket.gethostname()
listener_ip = socket.gethostbyname(hostname)
listener_port = 7200

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((listener_ip, listener_port))

running = True

def handle(msg):
  # do click stuff here
  pass

while running:
  (data, addr) = sock.recvfrom(1024)
  msg = data.decode('utf-8')
  logging.debug(f"[Message]: {msg} from {addr}")
  match msg:
    case 'exit': running = False
    case _: handle(msg)

