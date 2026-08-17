from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional
class TipoDocumento(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre de documento")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del documento")

class Chico(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre del chico")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido del chico")
    edad: int = Field(..., gt=0, description="Edad del chico")
    tipoDocumento: TipoDocumento = Field(..., description="Tipo de documento")
    numeroDocumento: int = Field(..., ge=1000000, le=99999999, description="Numero de documento")

class Cliente(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre del cliente")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido del cliente")
    tipoDocumento: TipoDocumento = Field(..., description="Tipo de documento")
    numeroDocumento: int = Field(..., ge=1000000, le=99999999, description="Numero de documento")
    domicilio: str = Field(..., description="Domicilio del cliente")
    telefono: str = Field(..., min_length=8, max_length=15, description="Telefono del cliente")
    celular: str = Field(..., min_length=8, max_length=15, description="Celular del cliente")
    email: str = Field(..., description="Email del cliente")
    hijos: list[Chico] = Field(default_factory=list, description="Hijos del cliente")

class Coordinadora(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre de coordinadora")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido de coordinadora")

class EstadoFestejo(BaseModel):
    nombre: str = Field(..., description="Nombre del estado de festejo")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del estado del festejo")

class Asistencia(BaseModel):
    numeroAsistencia: int = Field(..., gt=0, description="Numero de asistencia")
    chico: Chico = Field(..., description="Chico de la asistencia")

class Festejo(BaseModel):
    fechaHoraInicio: datetime = Field(..., description="Fecha y hora de inicio del festejo")
    fechaHoraFin: datetime = Field(..., description="Fecha y hora de fin del festejo")
    listaAsistencias: list[Asistencia] = Field(default_factory=list, description="Lista de asistencias")
    coordinadora: Coordinadora = Field(..., description="Coordinadora asignada al festejo")
    estadoFestejo: EstadoFestejo = Field(..., description="Estado actual del festejo")

    def calcularCostoAdicional(self):
        if len(self.listaAsistencias) > 20:
            extras = len(self.listaAsistencias) - 20
            return extras * 5000
        return 0

class PaqueteReserva(BaseModel):
    nombre: str = Field(..., description="Nombre del paquete de reserva")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del paquete de reserva")
    costoPaquete: float = Field(..., gt=0, description="Costo del paquete")

    def getCostoPaquete(self):
        return self.costoPaquete

class Carpa(BaseModel):
    numero: int = Field(..., gt=0, description="Numero de carpa")
    ubicacion: str = Field(..., description="Ubicacion de carpa")

class Factura(BaseModel):
    numero: str = Field(..., description="Numero de factura")
    fechaHoraEmision: datetime = Field(..., description=" Fecha y hora de emision de factura")
    importeServicio: float = Field(..., gt=0, description="Importe de servicio")
    importeExtras: float = Field(..., gt=0, description="Importe extras")
    saldoPendiente: float = Field(..., gt=0, description="Saldo pendiente")
    importeTotal: float = Field(default=0.0, ge=0, description="Importe total")

    def calcularImporteTotal(self):
        self.importeTotal = self.importeServicio + self.importeExtras
        return self.importeTotal

class EstadoReserva(BaseModel):
    nombre: str = Field(..., description="Nombre de estado reserva")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del estado de reserva")

    def getNombre(self):
        return self.nombre

class CambioEstadoReserva(BaseModel):
    fechaHoraInicio: datetime = Field(default_factory=datetime.now, description="Fecha y hora de inicio del cambio de estado")
    fechaHoraFin: Optional[datetime] = Field(default=None, description="Fecha y hora de fin del cambio de estado")
    estadoReserva: EstadoReserva = Field(..., description="Estado asociadoa al cambio de estado reserva")

    def pasaron5Dias(self):
        tiempo_desde_cambio = datetime.now() - self.fechaHoraInicio
        return tiempo_desde_cambio >= timedelta(days=5)

    def setFechaHoraFin(self):
        self.fechaHoraFin = datetime.now()

    def getNombreEstado(self):
        return self.estadoReserva.getNombre()

class Reserva(BaseModel):
    fechaHoraFestejo: datetime = Field(..., description="Fecha y hora seleccionada para el festejo")
    observacion: Optional[str] = Field(default=None,description="Observacion adicional para el festejo")
    senia: float = Field(..., ge=0, description="Senia")

    cliente: Cliente = Field(..., description="Cliente")
    cumpleaniero: Chico = Field(..., description="Cumplaniero")

    listaCambiosEstado: list[CambioEstadoReserva] = Field(default_factory=list, description="Lista de cambios estado de la reserva")
    paqueteSeleccionado: PaqueteReserva = Field(..., description="Paquete seleccionado para el festejo")
    carpaSeleccionada: Carpa = Field(..., description="Carpa seleccionada para el festejo")

    festejo: Optional[Festejo] = Field(default=None, description="Festejo asociado a la reserva")
    factura: Optional[Factura] = Field(default=None, description="Factura correspondiente al festejo")

    def calcularCostoBase(self):
        return self.paqueteSeleccionado.getCostoPaquete()

    def calcularSenia(self):
        return self.calcularCostoBase() * 0.30

    def crearReserva(self):
        cambioEstado = CambioEstadoReserva(estadoReserva=EstadoReserva(nombre="Creada"))
        self.listaCambiosEstado.append(cambioEstado)

    def setPendienteConfirmacion(self):
        cambioEstado = CambioEstadoReserva(estadoReserva=EstadoReserva(nombre="PendienteDeConfirmacion"))
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)

    def pasaron5Dias(self):
        if not self.listaCambiosEstado:
            return False
        
        estado = self.listaCambiosEstado[-1].getNombreEstado()

        if estado and estado == "PendienteDeConfirmacion" and self.listaCambiosEstado[-1].pasaron5Dias():
            self.setAnulada()

    def setAnulada(self):
        cambioEstado = CambioEstadoReserva(estadoReserva=EstadoReserva(nombre="Anulada"))
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)

    def setSeniaPagada(self):
        cambioEstado = CambioEstadoReserva(estadoReserva=EstadoReserva(nombre="SeniaPagada"))
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)

    def generarContrato(self):
        pass

    def cancelarReserva(self):
        cambioEstado = CambioEstadoReserva(estadoReserva=EstadoReserva(nombre="Cancelada"))
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)

    def calcularRetencion(self):
        pass