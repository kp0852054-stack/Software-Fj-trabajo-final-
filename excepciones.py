
# Errores Software FJ

# Error cuando los datos del cliente no son correctos
class ErrorCliente(Exception):
    pass

# Error cuando un servicio no esta disponible
class ErrorServicio(Exception):
    pass

# Error cuando una reserva no se puede realizar
class ErrorReserva(Exception):
    pass

# Error cuando se intenta realizar una operacion incorrecta
class ErrorOperacion(Exception):
    pass
