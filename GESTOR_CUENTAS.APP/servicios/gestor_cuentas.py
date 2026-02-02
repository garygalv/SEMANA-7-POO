# servicios/gestor_cuentas.py
"""
Capa de servicios: lógica de negocio que usa los modelos.
No contiene datos persistentes, solo orquesta operaciones.
"""

from modelos.cuenta_bancaria import CuentaBancaria


class GestorCuentas:
    """Servicio que gestiona múltiples cuentas bancarias."""
    
    def __init__(self):
        self.cuentas = {}  # diccionario: titular -> CuentaBancaria

    def crear_cuenta(self, titular: str, saldo_inicial: float = 0.0):
        """Crea una nueva cuenta y la registra en el gestor."""
        if titular in self.cuentas:
            print(f"Ya existe una cuenta para {titular}")
            return
        
        cuenta = CuentaBancaria(titular, saldo_inicial)
        self.cuentas[titular] = cuenta
        print(f"Cuenta registrada en el sistema para {titular}")

    def realizar_deposito(self, titular: str, monto: float):
        if titular in self.cuentas:
            self.cuentas[titular].depositar(monto)
        else:
            print(f"No se encontró cuenta para {titular}")

    def realizar_retiro(self, titular: str, monto: float):
        if titular in self.cuentas:
            self.cuentas[titular].retirar(monto)
        else:
            print(f"No se encontró cuenta para {titular}")

    def mostrar_saldos(self):
        """Muestra el estado actual de todas las cuentas."""
        if not self.cuentas:
            print("No hay cuentas registradas.")
            return
        
        print("\n--- Estado de cuentas ---")
        for titular, cuenta in self.cuentas.items():
            print(f"{titular}: ${cuenta.saldo:.2f}")
        print("-------------------------\n")

    def eliminar_cuenta(self, titular: str):
        """Elimina explícitamente una cuenta (invoca __del__ al perder referencia)."""
        if titular in self.cuentas:
            del self.cuentas[titular]  # Aquí se pierde la referencia → debería llamar a __del__
            print(f"Cuenta de {titular} eliminada del sistema")
        else:
            print(f"No se encontró cuenta para {titular}")
            