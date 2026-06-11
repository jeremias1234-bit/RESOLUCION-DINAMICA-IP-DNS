# Pinger CLI - Resolución Dinámica de IP y DNS 🛡️🦅

Este proyecto es un utilitario de consola interactiva desarrollado en **Python** utilizando la librería avanzada de manipulación y forja de paquetes **Scapy** en conjunto con la librería nativa **`socket`**. El sistema funciona como un analizador y verificador de conectividad inteligente que automatiza la traducción de nombres de dominio web a direcciones lógicas reales para inyectar peticiones ICMP directas en la red.

## ⚙️ Flujo del Sistema e Interacción con el Modelo OSI

El script procesa la entrada del usuario y ejecuta una transición fluida entre la resolución del nombre de dominio y la inyección del paquete en la capa de red:

```text
[ Usuario ingresa: google.com ]
               │
               ▼ (Consulta DNS Externa)
   [ socket.gethostbyname() ] ───> Descubre IP Real (ej: 142.250.191.142)
               │
               ▼ (Forja de Paquetes con Scapy)
   [ IP(dst=IP_Real) / ICMP() ] ───> Inyección de petición Eco (Ping)
               │
               ▼ (Escucha Activa / sr1)
   [ respuesta.show() ] ───> Desarma y visualiza la cabecera en consola
```

1. **Resolución de Nombres en Capa de Aplicación:** El script actúa como un cliente DNS nativo utilizando la red de internet para transformar un texto humano (ej: `google.com`) en la dirección IP numérica que entienden los routers.
2. **Forja Analítica de Paquetes:** Utilizando Scapy, apila las capas del Modelo OSI combinando la cabecera de Red (`IP`) con la cabecera de control `ICMP()` para dar forma manual a una petición Eco (Ping Request).
3. **Desarmado de Respuestas (Deep Packet Inspection):** Captura el paquete Eco-Reply que devuelve el servidor remoto y utiliza el atributo `.show()` para desglosar detalladamente en la consola campos como el `ttl` (Time to Live), longitud de datos y flags.

## 🚀 Requisitos e Instalación

Para inyectar paquetes lógicos crudos (*raw sockets*) en sistemas operativos Windows, se deben cumplir dos condiciones:
1. **Driver Npcap:** Instalar el motor de captura de red [Npcap](https://npcap.com) para habilitar el puente de inyección en la interfaz física.
2. **Elevación de Privilegios:** Ejecutar la terminal o la consola de desarrollo (VS Code) con clic derecho -> **Ejecutar como Administrador**.

---
*Desarrollado como laboratorio técnico de análisis de paquetes de control, resolución de nombres (DNS) e inyección lógica en ciberseguridad informática.*
