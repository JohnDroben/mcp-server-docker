import socket
import json

def send_tcp_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(json.dumps(request).encode('utf-8'))
        response = s.recv(1024)
        print(response.decode('utf-8'))

request = {
  "jsonrpc": "2.0",
  "method": "call_tool",
  "params": {
    "name": "coin_flip",
    "arguments": {}
  },
  "id": 1
}

send_tcp_request('localhost', 8080, request)
