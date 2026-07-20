from scapy.all import IP, ICMP, sr1
import socket

print("==================================================")
print("           RESOLUCIÓN DE IP Y DNS
print("==================================================")
destino_usuario = input("[>] Ingrese la web o IP para lanzar Ping (ej: google.com): ")
print("==================================================\n")

try:
    print(f"[+] Traduciendo dominio '{destino_usuario}' a través de DNS...")

    ip_real = socket.gethostbyname(destino_usuario)
    print(f"[+] OBJETIVO DETECTADO -> Nombre: {destino_usuario} | IP Real: {ip_real}\n")
    
    print(f"[+] Fabricando paquete ICMP (Ping) hacia {ip_real}...")

    paquete_ping = IP(dst=ip_real) / ICMP()

    print("[+] Enviando paquete por la red y esperando respuesta...")
    respuesta = sr1(paquete_ping, timeout=2, verbose=False)

    if respuesta is None:
        print(f"[-] No hubo respuesta de {ip_real} (Host caído o Firewall bloqueando ICMP).")
    else:
        print(f"\n[+] ¡ÉXITO! El servidor de {destino_usuario} ({ip_real}) respondió al Ping.")
        print("--------------------------------------------------")
        #Muestra en pantalla el paquete desarmado
        respuesta.show()

except socket.gaierror:
    print(f" [-] ERROR: No se pudo resolver el dominio '{destino_usuario}'. Revisá si está bien escrito o si tenés internet.")
except Exception as e:
    print(f" [.] Ocurrió un error inesperado: {e}")
