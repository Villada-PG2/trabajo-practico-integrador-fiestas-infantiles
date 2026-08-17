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
    numeroDocumento: str = Field(..., min_length=7, max_length=8, pattern=r"^\d+$", description="Numero de documento")

    def mostrarChico(self):
        print("Nombre:", self.nombre, self.apellido)
        print("Edad:", self.edad)

class Cliente(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre del cliente")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido del cliente")
    tipoDocumento: TipoDocumento = Field(..., description="Tipo de documento")
    numeroDocumento: str = Field(..., min_length=7, max_length=8, pattern=r"^\d+$", description="Numero de documento")
    domicilio: str = Field(..., description="Domicilio del cliente")
    telefono: str = Field(..., min_length=8, max_length=15, pattern=r"^\d+$", description="Telefono del cliente")
    celular: str = Field(..., min_length=8, max_length=15, pattern=r"^\d+$", description="Celular del cliente")
    email: str = Field(..., description="Email del cliente")
    hijos: list[Chico] = Field(default_factory=list, description="Hijos del cliente")

    def mostrarCliente(self):
        print("Nombre:", self.nombre, self.apellido)
        print("Hijos:")
        if self.hijos:
            for hijo in self.hijos:
                hijo.mostrarChico()
        else:
            print("No tiene hijos")

class Coordinadora(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, description="Nombre de coordinadora")
    apellido: str = Field(..., min_length=3, max_length=30, description="Apellido de coordinadora")

    def mostrarCoordinadora(self):
        print(f"Coordinadora: {self.nombre} {self.apellido}")

class EstadoFestejo(BaseModel):
    nombre: str = Field(..., description="Nombre del estado de festejo")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del estado del festejo")

    def mostrarEstadoFestejo(self):
        print(f"Estado festejo: {self.nombre}")

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

        duracion = self.fechaHoraFin - self.fechaHoraInicio
        if duracion != timedelta(hours=2, minutes=45):
            raise ValueError("El festejo debe tener una duración de 2 horas y 45 minutos")
        return self
    
    def calcularCostoAdicional(self):
        if len(self.listaAsistencias) > 20:
            extras = len(self.listaAsistencias) - 20
            return extras * 5000
        return 0

    def mostrarFestejo(self):
        print("############### FESTEJO ################")
        print(f"Fecha: {self.fechaHoraInicio} - {self.fechaHoraFin}")
        self.coordinadora.mostrarCoordinadora()
        self.estadoFestejo.mostrarEstadoFestejo()
        

class PaqueteReserva(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, description="Nombre del paquete de reserva")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del paquete de reserva")
    costoPaquete: float = Field(..., gt=0, description="Costo del paquete")

    def getCostoPaquete(self):
        return self.costoPaquete

    def mostrarPaquete(self):
        print(f"Paquete: {self.nombre} - Costo: {self.costoPaquete}")

class Carpa(BaseModel):
    numero: int = Field(..., gt=0, description="Numero de carpa")
    ubicacion: str = Field(..., description="Ubicacion de carpa")

    def mostrarCarpa(self):
        print(f"Carpa: {self.numero} - Ubicacion: {self.ubicacion}")


class Factura(BaseModel):
    numero: str = Field(..., description="Numero de factura")
    fechaHoraEmision: datetime = Field(..., description=" Fecha y hora de emision de factura")
    importeServicio: float = Field(..., gt=0, description="Importe de servicio")
    importeExtras: float = Field(..., ge=0, description="Importe extras")
    saldoPendiente: float = Field(..., ge=0, description="Saldo pendiente")

    def calcularImporteTotal(self):
        return self.importeServicio + self.importeExtras

    def mostrarFactura(self):
        print("################ FACTURA ###################")
        print("Numero:", self.numero)
        print("Fecha de emision:", self.fechaHoraEmision)
        print("Importe del servicio:", self.importeServicio)
        print("Importe de extras:", self.importeExtras)
        print("Importe total:", self.calcularImporteTotal())
        print("Saldo pendiente:", self.saldoPendiente)

class EstadoReserva(BaseModel):
    nombre: str = Field(..., description="Nombre de estado reserva")
    descripcion: Optional[str] = Field(default=None,description="Descripcion del estado de reserva")

    def esCreada(self):
        return self.nombre == "Creada"

    def esPendienteConfirmacion(self):
        return self.nombre == "Pendiente de confirmacion"

    def esAnulada(self):
        return self.nombre == "Anulada"

    def esSeniaPagada(self):
        return self.nombre == "Senia Pagada"

    def esCancelada(self):
        return self.nombre == "Cancelada"

    def mostrarEstadoReserva(self):
        print(f"Estado de Reserva: {self.nombre}")

class CambioEstadoReserva(BaseModel):
    fechaHoraInicio: datetime = Field(default_factory=datetime.now, description="Fecha y hora de inicio del cambio de estado")
    fechaHoraFin: Optional[datetime] = Field(default=None, description="Fecha y hora de fin del cambio de estado")
    estadoReserva: Optional[EstadoReserva] = Field(default=None, description="Estado asociadoa al cambio de estado reserva")

    def setFechaHoraFin(self):
        self.fechaHoraFin = datetime.now()

    def conocerEstadosReserva(self):
        return ESTADOS_RESERVA

    def setCreada(self):
        estados: EstadoReserva = self.conocerEstadosReserva()
        creada = None
        for e in estados:
            if e.esCreada():
                creada = e
                break
        if creada == None:
            raise ValueError("No existe el estado creada")
        else:
            self.estadoReserva = creada

    def setPendienteConfirmacion(self):
        estados: EstadoReserva = self.conocerEstadosReserva()
        pendiente = None
        for e in estados:
            if e.esPendienteConfirmacion():
                pendiente = e
                break
        if pendiente == None:
            raise ValueError("No existe el estado pendiente de confirmacion")
        else:
            self.estadoReserva = pendiente

    def pasaron5Dias(self):
        return self.estadoReserva.esPendienteConfirmacion() and self.fechaHoraFin is None and datetime.now() - self.fechaHoraInicio >= timedelta(days=5)

    def setAnulada(self):
        estados: EstadoReserva = self.conocerEstadosReserva()
        anulada = None
        for e in estados:
            if e.esAnulada():
                anulada = e
                break
        if anulada == None:
            raise ValueError("No existe el estado anulada")
        else:
            self.estadoReserva = anulada

    def setSeniaPagada(self):
        estados: EstadoReserva = self.conocerEstadosReserva()
        seniaPagada = None
        for e in estados:
            if e.esSeniaPagada():
                seniaPagada = e
                break
        if seniaPagada == None:
            raise ValueError("No existe el estado senia pagada")
        else:
            self.estadoReserva = seniaPagada

    def setCancelada(self):
        estados: EstadoReserva = self.conocerEstadosReserva()
        cancelada = None
        for e in estados:
            if e.esCancelada():
                cancelada = e
                break
        if cancelada == None:
            raise ValueError("No existe el estado cancelada")
        else:
            self.estadoReserva = cancelada

    def mostrarEstadoReserva(self):
        self.estadoReserva.mostrarEstadoReserva()

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
        
        siPasaron = self.listaCambiosEstado[-1].pasaron5Dias()
        if siPasaron:
            self.setAnulada()
        return siPasaron

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

    def mostrarReserva(self):
        print("################ RESERVA ###################")
        print("Cumpleaniero:")
        self.cumpleaniero.mostrarChico()
        self.paqueteSeleccionado.mostrarPaquete()
        self.carpaSeleccionada.mostrarCarpa()
        print("Observacion:", self.observacion)

        if self.listaCambiosEstado:
            self.listaCambiosEstado[-1].mostrarEstadoReserva()
        else:
            print("Estado actual: Sin estado")