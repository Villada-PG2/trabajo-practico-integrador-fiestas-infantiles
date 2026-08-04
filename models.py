from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class TipoDocumento(BaseModel):
    nombre: str = Field(...)
    descripcion: str = Field(...)

class Chico(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)
    apellido: str = Field(..., min_length=3, max_length=30)
    edad: int = Field(..., gt=0)
    tipoDocumento: TipoDocumento = Field(...)
    numeroDocumento: int = Field(..., ge=1000000, le=99999999)

class Cliente(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)
    apellido: str = Field(..., min_length=3, max_length=30)
    tipoDocumento: TipoDocumento = Field(...)
    numeroDocumento: int = Field(..., ge=1000000, le=99999999)
    domicilio: str = Field(...)
    telefono: str = Field(..., min_length=8, max_length=15)
    celular: str = Field(..., min_length=8, max_length=15)
    email: str = Field(...)
    hijos: list[Chico] = []

class Coordinadora(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)
    apellido: str = Field(..., min_length=3, max_length=30)

class EstadoFestejo(BaseModel):
    nombre: str = Field(...)
    descripcion: str = Field(...)

class Asistencia(BaseModel):
    numeroAsistencia: int = Field(gt=0)
    chico: Chico

class Festejo(BaseModel):
    fechaHoraInicio: datetime = Field(...)
    fechaHoraFin: datetime = Field(...)
    listaAsistencias: list[Asistencia] = []
    coordinadora: Coordinadora = Field(...)
    estadoFestejo: EstadoFestejo = Field(...)

    def calcularCostoAdicional(self):
        if len(self.listaAsistencias) > 20:
            extras = len(self.listaAsistencias) - 20
            return extras * 5000
        return 0

class PaqueteReserva(BaseModel):
    nombre: str = Field(...)
    descripcion: str = Field(...)
    costoPaquete: float = Field(gt=0)

class Carpa(BaseModel):
    numero: int = Field(..., gt=0)
    ubicacion: str = Field(...,)

class Factura(BaseModel):
    numero: str
    fechaHoraemision: datetime
    importeServicio: float
    importeExtras: float
    saldoPendiente: float
    importeTotal: float

    def calcularImporteTotal(self):
        self.importeTotal = self.importeServicio + self.importeExtras
        return self.importeTotal

class EstadoReserva(BaseModel):
    nombre: str = Field(...)
    descripcion: str = Field(...)

class CambioEstadoReserva(BaseModel):
    fechaHoraInicio: datetime = Field(default_factory=datetime.now)
    fechaHoraFin: datetime | None = None
    estadoReserva: EstadoReserva = Field(...)

    def pasaron5Dias(self):
        tiempo_desde_cambio = datetime.now() - self.fechaHoraInicio
        return tiempo_desde_cambio >= timedelta(days=5)

    def setFechaHoraFin(self):
        self.fechaHoraFin = datetime.now()

    def getEstado(self):
        return self.estadoReserva