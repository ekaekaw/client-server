import socket

# Konfigurasi server
host = '127.0.0.1'  # IP address server
port = 12345       # Port yang akan digunakan

# Membuat socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding socket ke alamat dan port yang telah ditentukan
server_socket.bind(host, port)

# Mendengarkan koneksi
server_socket.listen(5)

print(f"Server berjalan di {host}:{port}")

# Menerima koneksi dari client
client_socket, client_address = server_socket.accept()
print(f"Terhubung dengan {client_address}")

while True:
    # Menerima pesan dari client
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Pesan dari client: {data.decode()}")

    # Mengirim balasan ke client
    response = "Pesan diterima oleh server."
    client_socket.send(response.encode())

# Menutup koneksi dengan client
client_socket.close()

# Menutup socket server
server_socket.close()
