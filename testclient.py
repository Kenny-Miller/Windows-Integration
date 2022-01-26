import socket


hostname = socket.gethostname()
target_ip = socket.gethostbyname(hostname)
target_port = 7200

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

running = True
while running:
  msg = input("Enter message: ")
  if msg == 'exit': running = False
  sock.sendto(msg.encode('utf-8'), (target_ip,target_port))