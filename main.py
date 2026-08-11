from datetime import datetime, timedelta
from os import name

from models import (
    TipoDocumento,
    Chico,
    Cliente,
    Coordinadora,
    EstadoFestejo,
    Asistencia,
    Festejo,
    PaqueteReserva,
    Carpa,
    Factura,
    EstadoReserva,
    CambioEstadoReserva,
    Reserva
)


def main():

    # =========================
    # TIPO DE DOCUMENTO
    # =========================

    tipo_documento = TipoDocumento(
        nombre="DNI",
        descripcion="Documento Nacional de Identidad"
    )


    # =========================
    # CHICO
    # =========================

    cumpleaniero = Chico(
        nombre="Juan",
        apellido="Perez",
        edad=10,
        tipoDocumento=tipo_documento,
        numeroDocumento=45678912
    )


    invitado = Chico(
        nombre="Pedro",
        apellido="Gomez",
        edad=11,
        tipoDocumento=tipo_documento,
        numeroDocumento=40123456
    )


    # =========================
    # CLIENTE
    # =========================

    cliente = Cliente(
        nombre="Carlos",
        apellido="Perez",
        tipoDocumento=tipo_documento,
        numeroDocumento=30123456,
        domicilio="Av. Siempre Viva 123",
        telefono="3511234567",
        celular="3517654321",
        email="carlos@gmail.com",
        hijos=[cumpleaniero]
    )


    # =========================
    # COORDINADORA
    # =========================

    coordinadora = Coordinadora(
        nombre="Maria",
        apellido="Gonzalez"
    )


    # =========================
    # ESTADO DEL FESTEJO
    # =========================

    estado_festejo = EstadoFestejo(
        nombre="Confirmado",
        descripcion="Festejo confirmado"
    )


    # =========================
    # ASISTENCIAS
    # =========================

    asistencia1 = Asistencia(
        numeroAsistencia=1,
        chico=cumpleaniero
    )

    asistencia2 = Asistencia(
        numeroAsistencia=2,
        chico=invitado
    )


    # =========================
    # FESTEJO
    # =========================

    festejo = Festejo(
        fechaHoraInicio=datetime(2026, 8, 20, 15, 0),
        fechaHoraFin=datetime(2026, 8, 20, 18, 0),
        listaAsistencias=[asistencia1, asistencia2],
        coordinadora=coordinadora,
        estadoFestejo=estado_festejo
    )


    # =========================
    # PAQUETE
    # =========================

    paquete = PaqueteReserva(
        nombre="Paquete A",
        descripcion="Festejo basico",
        costoPaquete=50000
    )


    # =========================
    # CARPA
    # =========================

    carpa = Carpa(
        numero=1,
        ubicacion="Sector Norte"
    )


    # =========================
    # RESERVA
    # =========================

    reserva = Reserva(
        fechaHoraInicio=datetime(2026, 8, 20, 15, 0),
        observacion="Cumpleaños de Juan",
        senia=15000,
        cliente=cliente,
        cumpleaniero=cumpleaniero,
        paqueteSeleccionado=paquete,
        carpaSeleccionada=carpa,
        festejo=festejo
    )


    # =========================
    # PRUEBAS
    # =========================

    print("===== DATOS DE LA RESERVA =====")

    print("Cliente:", reserva.cliente.nombre, reserva.cliente.apellido)
    print("Cumpleañero:", reserva.cumpleaniero.nombre)
    print("Paquete:", reserva.paqueteSeleccionado.nombre)
    print("Carpa:", reserva.carpaSeleccionada.numero)


    # Costo base

    print("\n===== COSTOS =====")

    print("Costo del paquete:",
          reserva.calcularCostoBase())

    print("Seña correspondiente:",
          reserva.calcularSenia())


    # Crear reserva

    print("\n===== ESTADOS =====")

    reserva.crearReserva()

    print(
        "Estado actual:",
        reserva.listaCambiosEstado[-1].getNombreEstado()
    )


    # Pasar a pendiente de confirmación

    reserva.setPendienteConfirmacion()

    print(
        "Estado actual:",
        reserva.listaCambiosEstado[-1].getNombreEstado()
    )


    # Pagar seña

    reserva.setSeniaPagada()

    print(
        "Estado actual:",
        reserva.listaCambiosEstado[-1].getNombreEstado()
    )


    # Cancelar reserva

    reserva.cancelarReserva()

    print(
        "Estado actual:",
        reserva.listaCambiosEstado[-1].getNombreEstado()
    )


    # =========================
    # COSTO ADICIONAL
    # =========================

    print("\n===== COSTO ADICIONAL =====")

    print(
        "Costo adicional del festejo:",
        festejo.calcularCostoAdicional()
    )


    # =========================
    # FACTURA
    # =========================

    factura = Factura(
        numero="F001",
        fechaHoraEmision=datetime.now(),
        importeServicio=reserva.calcularCostoBase(),
        importeExtras=festejo.calcularCostoAdicional(),
        saldoPendiente=0
    )

    factura.calcularImporteTotal()

    print("\n===== FACTURA =====")

    print("Número:", factura.numero)
    print("Importe servicio:", factura.importeServicio)
    print("Importe extras:", factura.importeExtras)
    print("Importe total:", factura.importeTotal)


if name == "__main__":
    main()