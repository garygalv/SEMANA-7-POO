# main.py
"""
Punto de entrada del programa - Semana 7 POO
Demuestra constructores y destructores con arquitectura modelos/servicios.
"""

from servicios.gestor_cuentas import GestorCuentas


def main():
    print("=== Sistema de Gestión de Cuentas Bancarias ===\n")
    
    gestor = GestorCuentas()
    
    # Crear cuentas (se ejecuta __init__)
    gestor.crear_cuenta("César Moisés", 1500.0)
    gestor.crear_cuenta("María López", 800.0)
    
    gestor.mostrar_saldos()
    
    # Operaciones
    gestor.realizar_deposito("César Moisés", 500.0)
    gestor.realizar_retiro("María López", 200.0)
    
    gestor.mostrar_saldos()
    
    # Eliminación explícita de una cuenta (debería disparar __del__)
    print("\nEliminando cuenta de María López...")
    gestor.eliminar_cuenta("María López")
    
    # Al finalizar main(), el gestor y la cuenta restante pierden referencia
    # → garbage collector debería llamar a __del__ de la cuenta de César

    print("\nFin del programa. Observa los mensajes [DEL] para ver destructores.")


if __name__ == "__main__":
    main()
    
    # Extra: forzar recolector de basura para evidenciar __del__ (solo didáctico)
    import gc
    gc.collect()
    print("\nForzado garbage collector → verifica si aparecen más [DEL]")