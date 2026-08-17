from pydantic import BaseModel, Field, model_validator, field_validator
from datetime import datetime, timedelta
from typing import Optional

ESTADOS_RESERVA = []
ESTADOS_FESTEJO = []

class TipoDocumento(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre de documento")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del documento")

class Chico(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre del chico")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido del chico")
    edad: int = Field(..., gt=0, description="Edad del chico")
    tipoDocumento: TipoDocumento = Field(..., description="Tipo de documento")
    numeroDocumento: str = Field(..., min_length=7, max_length=8, description="Numero de documento")

class Cliente(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre del cliente")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido del cliente")
    tipoDocumento: TipoDocumento = Field(..., description="Tipo de documento")
    numeroDocumento: str = Field(..., min_length=7, max_length=8, description="Numero de documento")
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

    @field_validator("fechaHoraInicio")
    @classmethod
    def validar_fecha_inicio(cls, value):
        if value <= datetime.now():
            raise ValueError("El festejo no puede comenzar en el pasado")
        return value
    
    @model_validator(mode="after") 
    def verificar_fechas(self): 
        if self.fechaHoraFin <= self.fechaHoraInicio:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin")
        return self

    @model_validator(mode="after")
    def verificar_duracion(self):
        duracion = self.fechaHoraFin - self.fechaHoraInicio
        if duracion != timedelta(hours=2, minutes=45):
            raise ValueError("El festejo debe tener una duración de 2 horas y 45 minutos")
        return self
    
    def calcularCostoAdicional(self):
        if len(self.listaAsistencias) > 20:
            extras = len(self.listaAsistencias) - 20
            return extras * 5000
        return 0

class PaqueteReserva(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, description="Nombre del paquete de reserva")
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

    def calcularImporteTotal(self):
        return self.importeServicio + self.importeExtras

class EstadoReserva(BaseModel):
    nombre: str = Field(..., description="Nombre de estado reserva")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del estado de reserva")

    def getNombre(self):
        return self.nombre

class CambioEstadoReserva(BaseModel):
    fechaHoraInicio: datetime = Field(default_factory=datetime.now, description="Fecha y hora de inicio del cambio de estado")
    fechaHoraFin: Optional[datetime] = Field(default=None, description="Fecha y hora de fin del cambio de estado")
    estadoReserva: Optional[EstadoReserva] = Field(default=None, description="Estado asociadoa al cambio de estado reserva")

    def pasaron5Dias(self):
        tiempo_desde_cambio = datetime.now() - self.fechaHoraInicio
        return tiempo_desde_cambio >= timedelta(days=5)

    def setFechaHoraFin(self):
        self.fechaHoraFin = datetime.now()

    def getNombreEstado(self):
        return self.estadoReserva.getNombre()

    def setCreada(self):
        pass

    def setPendienteConfirmacion(self):
        pass

    def pasaron5Dias(self):
        pass

    def setAnulada(self):
        pass

    def setSeniaPagada(self):
        pass

    def setAnulada(self):
        pass

    def serCancelada(self):
        pass

class Reserva(BaseModel):
    fechaHoraFestejo: datetime = Field(..., description="Fecha y hora seleccionada para el festejo")
    observacion: Optional[str] = Field(default=None,description="Observacion adicional para el festejo")

    cliente: Cliente = Field(..., description="Cliente")
    cumpleaniero: Chico = Field(..., description="Cumplaniero")

    listaCambiosEstado: list[CambioEstadoReserva] = Field(default_factory=list, description="Lista de cambios estado de la reserva")
    paqueteSeleccionado: PaqueteReserva = Field(..., description="Paquete seleccionado para el festejo")
    carpaSeleccionada: Carpa = Field(..., description="Carpa seleccionada para el festejo")

    festejo: Optional[Festejo] = Field(default=None, description="Festejo asociado a la reserva")
    factura: Optional[Factura] = Field(default=None, description="Factura correspondiente al festejo")

    @field_validator("fechaHoraFestejo")
    @classmethod
    def validar_fecha_festejo(cls, value: datetime):
        if value <= datetime.now():
            raise ValueError("El Festejo no puede ser asignado para un dia pasado")
        return value
    
    def calcularCostoBase(self):
        return self.paqueteSeleccionado.getCostoPaquete()

    def calcularSenia(self):
        return self.calcularCostoBase() * 0.30

    def crearReserva(self):
        cambioEstado = CambioEstadoReserva()
        self.listaCambiosEstado.append(cambioEstado)
        cambioEstado.setCreada()

    def setPendienteConfirmacion(self):
        cambioEstado = CambioEstadoReserva()
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)
        cambioEstado.setPendienteConfirmacion()

    def pasaron5Dias(self):
        if not self.listaCambiosEstado:
            return False
        
        estado = self.listaCambiosEstado[-1].getNombreEstado()

        if estado and estado == "PendienteDeConfirmacion" and self.listaCambiosEstado[-1].pasaron5Dias():
            self.setAnulada()

    def setAnulada(self):
        cambioEstado = CambioEstadoReserva()
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)
        cambioEstado.setAnulada()

    def setSeniaPagada(self):
        cambioEstado = CambioEstadoReserva()
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)
        cambioEstado.setSeniaPagada()

    def generarContrato(self):
        pass

    def cancelarReserva(self):
        cambioEstado = CambioEstadoReserva()
        if len(self.listaCambiosEstado) > 0: 
            self.listaCambiosEstado[-1].setFechaHoraFin()
        self.listaCambiosEstado.append(cambioEstado)
        cambioEstado.setCancelada()

    def calcularRetencion(self):
        pass