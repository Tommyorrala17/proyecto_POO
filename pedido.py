from revista import Revista
from libro import Libro
from docente import Docente
from estudiante import Estudiante

class Pedido():

    def __init__(self, cedula, solicitante, lista_material ,fecha_prestamo ,fecha_devolucion):

        self._cedula = cedula
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        super(Pedido, self).__init__( cedula  = cedula , solicitante = solicitante , lista_material = lista_material , fecha_prestamo = fecha_prestamo ,
                                         fecha_devolucion = fecha_devolucion)

        def __str__(self):
            return f' Pedido : {self.__dict__.__str__}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, nuevo_solicitante):
        self._solicitante = nuevo_solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, nueva_lista_material):
        self._lista_material = nueva_lista_material


    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nueva_fecha_prestamo):
        self._fecha_prestamo = nueva_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha_devolucion):
        self._fecha_devolucion = nueva_fecha_devolucion


if __name__ == '__main__':
 #pedio1 = Pedido ( cedula = '09854521421', solicitante ='LUIS MACIAS', lista_material = 'DESARROLLO EN PYTHON', fecha_prestamo ='15 de Junio', fecha_devolucion = '17 de Junio')
 pedido2 = Pedido ( cedula = '0985115665', solicitante= 'Maria Castañeda', lista_material= 'revista', fecha_prestamo= '04/05/2023', fecha_devolucion= '09/05/2023' )
print (pedido2)