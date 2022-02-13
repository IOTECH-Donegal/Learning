'''
Multicast client by: JOR
Sends multicast packets to a particular address and port.

Alpha: 13FEB22
'''

import socket
import time
from datetime import datetime
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MCCLIENT["MCAST_GROUP"]
MCAST_PORT = settings.MCCLIENT["PORT"]
MCAST_IF_IP = settings.MCCLIENT["IP_ADDRESS"]


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(MCAST_IF_IP))
        message_text = f"IOTECH {datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (MCAST_GRP, MCAST_PORT))
        time.sleep(1)
