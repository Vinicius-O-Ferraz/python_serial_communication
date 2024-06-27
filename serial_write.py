
import serial
import time

class SerialMonitor:

    def __init__(self, port='COM6', baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        time.sleep(2)  # Aguarda a inicialização da conexão serial

    def send_command(self, command):
        self.ser.write(command.encode())
        time.sleep(0.1)  # Aguarda um curto período de tempo para resposta
        response = self.ser.readlines()
        return response

    def close(self):
        self.ser.close()

if __name__ == "__main__":
    try:
        monitor = SerialMonitor(port='COM6')
        # Demonstrando o uso do monitor
        response = monitor.send_command('U')  # Comando exemplo
        print("Resposta:", response)

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        monitor.close()