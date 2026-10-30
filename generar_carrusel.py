import os
import subprocess
import time

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1080px;
      height: 1350px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #080c15;
      color: #f1f5f9;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 80px 80px;
      position: relative;
    }
    .radial-bg {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.18) 0%, rgba(56, 189, 248, 0.08) 35%, transparent 70%);
      pointer-events: none;
    }
  </style>
</head>
<body>
  <div class="radial-bg"></div>
  __CONTENT__
</body>
</html>
"""

slides_content = [
    # Slide 1 (Portada)
    """
    <div class="relative z-10 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center font-bold text-emerald-400 font-mono text-lg">K</div>
        <span class="font-mono tracking-widest text-emerald-400 font-bold text-xl uppercase">Kinetix.OS</span>
      </div>
      <span class="text-xl text-slate-500 font-mono font-semibold">01 / 06</span>
    </div>

    <div class="relative z-10 my-auto space-y-8">
      <div class="inline-block px-5 py-2 rounded-full bg-red-500/10 border border-red-500/30 text-red-400 font-bold uppercase tracking-widest text-sm">
        Fuga Operativa Oculta
      </div>
      <h1 class="text-6xl font-black leading-[1.15] text-white">
        4 síntomas de que tu empresa superó a tus <span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">hojas de cálculo</span>
      </h1>
      <p class="text-2xl text-slate-400 font-normal leading-relaxed max-w-2xl">
        Y por qué necesitas un sistema digital propio antes de que termine el mes si quieres escalar en serio.
      </p>
    </div>

    <div class="relative z-10 flex items-center justify-between text-lg text-slate-400 pt-8 border-t border-slate-800">
      <span class="font-medium">Desliza para ver los 4 errores &rarr;</span>
      <div class="flex gap-2">
        <div class="w-3 h-3 rounded-full bg-emerald-400"></div>
        <div class="w-3 h-3 rounded-full bg-slate-800"></div>
        <div class="w-3 h-3 rounded-full bg-slate-800"></div>
      </div>
    </div>
    """,

    # Slide 2 (Problema 1)
    """
    <div class="relative z-10 flex items-center justify-between">
      <span class="text-xl font-bold text-emerald-400 font-mono tracking-wide">01 // EL PUENTE HUMANO</span>
      <span class="text-xl text-slate-500 font-mono font-semibold">02 / 06</span>
    </div>

    <div class="relative z-10 my-auto space-y-8">
      <div class="w-20 h-20 rounded-3xl bg-red-500/10 border border-red-500/30 text-red-400 flex items-center justify-center font-bold text-4xl">
        !
      </div>
      <h2 class="text-5xl font-black text-white leading-tight">
        Pasas más de 1 hora al día copiando y pegando datos
      </h2>
      <p class="text-2xl text-slate-300 leading-relaxed">
        De WhatsApp a Excel. De Excel a correos. De correos a facturación.
      </p>
      <div class="p-8 bg-slate-900/90 border border-slate-800 rounded-3xl space-y-3">
        <span class="text-xs font-bold uppercase tracking-wider text-red-400 block">La Realidad Financiera</span>
        <p class="text-xl text-slate-300 leading-relaxed">
          Estás pagando un salario completo para hacer una tarea mecánica que un script o bot automático ejecuta en <strong class="text-emerald-400">300 milisegundos</strong> y sin margen de error.
        </p>
      </div>
    </div>

    <div class="relative z-10 text-right text-lg text-slate-500 font-medium pt-8 border-t border-slate-800">
      Desliza &rarr;
    </div>
    """,

    # Slide 3 (Problema 2)
    """
    <div class="relative z-10 flex items-center justify-between">
      <span class="text-xl font-bold text-emerald-400 font-mono tracking-wide">02 // EL CUELLO DE BOTELLA</span>
      <span class="text-xl text-slate-500 font-mono font-semibold">03 / 06</span>
    </div>

    <div class="relative z-10 my-auto space-y-8">
      <div class="w-20 h-20 rounded-3xl bg-amber-500/10 border border-amber-500/30 text-amber-400 flex items-center justify-center font-bold text-4xl font-mono">
        02
      </div>
      <h2 class="text-5xl font-black text-white leading-tight">
        Si tú no estás encima, la empresa se detiene
      </h2>
      <p class="text-2xl text-slate-300 leading-relaxed">
        Tu equipo no sabe si el cliente ya pagó, dónde están los archivos o quién debe hacer la siguiente entrega.
      </p>
      <div class="p-8 bg-slate-900/90 border border-slate-800 rounded-3xl space-y-3">
        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block">Regla de Oro Empresarial</span>
        <p class="text-xl text-slate-300 leading-relaxed">
          Un negocio que depende de la memoria de las personas no es un activo escalable: es una cárcel para el fundador.
        </p>
      </div>
    </div>

    <div class="relative z-10 text-right text-lg text-slate-500 font-medium pt-8 border-t border-slate-800">
      Desliza &rarr;
    </div>
    """,

    # Slide 4 (Problema 3)
    """
    <div class="relative z-10 flex items-center justify-between">
      <span class="text-xl font-bold text-emerald-400 font-mono tracking-wide">03 // FUGA DE PROSPECTOS</span>
      <span class="text-xl text-slate-500 font-mono font-semibold">04 / 06</span>
    </div>

    <div class="relative z-10 my-auto space-y-8">
      <div class="w-20 h-20 rounded-3xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 flex items-center justify-center font-bold text-4xl font-mono">
        03
      </div>
      <h2 class="text-5xl font-black text-white leading-tight">
        Tus prospectos esperan horas para recibir cotización
      </h2>
      <p class="text-2xl text-slate-300 leading-relaxed">
        La probabilidad de cerrar una venta cae un <strong class="text-red-400">80%</strong> si tardas más de 15 minutos en responder.
      </p>
      <div class="p-8 bg-slate-900/90 border border-slate-800 rounded-3xl space-y-3">
        <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 block">Solución Tecnológica</span>
        <p class="text-xl text-slate-300 leading-relaxed">
          Un cotizador web propio o bot calificador envía la propuesta y el enlace de pago seguro en menos de <strong class="text-emerald-400">20 segundos</strong>, sin importar si son las 2 de la madrugada.
        </p>
      </div>
    </div>

    <div class="relative z-10 text-right text-lg text-slate-500 font-medium pt-8 border-t border-slate-800">
      Desliza &rarr;
    </div>
    """,

    # Slide 5 (Problema 4)
    """
    <div class="relative z-10 flex items-center justify-between">
      <span class="text-xl font-bold text-emerald-400 font-mono tracking-wide">04 // GASTO CAUTIVO</span>
      <span class="text-xl text-slate-500 font-mono font-semibold">05 / 06</span>
    </div>

    <div class="relative z-10 my-auto space-y-8">
      <div class="w-20 h-20 rounded-3xl bg-teal-500/10 border border-teal-500/30 text-teal-400 flex items-center justify-center font-bold text-4xl font-mono">
        04
      </div>
      <h2 class="text-5xl font-black text-white leading-tight">
        Pagas 5 softwares mensuales que nadie usa al 100%
      </h2>
      <p class="text-2xl text-slate-300 leading-relaxed">
        Pagas licencias en dólares que suben de precio cada año por herramientas genéricas y complejas.
      </p>
      <div class="p-8 bg-slate-900/90 border border-slate-800 rounded-3xl space-y-3">
        <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 block">La Alternativa de Élite</span>
        <p class="text-xl text-slate-300 leading-relaxed">
          Un sistema digital propio, adaptado al modo exacto en que opera tu empresa, que sea <strong class="text-white">un activo de tu propiedad</strong> sin rentas cautivas por usuario.
        </p>
      </div>
    </div>

    <div class="relative z-10 text-right text-lg text-slate-500 font-medium pt-8 border-t border-slate-800">
      Desliza &rarr;
    </div>
    """,

    # Slide 6 (Cierre & CTA)
    """
    <div class="relative z-10 flex items-center justify-between">
      <span class="text-xl font-bold text-emerald-400 font-mono tracking-wide">SOLUCIÓN KINETIX</span>
      <span class="text-xl text-slate-500 font-mono font-semibold">06 / 06</span>
    </div>

    <div class="relative z-10 my-auto space-y-8 text-center">
      <div class="w-24 h-24 mx-auto rounded-3xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center shadow-lg shadow-emerald-500/30">
        <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
      </div>
      <h2 class="text-5xl font-black text-white leading-tight">
        Sistematiza tu empresa en menos de 14 días
      </h2>
      <p class="text-2xl text-slate-300 leading-relaxed max-w-2xl mx-auto">
        Diseñamos y desplegamos tu WebApp, bots y centro de mando operativo sin que tengas que tocar una sola línea de código.
      </p>
      <div class="p-6 bg-emerald-500/10 border-2 border-emerald-500/40 rounded-3xl max-w-xl mx-auto">
        <span class="text-2xl font-black text-emerald-400 tracking-wide uppercase block">Comenta "SISTEMA" en este post 👇</span>
      </div>
      <p class="text-lg text-slate-400">
        Y nuestro bot te enviará un diagnóstico operativo gratuito a tus mensajes directos.
      </p>
    </div>

    <div class="relative z-10 flex items-center justify-between text-lg text-slate-500 pt-8 border-t border-slate-800 font-mono">
      <span>@kinetix.systems</span>
      <span>Software & Automatización IA</span>
    </div>
    """
]

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
base_dir = r"c:\Users\User\Desktop\Nueva carpeta\Canal de Ventas"
temp_html = os.path.join(base_dir, "_temp_slide.html")

print("Generando las 6 diapositivas en alta resolución (1080x1350)...")

for i, content in enumerate(slides_content, 1):
    full_html = html_template.replace("__CONTENT__", content)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    output_png = os.path.join(base_dir, f"slide_{i}.png")
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=1080,1350",
        f"--screenshot={output_png}",
        f"file:///{temp_html.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Slide {i} generada con exito: slide_{i}.png")

if os.path.exists(temp_html):
    os.remove(temp_html)

print("Todas las 6 diapositivas generadas con éxito.")
