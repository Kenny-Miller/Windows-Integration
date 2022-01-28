import socket
from logger import create_logger
from pynput.mouse import Button, Controller

class WallClient():
  def __init__(self,ip,port) -> None:
    self.logger = create_logger(__name__)
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.bind((ip,port))
    self.mouse = Controller()
    self.running = False
  
  def start(self) -> None:
    self.logger.debug('Starting Wall Client')
    self.running = True
    while self.running:
      (data, addr) = self.sock.recvfrom(1024)
      msg = data.decode('utf-8')
      self.logger.debug(f"[Message]: {msg} from {addr}")
      match msg:
        case 'exit': self.running = False
        case _: self.handle(msg)
  
  def handle(self, msg) -> None:
    (x, y, pressed) = msg.split(" ")
    self.mouse.position = (x, y)
    self.mouse.press(Button.left) if pressed == False else self.mouse.release(Button.left)

if __name__ == "__main__":
  hostname = socket.gethostname()
  listener_ip = socket.gethostbyname(hostname)
  listener_port = 7200
  
  client = WallClient(listener_ip, listener_port)
  client.start()