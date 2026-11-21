
from datetime import datetime
from excepciones import ErrorReserva, ErrorOperacion


# Clase para manejo de reservas
class Reserva:

    def __init__(self, codigo, cliente, servicio, cantidad):
        if cliente is None:
            raise ErrorReserva("Debe seleccionar un cliente")
        if servicio is None:
            raise ErrorReserva("Debe seleccionar un servicio")
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ErrorReserva("La cantidad debe ser mayor que cero")
        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"
        self.fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Calcular el valor de la reserva
    def calcular_total(self, descuento=0, impuesto=0):
        if descuento < 0 or descuento > 100:
            raise ErrorReserva("El descuento debe estar entre 0 y 100")
        if impuesto < 0:
            raise ErrorReserva("El impuesto no puede ser negativo")
        costo = self.servicio.calcular_costo(self.cantidad)
        valor_descuento = costo * descuento / 100
        subtotal = costo - valor_descuento
        total = subtotal + (subtotal * impuesto / 100)
        return round(total, 2)

    # Confirmar la reserva
    def confirmar(self):
        if self.estado != "Pendiente":
            raise ErrorOperacion(
                "Solo se pueden confirmar reservas pendientes"
            )
        self.estado = "Confirmada"
        return "La reserva fue confirmada correctamente"

    # Cancelar la reserva
    def cancelar(self):
        if self.estado == "Cancelada":
            raise ErrorOperacion("La reserva ya se encuentra cancelada")
        self.estado = "Cancelada"
        return "La reserva fue cancelada correctamente"

    # Procesar la reserva y mostrar su informacion
    def procesar(self):
        try:
            if self.estado == "Cancelada":
                raise ErrorReserva(
                    "No se puede procesar una reserva cancelada"
                )
            total = self.calcular_total()
        except ErrorReserva as error:
            raise ErrorReserva(
                "No fue posible procesar la reserva"
            ) from error
        else:
            return (
                f"\n----- INFORMACION DE LA RESERVA -----\n"
                f"Codigo: {self.codigo}\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Servicio: {self.servicio.describir_servicio()}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Fecha: {self.fecha}\n"
                f"Estado: {self.estado}\n"
                f"Total a pagar: ${total:,.2f}\n"
                f"-------------------------------------"
            )
        finally:
            print("Proceso de reserva finalizado.")
