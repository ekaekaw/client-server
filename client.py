import socket

# Konfigurasi client
host = '127.0.0.1'  # IP address server
port = 12345       # Port yang akan digunakan

# Membuat socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke server
client_socket.connect((host, port))

# Mengirim pesan ke server
message = "Halo, ini pesan dari client."
client_socket.send(message.encode())

# Menerima balasan dari server
response = client_socket.recv(1024)
print(f"Balasan dari server: {response.decode()}")

# Menutup koneksi dengan server
client_socket.close()
