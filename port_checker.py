import socket
import random

BANNER = r"""
  _____     _      _                                                                                  
 | ____| __| |  __| | _   _  _   _  _   _   ___  __ _                                                 
 |  _|  / _` | / _` || | | || | | || | | | / __|/ _` |                                                
 | |___| (_| || (_| || |_| || |_| || |_| || (__| (_| |                                                
 |_____|\__,_| \__,_| \__, | \__, | \__,_| \___|\__,_|                                                
                      |___/  |___/                                                                    
  _____  _                 ____            _                                                          
 |_   _|| |__    ___      / ___| ___    __| |  ___                                                    
   | |  | '_ \  / _ \    | |    / _ \  / _` | / _ \                                                   
   | |  | | | ||  __/    | |___| (_) || (_| ||  __/                                                   
   |_|  |_| |_| \___|_____\____|\___/  \__,_| \___|                                                   
   ____             |_____|              _            _____  _                 ____                 _ 
  / ___| ___   _ __  _ __  _   _  _ __  | |_  ___    |_   _|| |__    ___      / ___|   ___   _   _ | |
 | |    / _ \ | '__|| '__|| | | || '_ \ | __|/ __|     | |  | '_ \  / _ \     \___ \  / _ \ | | | || |
 | |___| (_) || |   | |   | |_| || |_) || |_ \__ \     | |  | | | ||  __/      ___) || (_) || |_| || |
  \____|\___/ |_|   |_|    \__,_|| .__/  \__||___/_____|_|  |_| |_| \___|_____|____/  \___/  \__,_||_|
                                 |_|             |_____|                |_____|                        
"""

def is_port_free(port):
    """Cek apakah suatu port tersedia."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) != 0

def check_ports_in_range(start, end):
    """Cek port kosong dalam rentang tertentu."""
    print(f"\nMengecek port kosong dari {start} hingga {end}...\n")
    for port in range(start, end + 1):
        if is_port_free(port):
            print(f"Port {port} tersedia.")
    print("\nPengecekan selesai.")

def find_random_free_port():
    """Cari port kosong secara acak."""
    while True:
        port = random.randint(1024, 65535)
        if is_port_free(port):
            print(f"Port {port} tersedia.")
            break

def main():
    print(BANNER)
    print("\nPilih mode pengecekan:")
    print("1. Cek rentang port tertentu")
    print("2. Cari port kosong secara acak")
    
    choice = input("Masukkan pilihan (1/2): ").strip()
    
    if choice == "1":
        try:
            start = int(input("Masukkan port awal: "))
            end = int(input("Masukkan port akhir: "))
            check_ports_in_range(start, end)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    
    elif choice == "2":
        find_random_free_port()
    
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
