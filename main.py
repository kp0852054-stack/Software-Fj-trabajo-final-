
import logging

from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import ErrorReserva, ErrorOperacion


# Configuracion del archivo para guardar los eventos y errores
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Funcion para ejecutar y controlar cada operacion
def ejecutar_operacion(numero, descripcion, accion):

    print(f"\nOPERACION {numero}: {descripcion}")
    try:
        resultado = accion()
        if resultado is not None:
            print(resultado)
        logging.info("Operacion %s realizada: %s", numero, descripcion)
    except Exception as error:
        print("Se presento un error:", error)
        logging.exception(
            "Error en la operacion %s: %s",
            numero,
            descripcion
        )
    finally:
        print("Fin de la operacion.")


# Datos iniciales del sistema

print("       SOFTWARE FJ")

# Operacion 1: Registrar un cliente
def registrar_cliente():
    global cliente
    cliente = Cliente(
        "C001",
        "Maria Marmol",
        "maria@gmail.com",
        "3256987512"
    )
    return "Cliente registrado correctamente."
ejecutar_operacion(1, "Registro de cliente", registrar_cliente)

# Operacion 2: Intentar registrar un cliente con correo incorrecto
def cliente_incorrecto():
    return Cliente(
        "C002",
        "David Ruiz",
        "correo_incorrecto",
        "3136851369"
    )
ejecutar_operacion(2, "Registro de cliente con datos incorrectos",
                   cliente_incorrecto)

# Operacion 3: Crear una reserva de sala
def crear_sala():
    global sala
    sala = ReservaSala("S01", "Sala principal", 50000)
    return sala.describir_servicio()

ejecutar_operacion(3, "Creacion de servicio de sala", crear_sala)

# Operacion 4: Crear un alquiler de equipo
def crear_equipo():
    global equipo
    equipo = AlquilerEquipo("E01", "Proyector", 30000)
    return equipo.describir_servicio()

ejecutar_operacion(4, "Creacion de alquiler de equipo", crear_equipo)

# Operacion 5: Crear una asesoria
def crear_asesoria():
    global asesoria
    asesoria = Asesoria("A01", "Asesoria tecnica", 80000)
    return asesoria.describir_servicio()

ejecutar_operacion(5, "Creacion de asesoria", crear_asesoria)

# Operacion 6: Crear y procesar una reserva
def crear_reserva():
    global reserva
    reserva = Reserva("R001", cliente, sala, 2)
    return reserva.procesar()

ejecutar_operacion(6, "Creacion de reserva exitosa", crear_reserva)

# Operacion 7: Confirmar la reserva
def confirmar_reserva():
    return reserva.confirmar()

ejecutar_operacion(7, "Confirmacion de reserva", confirmar_reserva)

# Operacion 8: Intentar crear una reserva con cantidad incorrecta
def reserva_incorrecta():
    return Reserva("R002", cliente, equipo, 0)

ejecutar_operacion(8, "Reserva con cantidad incorrecta",
                   reserva_incorrecta)

# Operacion 9: Cancelar una reserva
def cancelar_reserva():
    return reserva.cancelar()

ejecutar_operacion(9, "Cancelacion de reserva", cancelar_reserva)

# Operacion 10: Intentar procesar una reserva cancelada
def procesar_reserva_cancelada():
    return reserva.procesar()

ejecutar_operacion(10, "Procesamiento de reserva cancelada",
                   procesar_reserva_cancelada)

print("       FIN DEL PROGRAMA")
print("Los eventos y errores fueron guardados.")
