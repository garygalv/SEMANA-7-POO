# modelos/cuenta_bancaria.py
"""
Modelo que representa una Cuenta Bancaria.
Demuestra el uso de constructor (__init__) y destructor (__del__).
"""

class CuentaBancaria:
    """
    Clase que modela una cuenta bancaria simple.
    
    - __init__: Inicializa el titular, saldo y abre un archivo de registro personal por cuenta.
    - __del__: Cierra el archivo de registro y deja constancia de la destrucción del objeto.
    """
    
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Constructor de la clase CuentaBancaria.
        
        Qué inicializa:
        - Nombre del titular (obligatorio)
        - Saldo inicial (por defecto 0.0)
        - Abre un archivo de log específico para esta cuenta (para registrar movimientos)
        
        Parámetros:
            titular (str): Nombre del dueño de la cuenta
            saldo_inicial (float): Saldo con el que se crea la cuenta (opcional)
        """
        self.titular = titular
        self.saldo = saldo_inicial
        self.archivo_log = open(f"logs/movimientos_{titular.replace(' ', '_')}.txt", "a", encoding="utf-8")
        
        # Registro inicial en el log
        self._registrar(f"Cuenta creada | Saldo inicial: ${saldo_inicial:.2f}")
        
        print(f"[INIT] Cuenta creada para {self.titular} con saldo ${self.saldo:.2f}")

    def depositar(self, monto: float):
        """Método para depositar dinero."""
        if monto > 0:
            self.saldo += monto
            self._registrar(f"Depósito: +${monto:.2f} | Nuevo saldo: ${self.saldo:.2f}")
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto: float):
        """Método para retirar dinero."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            self._registrar(f"Retiro: -${monto:.2f} | Nuevo saldo: ${self.saldo:.2f}")
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Saldo insuficiente o monto inválido.")

    def _registrar(self, mensaje: str):
        """Método privado para escribir en el log."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.archivo_log.write(f"[{timestamp}] {mensaje}\n")
        self.archivo_log.flush()  # Asegura que se escriba inmediatamente

    def __del__(self):
        """
        Destructor de la clase CuentaBancaria.
        
        Qué realiza:
        - Registra que la cuenta fue destruida
        - Cierra el archivo de log para liberar el recurso
        
        Cuándo se ejecuta (en teoría):
        - Cuando el objeto ya no tiene referencias (garbage collector decide el momento)
        - Al finalizar el programa si aún existen referencias
        - NO está garantizado al 100% en todos los casos (por ejemplo: ciclos de referencias)
        
        Por eso en la práctica se prefiere context managers (with) o métodos .cerrar() explícitos.
        Aquí se usa para fines didácticos y para evidenciar su invocación.
        """
        self._registrar("Cuenta destruida / objeto eliminado")
        print(f"[DEL] Cuenta de {self.titular} destruida - archivo log cerrado")
        
        try:
            self.archivo_log.close()
        except Exception as e:
            print(f"[ERROR en __del__] No se pudo cerrar archivo: {e}")
            