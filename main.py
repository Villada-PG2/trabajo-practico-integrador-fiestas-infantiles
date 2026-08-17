from datetime import datetime, timedelta

from models import (
    ESTADOS_RESERVA,
    ESTADOS_FESTEJO,
    TipoDocumento,
    Chico,
    Cliente,
    EstadoReserva,
    EstadoFestejo,
    Coordinadora,
    Festejo,
    Factura,
    PaqueteReserva,
    Carpa,
    Reserva
)


ESTADOS_RESERVA.extend([
    EstadoReserva(nombre="Creada", descripcion="Reserva creada"),
    EstadoReserva(nombre="Pendiente de confirmacion", descripcion="Reserva pendiente de confirmacion"),
    EstadoReserva(nombre="Anulada", descripcion="Reserva anulada por caducidad"),
    EstadoReserva(nombre="Senia Pagada", descripcion="Seña pagada"),
    EstadoReserva(nombre="Cancelada", descripcion="Reserva cancelada")
])

ESTADOS_FESTEJO.extend([
    EstadoFestejo(nombre="Pendiente", descripcion="Festejo pendiente"),
    EstadoFestejo(nombre="Realizado", descripcion="Festejo realizado"),
    EstadoFestejo(nombre="Cancelado", descripcion="Festejo cancelado")
])


tipoDocumento = TipoDocumento(nombre="DNI", descripcion="Documento Nacional de Identidad")

hijo1 = Chico(nombre="Mateo", apellido="Gomez", edad=8, tipoDocumento=tipoDocumento, numeroDocumento="45678901")
hijo2 = Chico(nombre="Sofia", apellido="Perez", edad=10, tipoDocumento=tipoDocumento, numeroDocumento="46789012")


cliente1 = Cliente(
    nombre="Juan",
    apellido="Gomez",
    tipoDocumento=tipoDocumento,
    numeroDocumento="30123456",
    domicilio="Av. Colon 123",
    telefono="3514567890",
    celular="3515678901",
    email="juan@gmail.com",
    hijos=[hijo1]
)

cliente2 = Cliente(
    nombre="Maria",
    apellido="Perez",
    tipoDocumento=tipoDocumento,
    numeroDocumento="31234567",
    domicilio="Bv. San Juan 456",
    telefono="3516789012",
    celular="3517890123",
    email="maria@gmail.com",
    hijos=[hijo2]
)


paqueteA = PaqueteReserva(nombre="Paquete A", descripcion="Uso de los juegos acorde a la edad, una coordinadora.", costoPaquete=80000)
paqueteB = PaqueteReserva(nombre="Paquete b", descripcion="Incluye la opción A más 10 litros de bebida y los descartables para niños.", costoPaquete=100000)
paqueteC = PaqueteReserva(nombre="Paquete b", descripcion="Incluye la opción B, más la comida para todos los invitados y los descartables para adultos.", costoPaquete=120000)

carpa1 = Carpa(numero=1, ubicacion="Sector norte")
carpa2 = Carpa(numero=2, ubicacion="Sector sur")

ahora = datetime.now()


reserva1 = Reserva(
    fechaHoraFestejo=ahora + timedelta(days=10),
    cliente=cliente1,
    cumpleaniero=hijo1,
    paqueteSeleccionado=paqueteA,
    carpaSeleccionada=carpa1
)

reserva1.crearReserva()
reserva1.cancelarReserva()


reserva2 = Reserva(
    fechaHoraFestejo=ahora + timedelta(days=15),
    observacion="El cumpleañero es alérgico al maní. Evitar alimentos que contengan maní.",
    cliente=cliente2,
    cumpleaniero=hijo2,
    paqueteSeleccionado=paqueteC,
    carpaSeleccionada=carpa2
)

reserva2.crearReserva()
reserva2.setPendienteConfirmacion()
reserva2.setSeniaPagada()


print("========== CLIENTE 1 ==========")
cliente1.mostrarCliente()

print("\n========== CLIENTE 2 ==========")
cliente2.mostrarCliente()

print("\n========== RESERVA 1 ==========")
reserva1.mostrarReserva()

print("\n========== RESERVA 2 ==========")
reserva2.mostrarReserva()

coordinadora = Coordinadora(nombre="Laura", apellido="Fernandez")

festejo2 = Festejo(
    fechaHoraInicio=reserva2.fechaHoraFestejo,
    fechaHoraFin=reserva2.fechaHoraFestejo + timedelta(hours=2, minutes=45),
    coordinadora=coordinadora,
    estadoFestejo=ESTADOS_FESTEJO[0]
)

factura2 = Factura(
    numero="0001",
    fechaHoraEmision=ahora,
    importeServicio=reserva2.calcularCostoBase(),
    importeExtras=0,
    saldoPendiente=reserva2.calcularCostoBase() - reserva2.calcularSenia()
)

print("\n---------------- FESTEJOS ----------------\n")
festejo2.mostrarFestejo()

print("\n---------------- FACTURAS ----------------\n")
factura2.mostrarFactura()