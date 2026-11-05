# -*- coding: utf-8 -*-
import asyncio
import base64
import os
import subprocess
import sys
import wave
import imageio_ffmpeg
import edge_tts

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\User\Desktop\Nueva carpeta\Canal de Ventas"
SCREENS_DIR = os.path.join(BASE_DIR, "_real_screens")
TEMP_DIR = os.path.join(BASE_DIR, "_temp_reels_build")
os.makedirs(TEMP_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "es-MX-DaliaNeural"
BG_MUSIC_PATH = os.path.join(BASE_DIR, "musica_corporativa_confianza.mp3")

# Definition of the 28 reels with specific real screen bindings and scripts
REELS = [
    {
        "day": 3,
        "filename": "reel_03_pos_venta_rapida.mp4",
        "system": "KINETIX POS",
        "tag": "PUNTO DE VENTA (TIENDAS)",
        "title": "Registra cobros y emite tickets en 3 segundos",
        "step1_title": "REGISTRO DE VENTA & CARRITO",
        "step2_title": "TICKET TÉRMICO & COMPROBANTE",
        "v1": "Si todavía usas cuadernos, notas de papel o una calculadora para cobrar en tu mostrador, estás perdiendo clientes y dinero en cada venta.",
        "v2": "Con Kinetix POS seleccionas los artículos en pantalla, ingresas el efectivo y en tres segundos imprimes el ticket térmico profesional.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day03_step1.png",
        "s2_img": "day03_step2.png"
    },
    {
        "day": 4,
        "filename": "reel_04_barberia_servicios.mp4",
        "system": "KINETIX POS",
        "tag": "BARBERÍAS & ESTÉTICAS",
        "title": "Controla servicios y comisiones en tu barbería o salón",
        "step1_title": "SERVICIOS DE BARBERÍA EN POS",
        "step2_title": "ALTA DE NUEVO SERVICIO EN CATÁLOGO",
        "v1": "Deja de hacer cálculos a mano al final de la semana para saber cuánto cobrar y pagar comisiones en tu barbería o salón.",
        "v2": "En Kinetix registras servicios como corte o barba, asignas al barbero en un clic y el sistema calcula comisiones y ventas al instante.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day04_step1.png",
        "s2_img": "day04_step2.png"
    },
    {
        "day": 5,
        "filename": "reel_05_registro_gastos.mp4",
        "system": "KINETIX POS",
        "tag": "CONTROL FINANCIERO",
        "title": "Registra gastos y salidas de caja chica en 5 segundos",
        "step1_title": "HISTORIAL DE GASTOS Y CAJA CHICA",
        "step2_title": "REGISTRAR NUEVA SALIDA OPERATIVA",
        "v1": "Nadie te lo dice, pero las pequeñas compras y salidas de caja chica no registradas son la fuga invisible número uno que drena las utilidades de tu negocio.",
        "v2": "En el módulo de gastos ingresas el concepto, monto y categoría en cinco segundos, descontando cada salida de tu balance diario en tiempo real.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day05_step1.png",
        "s2_img": "day05_step2.png"
    },
    {
        "day": 6,
        "filename": "reel_06_agregar_inventario.mp4",
        "system": "KINETIX POS",
        "tag": "CONTROL DE STOCK",
        "title": "Carga nuevos productos y códigos de barra al instante",
        "step1_title": "CATÁLOGO DE INVENTARIO Y STOCK",
        "step2_title": "ALTA RÁPIDA DE NUEVO PRODUCTO",
        "v1": "Si todavía usas hojas de Excel desactualizadas para contar tu mercancía, te aseguro que tienes pérdidas de stock o productos vencidos sin darte cuenta.",
        "v2": "En Kinetix agregas productos, escaneas códigos de barra y programas alertas automáticas de stock mínimo para no quedarte sin mercancía.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day06_step1.png",
        "s2_img": "day06_step2.png"
    },
    {
        "day": 7,
        "filename": "reel_07_corte_caja.mp4",
        "system": "KINETIX POS",
        "tag": "ARQUEO DE CAJA",
        "title": "Corte de caja en 1 clic con desglose exacto X y Z",
        "step1_title": "HISTORIAL DE FACTURAS EMITIDAS",
        "step2_title": "RESUMEN DE ARQUEO Y GANANCIA NETA",
        "v1": "¿Qué es mejor? ¿Perder dos horas al final del día contando tickets y buscando descuadres, o hacer tu corte de caja exacto en un solo clic?",
        "v2": "Kinetix registra cada venta en efectivo, tarjeta o transferencia y te entrega el arqueo de caja con desglose de ingresos y ganancia neta en segundos.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day07_step1.png",
        "s2_img": "day07_step2.png"
    },
    {
        "day": 8,
        "filename": "reel_08_usuarios_permisos.mp4",
        "system": "KINETIX POS",
        "tag": "SEGURIDAD & USUARIOS",
        "title": "4 perfiles independientes con PIN exclusivo para cajeros",
        "step1_title": "PANEL DE 4 USUARIOS DE LICENCIA",
        "step2_title": "RESTRICCIONES Y PERMISOS POR ROL",
        "v1": "Nadie te lo dice, pero dejar que cualquier empleado altere precios, borre ventas o mueva inventarios sin permisos es una invitación al robo hormiga.",
        "v2": "Con Kinetix configuras hasta cuatro usuarios con PIN exclusivo para que tus cajeros solo cobren, protegiendo tus costos y reportes confidenciales.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day08_step1.png",
        "s2_img": "day08_step2.png"
    },
    {
        "day": 9,
        "filename": "reel_09_exportar_excel.mp4",
        "system": "KINETIX POS",
        "tag": "REPORTES FINANCIEROS",
        "title": "Exporta tus ventas e inventarios a Excel en 1 clic",
        "step1_title": "EXPORTACIÓN DE STOCK Y COSTOS",
        "step2_title": "REPORTE COMPLETO DE VENTAS",
        "v1": "Cómo pasar de noches enteras cuadrando cuentas a mano a exportar todas las ventas, gastos e inventarios de tu empresa a Excel en un solo clic.",
        "v2": "El sistema genera una hoja de cálculo limpia con todos tus productos, costos, precios y márgenes de ganancia listos para tu contador.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day09_step1.png",
        "s2_img": "day09_step2.png"
    },
    {
        "day": 10,
        "filename": "reel_10_agendar_cita.mp4",
        "system": "KINETIX SALUD",
        "tag": "CLÍNICAS & CITAS",
        "title": "Agenda citas médicas por consultorio y especialista en segundos",
        "step1_title": "CALENDARIO GENERAL DE CITAS",
        "step2_title": "NUEVA RESERVA DE PACIENTE",
        "v1": "Si todavía usas una libreta de papel o chats dispersos para agendar pacientes, se te están cayendo citas valiosas todos los días.",
        "v2": "En Kinetix Salud seleccionas la fecha, la hora disponible y el médico especialista en segundos, sin riesgo de sobrecupos ni citas duplicadas.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day10_step1.png",
        "s2_img": "day10_step2.png"
    },
    {
        "day": 11,
        "filename": "reel_11_confirmar_whatsapp.mp4",
        "system": "KINETIX SALUD",
        "tag": "NOTIFICACIONES WHATSAPP",
        "title": "Confirma citas médicas por WhatsApp en 1 solo clic",
        "step1_title": "RECORDATORIOS DE CITAS PENDIENTES",
        "step2_title": "ENVÍO DE MENSAJE PERSONALIZADO",
        "v1": "Deja de perder horas llamando uno a uno a tus pacientes para recordarles su turno y evitar el ausentismo en tu clínica.",
        "v2": "Con un solo clic en la lista de citas abres un mensaje de confirmación por WhatsApp personalizado con fecha, hora y consultorio listo para enviar.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day11_step1.png",
        "s2_img": "day11_step2.png"
    },
    {
        "day": 12,
        "filename": "reel_12_expediente_clinico.mp4",
        "system": "KINETIX SALUD",
        "tag": "EXPEDIENTE DIGITAL",
        "title": "Expediente clínico confidencial y antecedentes médicos",
        "step1_title": "DIRECTORIO DE PACIENTES",
        "step2_title": "APERTURA DE FICHA Y ANTECEDENTES",
        "v1": "Nadie te lo dice, pero perder el historial de un paciente o no tener sus antecedentes clínicos a la mano es un grave riesgo profesional y médico.",
        "v2": "Con el expediente digital de Kinetix consultas diagnósticos previos, alergias y evolución clínica en segundos con total seguridad y confidencialidad.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day12_step1.png",
        "s2_img": "day12_step2.png"
    },
    {
        "day": 13,
        "filename": "reel_13_cobro_consulta.mp4",
        "system": "KINETIX SALUD",
        "tag": "FINANZAS MÉDICAS",
        "title": "Cobro de consulta médica y emisión de recibo desglosado",
        "step1_title": "CONSULTA & HONORARIOS MÉDICOS",
        "step2_title": "RECETA FORMAL Y COMPROBANTE",
        "v1": "¿Qué es mejor? ¿Tener recibos en papel perdidos por el consultorio, o cobrar consultas y emitir comprobantes profesionales digitales al instante?",
        "v2": "Registras honorarios y suministros utilizados, y el sistema genera la receta y recibo membretado con el logo de tu consultorio en segundos.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day13_step1.png",
        "s2_img": "day13_step2.png"
    },
    {
        "day": 14,
        "filename": "reel_14_gestion_doctores.mp4",
        "system": "KINETIX SALUD",
        "tag": "GESTIÓN CLÍNICA",
        "title": "Administra médicos, turnos y comisiones por consulta",
        "step1_title": "DIRECTORIO DE ESPECIALISTAS",
        "step2_title": "HORARIOS Y LIQUIDACIÓN MÉDICA",
        "v1": "Deja de enredarte coordinando los horarios, especialidades y porcentajes de pago de múltiples doctores en tu policlínico.",
        "v2": "Configura turnos, consultorios y liquidaciones automáticas de honorarios por cada paciente atendido de forma clara y sin desacuerdos.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day14_step1.png",
        "s2_img": "day14_step2.png"
    },
    {
        "day": 15,
        "filename": "reel_15_clinica_celular.mp4",
        "system": "KINETIX SALUD",
        "tag": "SALUD MÓVIL",
        "title": "Tu clínica médica disponible en tu celular o tablet",
        "step1_title": "AGENDA CLÍNICA EN PANTALLA MÓVIL",
        "step2_title": "WHATSAPP Y CITAS DESDE SMARTPHONE",
        "v1": "Cómo pasar de estar amarrado al escritorio de tu consultorio a revisar tu agenda médica y expedientes desde cualquier lugar en tu celular.",
        "v2": "Kinetix Salud se adapta a tu smartphone o tablet para confirmar pacientes y consultar fichas clínicas mientras te trasladas o visitas a domicilio.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day15_step1.png",
        "s2_img": "day15_step2.png"
    },
    {
        "day": 16,
        "filename": "reel_16_cotizacion_pdf.mp4",
        "system": "KINETIX CRM",
        "tag": "COTIZADOR B2B",
        "title": "Genera cotizaciones formales en PDF en 10 segundos",
        "step1_title": "CATÁLOGO DE PROPUESTAS COMERCIALES",
        "step2_title": "DOCUMENTO PDF CON LOGO Y PARTIDAS",
        "v1": "Si todavía usas plantillas de Word para enviar presupuestos a tus clientes, tu negocio se ve lento y poco profesional.",
        "v2": "En Kinetix CRM seleccionas el cliente, agregas las partidas y en diez segundos generas una cotización formal en PDF con tu marca y desglose.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day16_step1.png",
        "s2_img": "day16_step2.png"
    },
    {
        "day": 17,
        "filename": "reel_17_tablero_kanban.mp4",
        "system": "KINETIX CRM",
        "tag": "PIPELINE DE VENTAS",
        "title": "Tablero Kanban visual para cerrar tratos sin perder clientes",
        "step1_title": "EMBUDO COMERCIAL EN ETAPAS",
        "step2_title": "TRATO CERRADO Y GANADO",
        "v1": "Cómo pasar del desorden de no saber en qué etapa va cada cliente a tener un embudo comercial visual donde cerrar tratos es rápido y automático.",
        "v2": "Arrastra las tarjetas en el tablero Kanban desde prospecto hasta negociación, y celebra cada venta ganada con control total de tus ingresos.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day17_step1.png",
        "s2_img": "day17_step2.png"
    },
    {
        "day": 18,
        "filename": "reel_18_registro_leads.mp4",
        "system": "KINETIX CRM",
        "tag": "CAPTURA DE PROSPECTOS",
        "title": "Registra nuevos leads y asigna vendedores al instante",
        "step1_title": "BASE DE CLIENTES Y PROSPECTOS",
        "step2_title": "ALTA RÁPIDA DE NUEVO LEAD",
        "v1": "Deja de perder prospectos valiosos de Instagram, campañas y WhatsApp en chats dispersos que nadie atiende a tiempo.",
        "v2": "Registra cada interesado en segundos, define el monto del negocio y asigna el vendedor responsable para brindarle atención inmediata.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day18_step1.png",
        "s2_img": "day18_step2.png"
    },
    {
        "day": 19,
        "filename": "reel_19_seguimiento_cotizaciones.mp4",
        "system": "KINETIX CRM",
        "tag": "SEGUIMIENTO COMERCIAL",
        "title": "Seguimiento oportuno a cotizaciones pendientes",
        "step1_title": "COTIZACIONES EN NEGOCIACIÓN",
        "step2_title": "DETALLE Y RE-ENVÍO POR WHATSAPP",
        "v1": "Nadie te lo dice, pero más del setenta por ciento de las ventas corporativas se pierden simplemente por no hacer seguimiento en el momento justo.",
        "v2": "Tu tabla de cotizaciones te muestra qué propuestas siguen pendientes y te permite recontactar por WhatsApp en un clic para acelerar la compra.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day19_step1.png",
        "s2_img": "day19_step2.png"
    },
    {
        "day": 20,
        "filename": "reel_20_metas_comisiones.mp4",
        "system": "KINETIX CRM",
        "tag": "METAS & COMISIONES",
        "title": "Metas comerciales de vendedores y comisiones automáticas",
        "step1_title": "CUMPLIMIENTO DE CUOTA COMERCIAL",
        "step2_title": "USUARIOS Y COMISIONES POR VENTA",
        "v1": "Cómo pasar de confusiones y reclamos con tu equipo de ventas a tener metas comerciales claras y comisiones calculadas en tiempo real.",
        "v2": "Supervisa el avance de cada asesor hacia su cuota mensual y deja que el sistema calcule sus incentivos por venta de forma automática y transparente.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day20_step1.png",
        "s2_img": "day20_step2.png"
    },
    {
        "day": 21,
        "filename": "reel_21_taller_servicios.mp4",
        "system": "KINETIX POS",
        "tag": "TALLERES MECÁNICOS",
        "title": "Cobro de mano de obra y refacciones en un mismo ticket",
        "step1_title": "ORDEN DE TALLER: SERVICIOS Y REPUESTOS",
        "step2_title": "COMPROBANTE CON PLACA Y KILOMETRAJE",
        "v1": "¿Qué es mejor? ¿Anotar reparaciones en libretas grasientas, o facturar mano de obra y repuestos organizados desde tu tablet o celular?",
        "v2": "En Kinetix registras la placa, kilometraje y piezas utilizadas en una sola orden de servicio clara y profesional que genera confianza inmediata.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day21_step1.png",
        "s2_img": "day21_step2.png"
    },
    {
        "day": 22,
        "filename": "reel_22_restaurante_combos.mp4",
        "system": "KINETIX POS",
        "tag": "RESTAURANTES & CAFETERÍAS",
        "title": "Atención rápida por combos, bebidas y control de mesas",
        "step1_title": "PEDIDO DE COMIDAS & COMBOS EN POS",
        "step2_title": "TICKET DE MESA Y ORDEN DE COCINA",
        "v1": "Si todavía usas comandas en papel que se pierden o confunden en cocina, tu restaurante o cafetería está sufriendo demoras innecesarias.",
        "v2": "Con botones táctiles rápidos registras combos, bebidas y mesas, cobras en segundos y despachas los pedidos sin errores ni demoras.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day22_step1.png",
        "s2_img": "day22_step2.png"
    },
    {
        "day": 23,
        "filename": "reel_23_farmacia_busqueda.mp4",
        "system": "KINETIX POS",
        "tag": "FARMACIAS & MINIMARKETS",
        "title": "Búsqueda veloz de medicamentos y códigos de barra",
        "step1_title": "BÚSQUEDA Y SELECCIÓN DE MEDICAMENTOS",
        "step2_title": "TICKET DE FARMACIA Y RECETA",
        "v1": "Deja de buscar medicamentos a ciegas entre cientos de estantes sin saber cuánto stock te queda ni qué lote está por vencer en tu farmacia.",
        "v2": "Busca por nombre, principio activo o código de barras al instante, revisa la fecha de vencimiento y despacha con total agilidad y exactitud.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day23_step1.png",
        "s2_img": "day23_step2.png"
    },
    {
        "day": 24,
        "filename": "reel_24_multi_pantalla.mp4",
        "system": "KINETIX POS",
        "tag": "MULTI-PANTALLA LOCAL",
        "title": "Hasta 4 computadoras o tablets conectadas en red local",
        "step1_title": "CONFIGURACIÓN DE RED Y TERMINALES",
        "step2_title": "SINCRONIZACIÓN SIMULTÁNEA EN VIVO",
        "v1": "Casi nadie en tu sector está aprovechando esto: conectar hasta cuatro computadoras o tablets en tu negocio sin pagar servidores caros ni rentas mensuales.",
        "v2": "Con Kinetix tu mostrador principal, la oficina y tus vendedores operan sincronizados al mismo tiempo en red local con total estabilidad y rapidez.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day24_step1.png",
        "s2_img": "day24_step2.png"
    },
    {
        "day": 25,
        "filename": "reel_25_respaldo_seguro.mp4",
        "system": "KINETIX POS",
        "tag": "SEGURIDAD DE DATOS",
        "title": "Respaldo seguro en USB: tu información siempre bajo tu control",
        "step1_title": "PANEL DE COPIA DE SEGURIDAD LOCAL",
        "step2_title": "EXPORTACIÓN SEGURA DE INVENTARIO",
        "v1": "Nadie te lo dice, pero depender de sistemas en la nube que se caen cuando se va el internet o te bloquean si no pagas arriesga tu negocio.",
        "v2": "En Kinetix tu información comercial es cien por ciento tuya: respaldas tu base de datos completa a tu PC o memoria USB en un solo clic.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day25_step1.png",
        "s2_img": "day25_step2.png"
    },
    {
        "day": 26,
        "filename": "reel_26_licencia_vitalicia.mp4",
        "system": "KINETIX POS",
        "tag": "INVERSIÓN INTELIGENTE",
        "title": "$89 USD de por vida vs $600 anuales de suscripción",
        "step1_title": "LICENCIA VITALICIA 4 USUARIOS ACTIVA",
        "step2_title": "CERO MENSUALIDADES NI RENTAS",
        "v1": "¿Qué es mejor? ¿Pagar 600 dólares todos los años en suscripciones de software que nunca son tuyas, o pagar 89 dólares una sola vez en la vida?",
        "v2": "Con Kinetix aseguras una licencia vitalicia completa para hasta cuatro usuarios sin pagos recurrentes, sin letras pequeñas y con soporte incluido.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day26_step1.png",
        "s2_img": "day26_step2.png"
    },
    {
        "day": 27,
        "filename": "reel_27_soporte_garantia.mp4",
        "system": "KINETIX POS",
        "tag": "SOPORTE & GARANTÍA",
        "title": "7 asistencias técnicas anuales y soporte humano directo",
        "step1_title": "CONFIGURACIÓN Y CONTACTO DE SOPORTE",
        "step2_title": "4 PUESTOS DE TRABAJO ACTIVOS",
        "v1": "Casi nadie en tu sector está aprovechando esto: adquirir un software empresarial que incluye soporte técnico humano garantizado y cero mensualidades.",
        "v2": "Tu licencia vitalicia incluye siete asistencias técnicas durante el primer año con atención personalizada por WhatsApp para cualquier duda o configuración.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day27_step1.png",
        "s2_img": "day27_step2.png"
    },
    {
        "day": 28,
        "filename": "reel_28_tour_pos.mp4",
        "system": "KINETIX POS",
        "tag": "TOUR EN VIVO POS",
        "title": "Tour completo Kinetix POS: ventas, stock y arqueo",
        "step1_title": "TERMINAL COMPLETA DE PUNTO DE VENTA",
        "step2_title": "FACTURACIÓN Y LICENCIA VITALICIA",
        "v1": "Cómo pasar del caos de atender con filas lentas y stock descontrolado a tener una terminal de facturación rápida, moderna y profesional en tu local.",
        "v2": "Controla ventas, inventario con alertas de reposición y arqueo diario en una interfaz clara que cualquier colaborador domina en cinco minutos.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day28_step1.png",
        "s2_img": "day28_step2.png"
    },
    {
        "day": 29,
        "filename": "reel_29_tour_clinica.mp4",
        "system": "KINETIX SALUD",
        "tag": "TOUR EN VIVO SALUD",
        "title": "Tour completo Kinetix Salud: agenda, WhatsApp y expedientes",
        "step1_title": "AGENDA MULTI-DOCTOR EN TIEMPO REAL",
        "step2_title": "EXPEDIENTE Y RECETA MÉDICA FORMAL",
        "v1": "Casi nadie en tu sector está aprovechando esto: digitalizar expedientes, citas por consultorio y recordatorios automáticos por una fracción de lo habitual.",
        "v2": "Kinetix Salud organiza tu consultorio con agenda visual, notificaciones de WhatsApp y cobro transparente de consultas desde cualquier dispositivo.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day29_step1.png",
        "s2_img": "day29_step2.png"
    },
    {
        "day": 30,
        "filename": "reel_30_tour_crm.mp4",
        "system": "KINETIX CRM",
        "tag": "TOUR EN VIVO CRM",
        "title": "Tour completo Kinetix CRM: Kanban y cotizaciones PDF",
        "step1_title": "PIPELINE KANBAN Y CIERRE DE TRATOS",
        "step2_title": "COTIZADOR PDF EN 10 SEGUNDOS",
        "v1": "Casi nadie en tu sector está aprovechando esto: automatizar todo tu ciclo de ventas con CRM y cotizaciones en PDF con licencia vitalicia para cuatro usuarios.",
        "v2": "Aprovecha los últimos días para probar los tres sistemas en vivo y equipar tu empresa con la herramienta definitiva por un único pago de 89 dólares.",
        "v3": "Prueba este sistema gratis en tu celular o computadora. Comenta la palabra SISTEMA y te enviamos el enlace directo a tus mensajes privados.",
        "keyword": "SISTEMA",
        "s1_img": "day30_step1.png",
        "s2_img": "day30_step2.png"
    }
]

# Helper to convert image to base64
def to_b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

def get_system_step_html(system, tag, title, step_num, step_title, voice_text, keyword, img_b64):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      width: 1080px;
      height: 1920px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
      color: #0f172a;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 70px 60px 240px 60px; /* Zona segura inferior de 240px para evitar controles de video y UI de Reels */
      position: relative;
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <div class="space-y-4">
    <div class="flex items-center justify-between border-b border-slate-300 pb-5">
      <div class="flex items-center gap-3">
        <div class="w-12 h-12 rounded-2xl bg-emerald-500 flex items-center justify-center font-black text-slate-950 font-mono text-xl shadow-md">K</div>
        <div>
          <div class="font-extrabold text-slate-900 text-xl tracking-tight">{system}</div>
          <div class="text-xs font-mono uppercase tracking-widest text-emerald-600 font-extrabold">DEMO EN VIVO · SOFTWARE REAL</div>
        </div>
      </div>
      <span class="px-4 py-2 rounded-full bg-emerald-500/10 border border-emerald-500/40 text-emerald-700 font-mono text-sm font-extrabold shadow-sm">
        {tag}
      </span>
    </div>

    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-amber-500/15 border border-amber-500/30 text-amber-800 text-xs font-mono font-extrabold uppercase mb-2">
        <span>⚡</span> PASO {step_num} DE 2: {step_title}
      </div>
      <h1 class="text-3xl font-black text-slate-950 tracking-tight leading-tight">
        {title}
      </h1>
    </div>
  </div>

  <!-- Center Window Mockup with REAL Interface -->
  <div class="my-auto py-2">
    <div class="bg-white rounded-3xl border-2 border-slate-300 shadow-2xl overflow-hidden">
      <!-- Window Titlebar -->
      <div class="bg-slate-100 border-b border-slate-200 px-5 py-3 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-3.5 h-3.5 rounded-full bg-rose-400"></div>
          <div class="w-3.5 h-3.5 rounded-full bg-amber-400"></div>
          <div class="w-3.5 h-3.5 rounded-full bg-emerald-400"></div>
          <span class="ml-3 font-mono text-xs font-bold text-slate-500">{system} · Modo Claro Oficial</span>
        </div>
        <span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-mono font-extrabold">
          ● SISTEMA EN LÍNEA
        </span>
      </div>
      <!-- Real Interface Screenshot -->
      <div class="p-2.5 bg-slate-50 flex items-center justify-center">
        <img src="{img_b64}" class="w-full h-auto max-h-[820px] object-contain rounded-xl border border-slate-200 shadow-inner">
      </div>
    </div>
  </div>

  <!-- Bottom Lower Third Subtitles & CTA (Elevado y con tipografía grande de alto impacto) -->
  <div class="space-y-4">
    <!-- Subtitle Card -->
    <div class="p-7 rounded-3xl bg-white border-2 border-emerald-500/40 shadow-2xl">
      <div class="flex items-center gap-2 text-xs font-mono font-extrabold text-emerald-600 uppercase tracking-widest mb-2.5">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <span>🎙️ LOCUCIÓN OFICIAL</span>
      </div>
      <p class="text-[32px] font-black text-slate-950 leading-[1.25] tracking-tight">
        "{voice_text}"
      </p>
    </div>

    <!-- Call to action pill -->
    <div class="p-5 rounded-2xl bg-slate-900 text-white flex items-center justify-between shadow-xl border border-slate-800">
      <div class="flex items-center gap-3">
        <span class="text-3xl">💬</span>
        <div>
          <div class="text-xs text-emerald-400 font-mono font-extrabold uppercase">PRUÉBALO EN TU CELULAR AHORA:</div>
          <div class="text-lg font-black text-white">Comenta "<span class="text-amber-300">{keyword}</span>" y te enviamos la demo directa</div>
        </div>
      </div>
      <div class="px-4 py-2 rounded-xl bg-emerald-500 text-slate-950 font-black text-sm font-mono shadow-md">
        $89 VITALICIO
      </div>
    </div>
  </div>

</body>
</html>
"""

def get_cta_card_html(keyword, title):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      width: 1080px;
      height: 1920px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: radial-gradient(circle at 50% 30%, #1e293b 0%, #090d16 100%);
      color: #ffffff;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 90px 80px 220px 80px; /* Safe from bottom controls */
      position: relative;
    }}
  </style>
</head>
<body>
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 90px 80px;
      position: relative;
    }}
  </style>
</head>
<body>

  <!-- Top Branding -->
  <div class="flex items-center justify-between border-b border-slate-700/60 pb-6">
    <div class="flex items-center gap-3">
      <div class="w-14 h-14 rounded-2xl bg-emerald-500 flex items-center justify-center font-black text-slate-950 font-mono text-2xl shadow-lg shadow-emerald-500/20">K</div>
      <div>
        <div class="font-black text-white text-2xl tracking-tight">KINETIX SYSTEMS</div>
        <div class="text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold">SOFTWARE EMPRESARIAL VITALICIO</div>
      </div>
    </div>
    <span class="px-4 py-2 rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-mono text-sm font-extrabold">
      DEMO EN VIVO DISPONIBLE
    </span>
  </div>

  <!-- Center Action Box -->
  <div class="my-auto space-y-10 text-center">
    <div class="inline-flex items-center gap-3 px-6 py-2.5 rounded-full bg-emerald-500/15 border border-emerald-500/40 text-emerald-400 font-mono font-bold text-sm tracking-widest uppercase">
      <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
      ACCESO INSTANTÁNEO AL SISTEMA
    </div>

    <div class="space-y-4">
      <h2 class="text-5xl font-black text-white tracking-tight leading-tight">
        Pruébalo gratis en tu celular o PC ahora
      </h2>
      <p class="text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed">
        Descubre la velocidad y sencillez de Kinetix con las demos interactivas funcionales.
      </p>
    </div>

    <!-- Big Trigger Button -->
    <div class="p-10 rounded-3xl bg-slate-800/80 border-2 border-emerald-500/50 shadow-2xl space-y-6 max-w-xl mx-auto">
      <div class="text-sm font-mono uppercase tracking-widest text-emerald-400 font-extrabold">
        ESCRIBE EN LOS COMENTARIOS:
      </div>
      <div class="px-8 py-5 rounded-2xl bg-emerald-500 text-slate-950 font-black text-4xl font-mono tracking-wider shadow-lg shadow-emerald-500/30">
        "{keyword}"
      </div>
      <p class="text-sm text-slate-300 leading-relaxed font-semibold">
        Te enviamos el enlace directo a tus mensajes privados para probar el sistema y asegurar la oferta especial de <strong class="text-white">$89 USD de por vida</strong> (sin mensualidades).
      </p>
    </div>

    <!-- Guarantee Badges -->
    <div class="flex items-center justify-center gap-6 pt-4 text-xs font-mono text-slate-400">
      <span class="flex items-center gap-1.5"><strong class="text-white">✓</strong> 4 Usuarios</span>
      <span class="flex items-center gap-1.5"><strong class="text-white">✓</strong> Cero Rentas</span>
      <span class="flex items-center gap-1.5"><strong class="text-white">✓</strong> 7 Tickets Soporte</span>
    </div>
  </div>

  <!-- Footer Link -->
  <div class="text-center border-t border-slate-800 pt-6">
    <span class="font-mono text-xs text-slate-400">
      Tienda Oficial: <strong class="text-emerald-400">tinyurl.com/kinetixsistemasPOS</strong>
    </span>
  </div>

</body>
</html>
"""

async def generate_single_tts(text, out_mp3, out_wav):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(out_mp3)
    subprocess.run([
        FFMPEG_EXE, "-y", "-i", out_mp3,
        "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2",
        out_wav
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def generate_all_audio():
    print("Sintetizando locuciones neuronales de Jorge para los 28 Reels...")
    for idx, r in enumerate(REELS):
        d = r["day"]
        for s, text in [(1, r["v1"]), (2, r["v2"]), (3, r["v3"])]:
            mp3 = os.path.join(TEMP_DIR, f"day{d}_scene{s}.mp3")
            wav = os.path.join(TEMP_DIR, f"day{d}_scene{s}.wav")
            await generate_single_tts(text, mp3, wav)
        print(f"[{idx+1}/28] Audio generado para Día {d:02d}")
    print("Todas las locuciones neuronales listas.")

def render_all_frames():
    print("Renderizando escenas 1080x1920 con interfaces reales en Chrome...")
    for idx, r in enumerate(REELS):
        d = r["day"]
        b64_1 = to_b64(os.path.join(SCREENS_DIR, r["s1_img"]))
        b64_2 = to_b64(os.path.join(SCREENS_DIR, r["s2_img"]))
        
        # Frame 1
        h1 = get_system_step_html(r["system"], r["tag"], r["title"], 1, r["step1_title"], r["v1"], r["keyword"], b64_1)
        h1_path = os.path.join(TEMP_DIR, f"day{d}_scene1.html")
        p1_path = os.path.join(TEMP_DIR, f"day{d}_scene1.png")
        with open(h1_path, "w", encoding="utf-8") as f:
            f.write(h1)
        subprocess.run([
            CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--window-size=1080,1920", f"--screenshot={p1_path}",
            f"file:///{h1_path.replace(os.sep, '/')}"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Frame 2
        h2 = get_system_step_html(r["system"], r["tag"], r["title"], 2, r["step2_title"], r["v2"], r["keyword"], b64_2)
        h2_path = os.path.join(TEMP_DIR, f"day{d}_scene2.html")
        p2_path = os.path.join(TEMP_DIR, f"day{d}_scene2.png")
        with open(h2_path, "w", encoding="utf-8") as f:
            f.write(h2)
        subprocess.run([
            CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--window-size=1080,1920", f"--screenshot={p2_path}",
            f"file:///{h2_path.replace(os.sep, '/')}"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Frame 3 (CTA Card)
        h3 = get_cta_card_html(r["keyword"], r["title"])
        h3_path = os.path.join(TEMP_DIR, f"day{d}_scene3.html")
        p3_path = os.path.join(TEMP_DIR, f"day{d}_scene3.png")
        with open(h3_path, "w", encoding="utf-8") as f:
            f.write(h3)
        subprocess.run([
            CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--window-size=1080,1920", f"--screenshot={p3_path}",
            f"file:///{h3_path.replace(os.sep, '/')}"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"[{idx+1}/28] Frames renderizados para Día {d:02d}")
            
    print("Todas las escenas 1080x1920 renderizadas con interfaces reales.")

def get_audio_duration(wav_path):
    with wave.open(wav_path, "rb") as wf:
        return wf.getnframes() / float(wf.getframerate())

def encode_all_reels():
    print("Codificando video y mezclando música corporativa en los 28 Reels...")
    import time
    t0 = time.time()
    
    for idx, r in enumerate(REELS):
        d = r["day"]
        out_mp4 = os.path.join(BASE_DIR, r["filename"])
        
        # Audio paths
        w1 = os.path.join(TEMP_DIR, f"day{d}_scene1.wav")
        w2 = os.path.join(TEMP_DIR, f"day{d}_scene2.wav")
        w3 = os.path.join(TEMP_DIR, f"day{d}_scene3.wav")
        
        d1 = get_audio_duration(w1) + 0.3
        d2 = get_audio_duration(w2) + 0.3
        d3 = get_audio_duration(w3) + 0.5
        total_dur = d1 + d2 + d3

        # Frame paths
        p1 = os.path.join(TEMP_DIR, f"day{d}_scene1.png")
        p2 = os.path.join(TEMP_DIR, f"day{d}_scene2.png")
        p3 = os.path.join(TEMP_DIR, f"day{d}_scene3.png")

        # Concatenate audio
        concat_voice = os.path.join(TEMP_DIR, f"day{d}_voice_full.wav")
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-i", w1, "-i", w2, "-i", w3,
            "-filter_complex", "[0:0][1:0][2:0]concat=n=3:v=0:a=1[out]",
            "-map", "[out]", concat_voice
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Video concat script
        concat_txt = os.path.join(TEMP_DIR, f"day{d}_concat.txt")
        with open(concat_txt, "w", encoding="utf-8") as f:
            f.write(f"file '{p1.replace(os.sep, '/')}'\n")
            f.write(f"duration {d1:.2f}\n")
            f.write(f"file '{p2.replace(os.sep, '/')}'\n")
            f.write(f"duration {d2:.2f}\n")
            f.write(f"file '{p3.replace(os.sep, '/')}'\n")
            f.write(f"duration {d3:.2f}\n")
            f.write(f"file '{p3.replace(os.sep, '/')}'\n")

        silent_mp4 = os.path.join(TEMP_DIR, f"day{d}_silent.mp4")
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-f", "concat", "-safe", "0", "-i", concat_txt,
            "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
            "-r", "30", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22",
            "-t", f"{total_dur:.2f}",
            silent_mp4
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Mix with voice + corporate music
        fade_out_start = max(1.0, total_dur - 2.0)
        filter_complex = (
            f"[1:a]volume=1.20[v_aud];"
            f"[2:a]volume=0.14,afade=t=in:ss=0:d=1.0,afade=t=out:st={fade_out_start:.2f}:d=2.0[m_aud];"
            f"[v_aud][m_aud]amix=inputs=2:duration=first:dropout_transition=2[out_a]"
        )

        subprocess.run([
            FFMPEG_EXE, "-y",
            "-i", silent_mp4,
            "-i", concat_voice,
            "-ss", "0", "-i", BG_MUSIC_PATH,
            "-filter_complex", filter_complex,
            "-map", "0:v", "-map", "[out_a]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-t", f"{total_dur:.2f}",
            out_mp4
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        print(f"[{idx+1}/28] Día {d:02d} -> {r['filename']} ({total_dur:.1f}s) con Interfaz Real generado.")

    print(f"--- ¡LOS 28 REELS CON INTERFAZ REAL COMPLETADOS EN {time.time()-t0:.1f}s! ---")

async def main():
    await generate_all_audio()
    render_all_frames()
    encode_all_reels()

if __name__ == "__main__":
    asyncio.run(main())
