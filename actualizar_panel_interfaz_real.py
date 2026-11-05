# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from generar_reels_interfaz_real_completo import REELS

BASE_DIR = r"c:\Users\User\Desktop\Nueva carpeta\Canal de Ventas"
PANEL_PATH = os.path.join(BASE_DIR, "panel_30_dias_instagram.html")

HASHTAGS_MAP = {
    3: "#reels #puntodeventa #pos #sistemapos #abarrotes #comercio #ventasrapidas #kinetix",
    4: "#reels #barberia #barbershop #estetica #peluqueria #spadebelleza #comisiones #kinetix",
    5: "#reels #cajachica #gastosdelnegocio #controlfinanciero #finanzas #pymes #kinetix",
    6: "#reels #inventario #stock #codigodebarras #almacen #controlstock #retail #kinetix",
    7: "#reels #cortedecaja #arqueodecaja #cierredecaja #cajaregistradora #contabilidad #kinetix",
    8: "#reels #seguridadnegocio #cajeros #administracion #seguridad #pymes #kinetix",
    9: "#reels #excel #reportesfinancieros #contabilidad #datos #analisisdenegocio #kinetix",
    10: "#reels #clinicamedica #citasmedicas #agendamedica #consultorio #softwaremedico #kinetix",
    11: "#reels #whatsapp #confirmacioncitas #salud #odontologia #psicologia #consultorios #kinetix",
    12: "#reels #expedientemedico #historiaclinica #medicina #doctores #fichamedica #kinetix",
    13: "#reels #recibomedico #cobroconsultorio #honorarios #clinica #administracionmedica #kinetix",
    14: "#reels #doctores #especialistas #policlinico #gestionclinica #saludprivada #kinetix",
    15: "#reels #appmedica #saludmovil #medicoenmovimiento #tecnologiamedica #kinetix",
    16: "#reels #cotizaciones #crm #ventasb2b #presupuestos #propuestacomercial #kinetix",
    17: "#reels #kanban #crmventas #embudodeventas #pipeline #productividad #kinetix",
    18: "#reels #leads #prospectos #captacion #ventas #agenciadigital #servicios #kinetix",
    19: "#reels #seguimientocomercial #cierresdeventas #vendedores #negociacion #b2b #kinetix",
    20: "#reels #metasdeventas #comisiones #equipodeventas #liderazgo #ventas #kinetix",
    21: "#reels #tallermecanico #mecanica #serviciotecnico #repuestos #refaccionaria #kinetix",
    22: "#reels #restaurante #cafeteria #comidarapida #bares #hosteleria #kinetix",
    23: "#reels #farmacia #drogueria #minimarket #medicamentos #inventario #kinetix",
    24: "#reels #redlocal #multiterminal #puntodeventa #tecnologia #pymes #kinetix",
    25: "#reels #seguridadinformacion #backup #respaldo #basededatos #tranquilidad #kinetix",
    26: "#reels #ahorrointeligente #softwarevitalicio #sinrentas #inversionrentable #finanzas #kinetix",
    27: "#reels #soportetecnico #garantia #atencioncliente #tranquilidad #kinetix #respaldo",
    28: "#reels #demopos #tourvirtual #puntodeventa #probarsoftware #kinetix #demovivo",
    29: "#reels #democlinica #softwaremedico #saludintegral #doctores #kinetix #demovivo",
    30: "#reels #democrm #oportunidadunica #cierreoferta #lanzamiento #ventas #kinetix"
}

def get_week(day):
    if day <= 7: return 1
    if day <= 15: return 2
    if day <= 22: return 3
    return 4

def update_panel():
    with open(PANEL_PATH, "r", encoding="utf-8") as f:
        panel_content = f.read()

    start_marker = "const CAMPAIGN_DAYS = ["
    end_marker = "let currentSelectedDay = 1;"

    start_pos = panel_content.find(start_marker)
    end_pos = panel_content.find(end_marker)

    if start_pos == -1 or end_pos == -1:
        print("Error: Marcadores no encontrados en panel_30_dias_instagram.html")
        return

    days_list = []

    # DÍA 1
    day_1 = {
        "day": 1,
        "week": 1,
        "format": "🎥 REEL VERTICAL (DEMO EN VIVO)",
        "product": "Kinetix Multi-Dispositivo",
        "title": "Controla tu empresa en cualquier dispositivo sin invertir en costosos sistemas",
        "hook": "¿Qué es mejor? ¿Pagar miles de dólares al año en sistemas complicados que nadie sabe usar, o controlar tu empresa en PC, laptop y celular con un solo pago de por vida?",
        "mediaType": "video",
        "mediaFiles": ["reel_odoo_multidispositivo.mp4"],
        "script": """[00:00 - 00:08] Gancho: "¿Qué es mejor? ¿Pagar miles de dólares al año en sistemas complicados que nadie sabe usar, o controlar tu empresa en PC, laptop y celular con un solo pago de por vida? Mira esto."
[00:08 - 00:16] Adaptabilidad total: PC de mostrador, laptop y celular sincronizados.
[00:16 - 00:25] Para todo tipo de empresas: Retail, Salud privada y Servicios B2B.
[00:25 - 00:33] Oferta especial $89 USD pago único de por vida para 4 usuarios.
[00:33 - 00:43] CTA universal: Comenta la palabra SISTEMA y te enviamos el enlace directo al DM.""",
        "caption": """¿Qué es mejor? ¿Pagar miles de dólares al año en sistemas complicados que nadie en tu equipo sabe usar, o controlar tu empresa en PC, laptop y celular con un solo pago de por vida? 💻📱👇

En Kinetix creamos software de gestión empresarial que va directo al grano:
✅ 100% Práctico y Sencillo: Tu equipo aprende a usarlo en 5 minutos.
✅ Multi-Dispositivo: Úsalo en PC de mostrador, Laptop en oficina y Celular o Tablet en movilidad.
✅ Para Todo Negocio: Diseñado para tiendas, clínicas, distribuidoras, talleres y empresas en crecimiento.
✅ Cero Suscripciones: Olvídate de pagar mensualidades por usuario de por vida.

🔥 OFERTA DE LANZAMIENTO LIMITADA:
Asegura tu Licencia Vitalicia Oficial para hasta 4 usuarios simultáneos por un pago único de solo $89 USD (precio regular $189 USD). Incluye 7 tickets anuales de soporte técnico gratuito y respaldo local de tus datos.

👇 ¿Quieres probar la demo interactiva en tu celular o PC ahora mismo?
Comenta la palabra SISTEMA aquí abajo y te enviamos el enlace directo a tus mensajes privados para que pruebes los demos en vivo y aproveches la promoción.

🔗 Tienda y Demos en Vivo: https://tinyurl.com/kinetixsistemasPOS""",
        "keyword": "SISTEMA",
        "link": "https://tinyurl.com/kinetixsistemasPOS",
        "hashtags": "#reels #softwareempresarial #pos #sistemadeventas #kinetix #multidispositivo #pymes #negocios #sinrentas"
    }
    days_list.append(day_1)

    # DÍA 2
    day_2 = {
        "day": 2,
        "week": 1,
        "format": "📑 CARRUSEL EDUCATIVO (6 LÁMINAS)",
        "product": "Kinetix POS & Inventarios",
        "title": "5 Razones por las que tu empresa no necesita un sistema costoso y complicado",
        "hook": "¿Qué es mejor? ¿Pagar suscripciones mensuales caras que nunca terminas de pagar, o tener un software profesional con un solo pago de por vida?",
        "mediaType": "carousel",
        "mediaFiles": [
            "odoo_slide_1.png",
            "odoo_slide_2.png",
            "odoo_slide_3.png",
            "odoo_slide_4.png",
            "odoo_slide_5.png",
            "odoo_slide_6.png"
        ],
        "script": """Lámina 1: Portada estilo Odoo moderna con laptop y mockup claro.
Lámina 2: Razón 1 - Curva de aprendizaje cero vs sistemas lentos y pesados.
Lámina 3: Razón 2 - Sin rentas mensuales: pago único de $89 USD de por vida.
Lámina 4: Razón 3 - Multi-dispositivo en red local o nube privada.
Lámina 5: Razón 4 - Soporte técnico incluido con 7 tickets anuales.
Lámina 6: CTA - Comenta SISTEMA para enviarte la demo interactiva directa a tus mensajes.""",
        "caption": """¿Cuántas veces has visto empresas pagar cientos de dólares al mes por softwares que terminan usando al 10% porque nadie los entiende? 🤯

Desliza este carrusel y conoce la filosofía Kinetix:
👉 Facilidad real de uso desde el primer día.
👉 Información de tu negocio centralizada y segura.
👉 Un solo pago de $89 USD para hasta 4 usuarios, sin mensualidades sorpresa.

Comenta la palabra SISTEMA y te enviamos el acceso directo a la demo interactiva a tus mensajes privados.

🔗 Enlace oficial: https://tinyurl.com/kinetixsistemasPOS""",
        "keyword": "SISTEMA",
        "link": "https://tinyurl.com/kinetixsistemasPOS",
        "hashtags": "#carrusel #softwarepos #gestionempresarial #productividad #kinetix #negociosrentables #controltotal"
    }
    days_list.append(day_2)

    # DÍAS 3 AL 30 (REELS CON INTERFAZ REAL)
    for r in REELS:
        d = r["day"]
        script_text = f"""[00:00 - 00:07] Paso 1: {r['step1_title']}
Visual: Pantalla real de {r['system']} en Modo Claro operando en vivo.
Locución: "{r['v1']}"

[00:07 - 00:14] Paso 2: {r['step2_title']}
Visual: Sistema ejecutando la acción (comprobante, WhatsApp, PDF o modal).
Locución: "{r['v2']}"

[00:14 - 00:19] Llamado a la acción:
Visual: Tarjeta interactiva oficial invitando a probar la demo en vivo.
Locución: "{r['v3']}"
Acción: Comentar '{r['keyword']}' para recibir el enlace por DM."""

        caption_text = f"""{r['title']} 🚀👇

Mira en este video la demostración práctica de {r['system']} operando en tiempo real:
1️⃣ {r['step1_title']}: {r['v1']}
2️⃣ {r['step2_title']}: {r['v2']}

¿Por qué elegir Kinetix para tu negocio?
✅ 100% Práctico e Intuitivo: Tu equipo lo domina en 5 minutos sin cursos complicados.
✅ Multi-Dispositivo: Funciona en PC de mostrador, laptop y teléfono celular.
✅ Cero Suscripciones: Olvídate de mensualidades abusivas por usuario.
✅ Licencia Vitalicia Oficial: Un único pago de $89 USD para hasta 4 usuarios.
✅ Soporte Incluido: 7 asistencias técnicas gratuitas anuales con atención directa por WhatsApp.

👇 ¿Quieres probar la demo interactiva en tu celular o PC ahora mismo?
Comenta la palabra {r['keyword']} aquí abajo y te enviamos el enlace directo a tus mensajes privados para probar el sistema en vivo.

🔗 Tienda y Demos en Vivo: https://tinyurl.com/kinetixsistemasPOS"""

        day_obj = {
            "day": d,
            "week": get_week(d),
            "format": "🎥 REEL DEMO EN VIVO (INTERFAZ REAL)",
            "product": f"{r['system']} · {r['tag']}",
            "title": r["title"],
            "hook": r["v1"],
            "mediaType": "video",
            "mediaFiles": [r["filename"]],
            "script": script_text,
            "caption": caption_text,
            "keyword": r["keyword"],
            "link": "https://tinyurl.com/kinetixsistemasPOS",
            "hashtags": HASHTAGS_MAP.get(d, "#reels #softwareempresarial #pos #kinetix")
        }
        days_list.append(day_obj)

    js_code = "const CAMPAIGN_DAYS = " + json.dumps(days_list, ensure_ascii=False, indent=2) + ";\n\n    "
    new_panel_content = panel_content[:start_pos] + js_code + panel_content[end_pos:]

    with open(PANEL_PATH, "w", encoding="utf-8") as f:
        f.write(new_panel_content)

    print(f"Panel actualizado exitosamente con las interfaces reales para los {len(days_list)} días.")

if __name__ == "__main__":
    update_panel()
