import socket
import struct
import urllib.parse



def fetch(addr, port, querystr):

    if querystr[0] != "?":
        querystr = "?"+querystr
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    query = b"\x00\x83" + struct.pack('>H', len(querystr) + 6) + b"\x00\x00\x00\x00\x00" + querystr.encode() + b"\x00"

    sock.connect((addr, port))

    sock.sendall(query)

    data = sock.recv(4096)

    parsed_data = urllib.parse.parse_qs(data[5:-1].decode())
    return {i:parsed_data[i][0] for i in parsed_data.keys()}

def get_sec(h=0,m=0,s=0):
    return int(h) * 3600 + int(m) * 60 + int(s)
