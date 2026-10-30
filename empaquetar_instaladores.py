import os
import zipfile

BASE_DIR = r"c:\Users\User\Desktop\Nueva carpeta\Canal de Ventas"
SYS_DIR = os.path.join(BASE_DIR, "sistemas")
INST_DIR = os.path.join(BASE_DIR, "instaladores")
os.makedirs(INST_DIR, exist_ok=True)

PACKAGES = [
    {
        "zip_name": "Kinetix-POS-Inventario-Installer.zip",
        "source_html": "kinetix-pos-inventario.html",
        "app_file": "Kinetix_POS_Facturacion_Inventario.html",
        "title": "Kinetix POS, Facturación & Control de Inventarios v3.0",
        "short_name": "Kinetix POS"
    },
    {
        "zip_name": "Kinetix-Clinica-Citas-Installer.zip",
        "source_html": "kinetix-clinica-citas.html",
        "app_file": "Kinetix_Med_Expedientes_Citas.html",
        "title": "Kinetix Med & Booking Suite (Expedientes, Consultas, Citas y Recordatorios)",
        "short_name": "Kinetix Med"
    },
    {
        "zip_name": "Kinetix-CRM-Automatizacion-Installer.zip",
        "source_html": "kinetix-crm-automatizacion.html",
        "app_file": "Kinetix_CRM_Cotizador_Automatizacion.html",
        "title": "Kinetix CRM, Captación de Leads, Cotizaciones PDF & Automatización",
        "short_name": "Kinetix CRM"
    }
]

for pkg in PACKAGES:
    zip_path = os.path.join(INST_DIR, pkg["zip_name"])
    src_path = os.path.join(SYS_DIR, pkg["source_html"])

    launcher_bat = f"""@echo off
title Lanzador Oficial - {pkg["title"]}
set "APP_PATH=%~dp0{pkg["app_file"]}"
if exist "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" (
    start "" /max "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --start-maximized --app="file:///%APP_PATH%"
    exit
)
if exist "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" (
    start "" /max "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --start-maximized --app="file:///%APP_PATH%"
    exit
)
if exist "%LocalAppData%\\Google\\Chrome\\Application\\chrome.exe" (
    start "" /max "%LocalAppData%\\Google\\Chrome\\Application\\chrome.exe" --start-maximized --app="file:///%APP_PATH%"
    exit
)
if exist "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" (
    start "" /max "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --start-maximized --app="file:///%APP_PATH%"
    exit
)
if exist "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" (
    start "" /max "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" --start-maximized --app="file:///%APP_PATH%"
    exit
)
start "" /max "%APP_PATH%"
"""

    manifest_json = f"""{{
  "name": "{pkg["title"]}",
  "short_name": "{pkg["short_name"]}",
  "start_url": "./{pkg["app_file"]}",
  "display": "standalone",
  "background_color": "#070b13",
  "theme_color": "#10b981"
}}"""

    readme_txt = f"""========================================================================
{pkg["title"].upper()}
LICENCIA CORPORATIVA WHITE-LABEL (HASTA 4 USUARIOS CON ROLES)
========================================================================

¡Felicidades por tu adquisición! Este paquete contiene tu sistema completo
100% funcional, autónomo y sin pagos mensuales.

1. CREDENCIALES DE ACCESO INICIAL (USUARIO PRINCIPAL / MASTER):
   - Usuario: Administrador / Director Principal
   - PIN de Acceso Inicial: 1234
   *(Puedes cambiar el PIN y los nombres de los 4 usuarios dentro del menú "4 Usuarios & Roles")*

2. CÓMO ABRIR E INSTALAR EN PC (WINDOWS / MAC):
   - Opción A (Modo Programa Nativo en Windows): Haz doble clic sobre el archivo
     "Iniciar_Sistema_Escritorio_PC.bat". El sistema se abrirá en su propia ventana
     dedicada como un software de escritorio.
   - Opción B (Cualquier sistema operativo): Haz doble clic en "{pkg["app_file"]}"
     y en la barra superior de Chrome o Edge haz clic en el icono "Instalar aplicación".

3. CÓMO INSTALAR EN MÓVILES (ANDROID / IPHONE) Y TABLETAS (IPAD / GALAXY TAB):
   - Pasa el archivo "{pkg["app_file"]}" a tu dispositivo móvil o ábrelo desde tu enlace privado.
   - En el menú del navegador selecciona "Agregar a la pantalla de inicio".

4. PERSONALIZACIÓN DE TU MARCA (WHITE-LABEL):
   - Inicia sesión con el Usuario Principal (PIN: 1234).
   - Entra a la pestaña "⚙️ Personalizar Marca".
   - Sube tu propio LOGO, escribe el nombre de tu empresa/clínica/comercio, moneda,
     teléfono, dirección e impuestos y presiona "Guardar".
   - Todos los tickets, facturas, recetas médicas y cotizaciones saldrán con TU LOGO.

5. GESTIÓN DE LOS 4 USUARIOS Y ROLES:
   - Entra a la pestaña "👥 4 Usuarios & Roles".
   - Como Usuario Principal puedes activar, renombrar, cambiar el PIN y asignar el rol
     de los otros 3 usuarios incluidos en tu licencia.

Soporte Técnico Kinetix Systems · Todos los derechos reservados.
"""

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(src_path, arcname=pkg["app_file"])
        zf.writestr("Iniciar_Sistema_Escritorio_PC.bat", launcher_bat)
        zf.writestr("manifest.json", manifest_json)
        zf.writestr("LEEME_GUIA_INSTALACION_Y_LICENCIA.txt", readme_txt)

    print(f"Instalador empaquetado con éxito: {zip_path}")
