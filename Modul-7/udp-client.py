from socket  import *

serverName = "localhost"
serverPort = 12000

# AF_INET = ip addr IPv4 | SOCK_DGRAM = UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

running = True
while running:
    message = input("> ")

    if message.lower() == "exit":
        clientSocket.sendto(
            message.encode(),
            (serverName, serverPort)
        )
        print("[SYSTEM] Keluar dari program")
        running == False
        continue

    clientSocket.sendto(
        # jarkom = 10101001010
        message.encode(),
        # mengirim pesan
        (serverName, serverPort)
    )

    #menerima pesan
    # 2048 itu panjang byte nya
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print("[SYSTEM] Pesan telah diterima dari: ", serverAddress)
    print(modifiedMessage.decode())

#menutup socket dari client
clientSocket.close()
print("[SYSTEM] Koneksi telah ditutup")
