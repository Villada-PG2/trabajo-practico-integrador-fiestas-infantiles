# Dominio Fiestas Infantiles

SuperPark es un parque de diversiones ubicado en el Parque Sarmiento de la ciudad de Córdoba que ofrece, entre sus servicios, el festejo de cumpleaños a niños de 1 a 12 años. La empresa ha solicitado el diseño e implementación de un sistema de información que le permita gestionar los procesos relacionados con la reserva y realización del servicio de festejos de cumpleaños. 
Para ofrecer este servicio la empresa cuenta con 10 carpas ubicadas en el predio, dentro del parque de diversiones. En cada carpa puede realizarse un máximo de tres servicios por día. La duración de cada servicio es de 2:45 hs.; y tiene una hora de inicio y una hora de fin establecida. Cada carpa está preparada con mesas, sillas y una heladera, y se identifican con un número y una ubicación.
Los tipos de servicio que se ofrecen son:
* __Opción A__ Uso de los juegos acorde a la edad, una coordinadora.
* __Opción B__ Incluye la opción A más 10 litros de bebida y los descartables para niños.
* __Opción C__ Incluye la opción B, más la comida para todos los invitados y los descartables para adultos.

Cada opción define su costo considerando un máximo de 20 niños, y se ha establecido un importe adicional por cada niño extra que asista al cumpleaños. Sólo se aceptan pagos de contado efectivo.
Cuando una persona interesada solicita información del servicio lo puede hacer personal o telefónicamente, ante lo cual el responsable de atención al público (RAP) le ofrece información de la modalidad del servicio (tipo de servicios y precios). Aquella persona que decida realizar una reserva también puede hacerlo personal o telefónicamente. En ambos casos la persona debe informar la fecha del festejo, con lo cual el RAP verifica la disponibilidad en el día solicitado, buscando de los horarios
predeterminados aquellos que se encuentren libres. El RAP informa al cliente la disponibilidad, si la persona está de acuerdo con una fecha y horario, se toman los datos del cliente responsable (padre, madre o responsable del niño: apellido y nombre, tipo y número de documento, domicilio completo, teléfono, celular, email) y datos del niño (nombre, apellido, tipo y número de documento, edad) del cual se festejará el cumpleaños (previa verificación si los mismos no existen), o se modifican los datos de ser necesario. También puede registrar alguna observación a tener en cuenta en el cumpleaños.
Si la persona está presente, debe realizar el pago de una seña correspondiente al 30 % del costo según el tipo de servicio elegido, de manera de confirmar la reserva, y se genera y entrega al cliente el contrato de cumpleaños donde se especifica todo lo pactado y el importe abonado como entrega. El saldo deberá ser abonado al finalizar el día del festejo.
Dicho contrato debe ser impreso en un formato previamente definido, que establece los márgenes de impresión y el membrete de la empresa en la esquina superior izquierda. Para ello cuenta con una impresora la cual se utiliza para realizar la impresión del contrato y todas las impresiones necesarias.
En cambio, si el contacto es telefónico, se realiza la reserva la cual se considera válida por 5 días hábiles en espera que la persona efectivice la misma, es decir que se presente a abonar el importe correspondiente como seña. Los días de validez a considerar pueden variar frecuentemente, por ello para cada reserva se registra la fecha de vigencia correspondiente. Si la persona se presenta dentro de este período y realiza el pago de la seña, se genera y entrega el contrato de cumpleaños del mismo modo que se describió anteriormente.


Diariamente el RAP consulta todas las reservas pendientes de confirmación, y anula aquellas que se vencieron, liberando la fecha y el horario previamente reservado.
El cliente puede cancelar la fiesta en cualquier momento y el monto que retiene la empresa dependerá del lapso en que se produzca dicha cancelación con respecto a la fecha pactada.
El Responsable de Servicios en función de los cumpleaños reservados para el día siguiente, organiza los recursos para cada servicio agendado, asignando además una coordinadora y actualizando el estado de cada cumpleaños como “organizado”. Cada mañana, dicho responsable emite las órdenes de trabajo que son entregadas a cada coordinadora de cada cumpleaños, para que se organice y separe los recursos asignados.
Llegado el momento de realizar el servicio, se presenta el cliente y el niño, y se inicia el cumpleaños. Por cada niño que asiste la coordinadora anota el nombre y apellido. Al finalizar el cumpleaños, la coordinadora totaliza la cantidad de niños asistentes y calcula la cantidad de niños extras, informa al cliente y remite esta información al Responsable de
Servicios. El cliente debe dirigirse ante dicho responsable, el cual obtiene el importe extra a abonar por niño que excede la cantidad establecida como mínima, y suma el saldo pendiente de pago, informando al cliente el importe total a pagar. En este momento se genera la factura por el total del servicio realizado. La factura debe contener los datos requeridos por la ley de facturación vigente. En caso que asistieran menos de 20 niños, igualmente se cobra el costo del servicio previamente establecido.
En forma periódica se generan informes de cantidad de fiestas realizadas y horarios más solicitados para su análisis y además se emite un reporte de ingresos para su respectivo control
Para las distintas tareas que realiza cuenta con una PC HP ALL IN ONE 18-1209LA y una impresora láser color HP Pro400. EL sistema solicitado a desarrollar deberá ajustarse a este equipamiento.
Por otro lado se estableció la necesidad de la realización de copias de restauración periódicas de la base de datos para lograr la recuperación ante fallas.
En relación a aspectos de seguridad, se deberá manejar cuentas de usuarios con permisos para accesos al sistema, y además se limitará el número de intentos de conexión no exitosos a tres, momento a partir del cual se inhabilita el usuario y se rechazan otros intentos hasta la correspondiente autorización del usuario supervisor.

__________________________________________________________________

## Reglas de negocio:
* __Edad permitida:__ Los cumpleaños son para niños de 1 a 12 años
*__ Capacidad y uso: __Máximo 3 servicios por día por cada una de las 10 carpas
* __Duración:__ Cada servicio dura exactamente 2 horas y 45 minutos
* __Base de facturación:__ El costo inicial cubre hasta 20 niños; se cobra un adicional por cada niño extra
* __Forma de pago:__ Solo se acepta efectivo
* __Confirmación de reserva:__ Requiere el pago de una seña del 30% del costo total
* __Reservas telefónicas:__ Tienen una validez de 5 días hábiles (variable) antes de ser anuladas si no se paga la seña
* __Cancelaciones:__ La empresa retiene un monto según la antelación de la cancelación
* __Seguridad del sistema:__ El usuario se inhabilita tras 3 intentos fallidos de conexión

## Objetivo:
Gestionar los procesos relacionados con la reserva y la realización del servicio de festejos de cumpleaños en SuperPark

## Límite:
* La verificación física de la edad de los niños.
* La gestión de los juegos del parque fuera del horario del evento.
* El cumplimiento externo de las leyes de facturación (el sistema solo emite según la norma)

## Entorno:
* Clientes (padres, madres o responsables)
* Niños (homenajeados e invitados)
* Responsable de Atención al Público (RAP)
* Responsable de Servicios
* Coordinadoras

## Alcance:

__1. Gestión de Clientes y Niños__
* 1.1 El sistema debe permitir la búsqueda de clientes y niños en la base de datos para verificar si ya existen
* 1.2 Debe permitir el registro de datos del cliente responsable: apellido, nombre, DNI, domicilio, teléfono, celular y email
* 1.3 Debe permitir el registro de datos del niño: nombre, apellido, DNI y edad
* 1.4 El sistema debe facilitar la modificación de datos de clientes o niños ya registrados

__2. Gestión de Reservas y Disponibilidad__
* 2.1 El sistema debe permitir la consulta de disponibilidad de las 10 carpas en fechas y horarios predeterminados
* 2.2 Debe permitir el registro de reservas (personales o telefónicas), incluyendo fecha, horario, tipo de servicio y observaciones
* 2.3 El sistema debe calcular y registrar la fecha de vigencia para las reservas telefónicas (basado en días hábiles configurables)
* 2.4 Debe permitir la anulación de reservas vencidas para liberar los espacios no confirmados con seña
* 2.5 El sistema debe gestionar la cancelación de fiestas, calculando el monto de retención según la fecha de cancelación

__3. Gestión de Pagos y Contratos__
* 3.1 El sistema debe registrar el pago de la seña (30% del costo total) únicamente en efectivo
* 3.2 Debe generar e imprimir el contrato de cumpleaños con el formato, membrete y márgenes predefinidos por la empresa
* 3.3 El sistema debe permitir el registro del pago del saldo final y de los cargos por niños extras al concluir el evento

__4. Administración de Servicios y Organización__
* 4.1 El sistema debe permitir la configuración de los costos de las opciones de servicio (A, B y C) y el precio por niño adicional
* 4.2 Debe permitir al Responsable de Servicios asignar una coordinadora a cada evento programado
* 4.3 El sistema debe permitir actualizar el estado del cumpleaños a “organizado” una vez asignados los recursos
* 4.4 Debe emitir órdenes de trabajo diarias para que cada coordinadora conozca sus recursos y tareas

__5. Control de Ejecución del Evento__
* 5.1 El sistema debe permitir el registro de asistencia de los niños (nombre y apellido) durante el festejo
* 5.2 Al finalizar, el sistema debe calcular automáticamente la cantidad de niños extras (aquellos que superen los 20 básicos)
* 5.3 El sistema debe totalizar el importe extra y sumarlo al saldo pendiente para obtener el monto final a cobrar

__6. Facturación y Reportes__
* 6.1 El sistema debe generar la factura legal por el total del servicio, cumpliendo con la normativa vigente
* 6.2 Debe generar informes estadísticos sobre la cantidad de fiestas realizadas y los horarios más solicitados
* 6.3 El sistema debe emitir reportes de ingresos periódicos para el control administrativo

## R.N.F.:
* __Hardware:__ El sistema debe funcionar en una PC HP All-in-One 18-1209LA y usar una impresora HP Pro400
* __Seguridad:__ Manejo de perfiles de usuario con permisos específicos y bloqueo por intentos fallidos
* __Respaldo:__ Realización periódica de copias de restauración de la base de datos
* __Formato:__ Impresión de contratos con márgenes y membrete predefinidos

## Entradas:
Entrada: Datos del cliente y del niño, tipo de servicio elegido, fecha y hora, registro de seña, lista de niños asistentes

## Salidas:
Salida: Contrato de cumpleaños impreso, órdenes de trabajo para coordinadoras, factura final, reportes de ingresos y estadísticas de uso
