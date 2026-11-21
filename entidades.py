
from abc import ABC, abstractmethod

# entidades del sistema
class Entidad(ABC):
    def __init__(self, codigo):
        self._codigo = codigo
    @abstractmethod
    def mostrar_info(self):
        pass
#  registro de los clientes
class Cliente(Entidad):
    
    def __init__(self, codigo, nombre, correo, telefono):
        super().__init__(codigo)

        # Ver que los datos no esten vacios
        if not nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio")
        if "@" not in correo or "." not in correo:
            raise ValueError("El correo ingresado no es valido")
        if not telefono.isdigit() or len(telefono) < 7:
            raise ValueError("El telefono debe tener minimo 7 numeros")

        # Datos del cliente
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Consultar los datos del cliente
    @property
    def nombre(self):
        return self.__nombre
    @property
    def correo(self):
        return self.__correo
    @property
    def telefono(self):
        return self.__telefono
    # Mostrar la informacion del cliente
    def mostrar_info(self):
        return (
            f"Codigo: {self._codigo}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
