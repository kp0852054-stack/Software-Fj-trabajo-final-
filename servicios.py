

from abc import ABC, abstractmethod


# Clase para los servicios
class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
    @abstractmethod
    def calcular_costo(self, cantidad, descuento=0):
        pass
    @abstractmethod
    def describir_servicio(self):
        pass

# Servicio para reservar salas
class ReservaSala(Servicio):
    def calcular_costo(self, cantidad, descuento=0):
        if cantidad <= 0:
            raise ValueError("La cantidad de horas debe ser mayor que cero")
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        total = self.precio_base * cantidad
        return total - (total * descuento / 100)
    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"

# Servicio para alquilar equipos
class AlquilerEquipo(Servicio):
    def calcular_costo(self, cantidad, descuento=0):
        if cantidad <= 0:
            raise ValueError("La cantidad de dias debe ser mayor que cero")
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        total = self.precio_base * cantidad
        return total - (total * descuento / 100)
    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"

# Servicio de asesorias especiales
class Asesoria(Servicio):
    def calcular_costo(self, cantidad, descuento=0):
        if cantidad <= 0:
            raise ValueError("La cantidad de horas debe ser mayor que cero")
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        total = self.precio_base * cantidad
        return total - (total * descuento / 100)
    def describir_servicio(self):
        return f"Asesoria especializada: {self.nombre}"
