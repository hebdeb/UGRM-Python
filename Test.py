from netmiko import ConnectHandler

# Datos de conexión al dispositivo Cisco
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.5.201',         # Dirección IP o nombre de host del dispositivo
    'username': 'admin',          # Nombre de usuario
    'password': 'admin',       # Contraseña
    'secret': 'admin',  # Contraseña del modo privilegiado (si es necesario)
    'port': 22,                   # Puerto SSH (por defecto es 22)
}

# Conectar al dispositivo
connection = ConnectHandler(**cisco_device)

# Entrar en modo privilegiado (si es necesario)
connection.enable()

# Comandos de configuración
config_commands = ['interface Ethernet0/1',
    'description Conexion a la red interna',
    'ip address 192.168.1.1 255.255.255.0',
    'no shutdown']

# Enviar los comandos de configuración
output = connection.send_config_set(config_commands)

# Mostrar la salida de los comandos
print(output)

# Guardar la configuración
connection.save_config()

show_commands = [
    'show ip interface brief',
    'show version',
    'show running-config',
]

# Ejecutar los comandos 'show' y mostrar la salida
for command in show_commands:
    output = connection.send_command(command)
    print(f"Output for '{command}':\n{output}\n{'-'*40}\n")

# Cerrar la conexión
connection.disconnect()
