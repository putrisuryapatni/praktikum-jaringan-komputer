from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((" ", 6789))
serverSocket.listen(1)

print("Server jalan di http://127.0.0.1:6789")

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(1024).decode()
    print("REQUEST MASUK:\n", request)

    try:
        filename = request.split()[1]
        
        if filename == "/":
            filename = "/HelloWorld.html"

        with open("." + filename, "rb") as f:
            response_body = f.read()

        response_header = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(response_header.encode())
        connectionSocket.send(response_body)

    except Exception as e:
        print("ERROR:", e)

        response = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
        connectionSocket.send(response.encode())

    connectionSocket.close()