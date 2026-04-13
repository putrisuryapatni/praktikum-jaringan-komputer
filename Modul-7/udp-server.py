from socket import *

# membuat socket untuk server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# menghubungkan (bind)
serverSocket.bind(
    # tupple
    ('', serverPort)
)

print("[SERVER] Server siap digunakan")

# dijalankan, selama true 
running = True
while running:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode()

    if decodedMessage.lower() == "exit":
        print("[SYSTEM] Server telah diberhentikan")
        running = False
        continue

    # capslock
    modifiedMessage = decodedMessage.upper()
    print("[SERVER] Diterima dari ", clientAddress, "message: ", decodedMessage)

    # mengirim ke client
    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )

serverSocket.close()
print("[SYSTEM] Socket server telah ditutup")

