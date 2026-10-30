import asyncio
import os
import subprocess
import wave
import numpy as np
import edge_tts
import imageio_ffmpeg

BASE_DIR = r"c:\Users\User\Desktop\Nueva carpeta\Canal de Ventas"
TEMP_DIR = os.path.join(BASE_DIR, "_reel_temp")
os.makedirs(TEMP_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "es-MX-JorgeNeural"

SCENES = [
    {
        "id": 1,
        "voice": "Si tu empresa sigue operando con hojas de cálculo compartidas, estás perdiendo miles de dólares cada mes.",
        "tag": "01 // ALERTA OPERATIVA",
        "subtitle": 'Si tu empresa sigue operando con <span class="text-emerald-400">hojas de cálculo</span>, estás perdiendo miles de dólares.',
        "html": """
        <div class="my-auto space-y-8">
          <div class="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-red-500/15 border border-red-500/40 text-red-400 font-bold text-lg uppercase tracking-wider">
            <span class="w-3 h-3 rounded-full bg-red-500"></span> Fuga Operativa Detectada
          </div>
          <h1 class="text-6xl font-black text-white leading-[1.12]">
            El error silencioso que drena <span class="text-red-400">$2,850 USD/mes</span> de tu negocio
          </h1>
          <!-- Mockup Excel Roto -->
          <div class="rounded-3xl bg-slate-900/95 border-2 border-red-500/40 p-7 shadow-2xl space-y-5">
            <div class="flex items-center justify-between border-b border-slate-800 pb-4">
              <div class="flex items-center gap-2">
                <div class="w-3.5 h-3.5 rounded-full bg-red-500"></div>
                <div class="w-3.5 h-3.5 rounded-full bg-amber-500"></div>
                <div class="w-3.5 h-3.5 rounded-full bg-emerald-500"></div>
                <span class="ml-3 font-mono text-base text-slate-400">Control_Clientes_FINAL_v4.xlsx</span>
              </div>
              <span class="text-xs font-mono bg-red-500/20 text-red-300 px-3 py-1 rounded-md">SIN SINCRONIZAR</span>
            </div>
            <div class="space-y-3 font-mono text-lg">
              <div class="grid grid-cols-3 bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-slate-400">
                <span>Cliente #104</span>
                <span class="text-red-400 font-bold">#¡REF! ERROR</span>
                <span class="text-amber-400">Pendiente</span>
              </div>
              <div class="grid grid-cols-3 bg-slate-950 p-3.5 rounded-xl border border-red-500/30 text-slate-300">
                <span>Clínica Sur</span>
                <span class="text-red-400 font-bold">DATO BORRADO</span>
                <span class="text-red-400">-$1,400 USD</span>
              </div>
              <div class="grid grid-cols-3 bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-slate-400">
                <span>Lead WhatsApp</span>
                <span class="text-amber-400">Sin respuesta 6h</span>
                <span class="text-red-400">Perdido</span>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 2,
        "voice": "Una celda borrada por error, una fórmula rota o un prospecto esperando horas por una cotización le regala tus clientes a la competencia.",
        "tag": "02 // EL COSTO MANUAL",
        "subtitle": 'Una celda borrada o un prospecto esperando horas <span class="text-red-400">le regala tus ventas a la competencia.</span>',
        "html": """
        <div class="my-auto space-y-7">
          <h2 class="text-5xl font-black text-white leading-tight">
            ¿Qué pasa cuando tu operación depende de <span class="text-amber-400">copiar y pegar</span>?
          </h2>
          <div class="space-y-5">
            <div class="p-6 rounded-3xl bg-slate-900/90 border border-slate-800 flex items-center gap-6">
              <div class="w-16 h-16 rounded-2xl bg-red-500/15 border border-red-500/30 flex items-center justify-center text-red-400 font-black text-3xl shrink-0">80%</div>
              <div>
                <h3 class="text-2xl font-bold text-white">Menos cierres de venta</h3>
                <p class="text-lg text-slate-400">Cuando tardas más de 15 minutos en enviar una cotización o responder en WhatsApp.</p>
              </div>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900/90 border border-slate-800 flex items-center gap-6">
              <div class="w-16 h-16 rounded-2xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center text-amber-400 font-black text-3xl shrink-0">60%</div>
              <div>
                <h3 class="text-2xl font-bold text-white">De tu nómina desperdiciada</h3>
                <p class="text-lg text-slate-400">Pagando sueldos para pasar datos de WhatsApp a Excel en vez de generar ingresos.</p>
              </div>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900/90 border border-slate-800 flex items-center gap-6">
              <div class="w-16 h-16 rounded-2xl bg-cyan-500/15 border border-cyan-500/30 flex items-center justify-center text-cyan-400 font-black text-3xl shrink-0">24/7</div>
              <div>
                <h3 class="text-2xl font-bold text-white">Dependencia del dueño</h3>
                <p class="text-lg text-slate-400">Si tú no supervisas cada paso, la operación se frena o comete errores costosos.</p>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 3,
        "voice": "Mira cómo transformamos una clínica médica que gastaba cuatro horas diarias de papeleo en un sistema propio de un solo clic.",
        "tag": "03 // CASO DE ESTUDIO REAL",
        "subtitle": 'De 4 horas diarias de papeleo manual a <span class="text-emerald-400">un sistema propio de 1 solo clic.</span>',
        "html": """
        <div class="my-auto space-y-8">
          <div class="inline-flex items-center gap-2 px-5 py-2 rounded-full bg-emerald-500/15 border border-emerald-500/40 text-emerald-400 font-bold text-lg uppercase">
            Caso Real · Sector Clínico & Salud
          </div>
          <h2 class="text-5xl font-black text-white leading-tight">
            De <span class="line-through text-slate-500">4 Horas Manuales</span> a <span class="text-emerald-400">300 Milisegundos</span>
          </h2>
          <div class="grid grid-cols-1 gap-6">
            <div class="p-7 rounded-3xl bg-red-950/25 border border-red-500/30 space-y-2">
              <span class="text-sm font-mono uppercase text-red-400 font-bold">ANTES (OPERACIÓN TRADICIONAL)</span>
              <p class="text-2xl font-bold text-white">Agendas sueltas, pacientes olvidados y expedientes en carpetas</p>
              <p class="text-lg text-slate-400">40% de ausentismo en consultas y horas perdidas confirmando uno por uno.</p>
            </div>
            <div class="p-7 rounded-3xl bg-emerald-950/30 border-2 border-emerald-500/50 space-y-2 shadow-2xl">
              <span class="text-sm font-mono uppercase text-emerald-400 font-bold">AHORA (ARQUITECTURA KINETIX.OS)</span>
              <p class="text-2xl font-bold text-white">WebApp Propia + Bot de Agenda & Expedientes en 1 Clic</p>
              <p class="text-lg text-emerald-200">Cero rentas mensuales por usuario. 100% adaptado al flujo médico real.</p>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 4,
        "voice": "Diseñamos un centro de mando a medida: el paciente agenda, el sistema valida disponibilidad y envía confirmación automática por WhatsApp.",
        "tag": "04 // DEMO EN VIVO: PEDIATRÍA & CLÍNICA",
        "subtitle": 'El cliente agenda, el sistema valida horarios y <span class="text-cyan-400">confirma en automático por WhatsApp.</span>',
        "html": """
        <div class="my-auto space-y-7">
          <div class="rounded-3xl bg-slate-900 border-2 border-emerald-500/40 p-7 shadow-2xl space-y-6">
            <div class="flex items-center justify-between border-b border-slate-800 pb-4">
              <div>
                <span class="text-xs font-mono text-emerald-400 uppercase font-bold">KINETIX CLINICAL OS · v2.4</span>
                <h3 class="text-2xl font-black text-white">Centro de Mando & Agenda Autónoma</h3>
              </div>
              <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-sm font-bold">● EN LÍNEA 24/7</span>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div class="p-5 rounded-2xl bg-slate-950 border border-slate-800">
                <span class="text-sm text-slate-400">Citas Confirmadas Hoy</span>
                <p class="text-4xl font-black text-emerald-400 mt-1">28 / 28</p>
                <span class="text-xs text-emerald-300">100% vía Bot WhatsApp</span>
              </div>
              <div class="p-5 rounded-2xl bg-slate-950 border border-slate-800">
                <span class="text-sm text-slate-400">Tiempo Admin Ahorrado</span>
                <p class="text-4xl font-black text-cyan-400 mt-1">22.5 hrs</p>
                <span class="text-xs text-cyan-300">Esta semana</span>
              </div>
            </div>
            <div class="space-y-3 text-base">
              <div class="p-4 rounded-2xl bg-slate-950 border border-emerald-500/30 flex items-center justify-between">
                <div>
                  <p class="font-bold text-white">Expediente #4092 · Consulta Pediátrica</p>
                  <p class="text-sm text-slate-400">Recordatorio WhatsApp enviado + Historial listo</p>
                </div>
                <span class="px-3 py-1 rounded-lg bg-emerald-500 text-slate-950 font-black text-xs">CONFIRMADO</span>
              </div>
              <div class="p-4 rounded-2xl bg-slate-950 border border-cyan-500/30 flex items-center justify-between">
                <div>
                  <p class="font-bold text-white">Expediente #4093 · Seguimiento Clínico</p>
                  <p class="text-sm text-slate-400">Receta digital y cobro automático procesado</p>
                </div>
                <span class="px-3 py-1 rounded-lg bg-cyan-400 text-slate-950 font-black text-xs">PAGADO</span>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 5,
        "voice": "Al concluir la consulta, el expediente se blinda con acceso por roles y la factura se emite sola, con cero errores humanos.",
        "tag": "05 // FLUJO 100% AUTÓNOMO",
        "subtitle": 'Expedientes blindados por roles y <span class="text-emerald-400">facturación emitida sola</span> con cero errores.',
        "html": """
        <div class="my-auto space-y-6">
          <h2 class="text-5xl font-black text-white leading-tight">
            Tu empresa operando como un <span class="text-emerald-400">reloj suizo</span>
          </h2>
          <div class="space-y-4">
            <div class="p-6 rounded-3xl bg-slate-900/95 border border-emerald-500/40 flex items-center justify-between">
              <div class="flex items-center gap-5">
                <div class="w-12 h-12 rounded-2xl bg-emerald-500 text-slate-950 font-black text-xl flex items-center justify-center">1</div>
                <div>
                  <h4 class="text-2xl font-bold text-white">Captura & Calificación IA</h4>
                  <p class="text-base text-slate-400">Atiende prospectos en WhatsApp y Web en 3 segundos</p>
                </div>
              </div>
              <span class="text-emerald-400 font-mono font-bold">0.3s</span>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900/95 border border-cyan-500/40 flex items-center justify-between">
              <div class="flex items-center gap-5">
                <div class="w-12 h-12 rounded-2xl bg-cyan-400 text-slate-950 font-black text-xl flex items-center justify-center">2</div>
                <div>
                  <h4 class="text-2xl font-bold text-white">Gestión & Roles Privados</h4>
                  <p class="text-base text-slate-400">Cada miembro del equipo ve solo lo que le corresponde</p>
                </div>
              </div>
              <span class="text-cyan-400 font-mono font-bold">SSL</span>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900/95 border border-teal-500/40 flex items-center justify-between">
              <div class="flex items-center gap-5">
                <div class="w-12 h-12 rounded-2xl bg-teal-400 text-slate-950 font-black text-xl flex items-center justify-center">3</div>
                <div>
                  <h4 class="text-2xl font-bold text-white">Cobro, Contrato y Reporte</h4>
                  <p class="text-base text-slate-400">Dashboard financiero actualizado en tiempo real</p>
                </div>
              </div>
              <span class="text-teal-400 font-mono font-bold">AUTO</span>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 6,
        "voice": "No importa si tienes una clínica, una agencia, una inmobiliaria o una distribuidora: construimos tu software propio en menos de catorce días.",
        "tag": "06 // SIN LÍMITES DE INDUSTRIA",
        "subtitle": 'Construimos el software a medida de tu negocio <span class="text-emerald-400">en menos de 14 días.</span>',
        "html": """
        <div class="my-auto space-y-7">
          <h2 class="text-5xl font-black text-white leading-tight">
            Diseñado a la medida exacta de <span class="text-cyan-400">tu modelo de negocio</span>
          </h2>
          <div class="grid grid-cols-2 gap-5">
            <div class="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-2">
              <span class="text-3xl">🏥</span>
              <h3 class="text-2xl font-bold text-white">Clínicas & Salud</h3>
              <p class="text-base text-slate-400">Expedientes clínicos, agendas y recordatorios por WhatsApp.</p>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-2">
              <span class="text-3xl">🏢</span>
              <h3 class="text-2xl font-bold text-white">Inmobiliarias</h3>
              <p class="text-base text-slate-400">Calificación de leads, portales de clientes y contratos.</p>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-2">
              <span class="text-3xl">📦</span>
              <h3 class="text-2xl font-bold text-white">Comercio & ERP</h3>
              <p class="text-base text-slate-400">Control de inventario, cotizadores y cobranza automática.</p>
            </div>
            <div class="p-6 rounded-3xl bg-slate-900 border border-slate-800 space-y-2">
              <span class="text-3xl">⚡</span>
              <h3 class="text-2xl font-bold text-white">Agencias & B2B</h3>
              <p class="text-base text-slate-400">Onboarding en 1 clic, dashboards y seguimiento autónomo.</p>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 7,
        "voice": "Comenta la palabra SISTEMA aquí abajo y te enviaremos un diagnóstico operativo gratuito directamente a tus mensajes privados.",
        "tag": "07 // ACCESO INMEDIATO",
        "subtitle": 'Comenta la palabra <span class="text-emerald-400 font-black">"SISTEMA"</span> y recibe tu diagnóstico gratis al DM.',
        "html": """
        <div class="my-auto text-center space-y-8">
          <div class="w-28 h-28 mx-auto rounded-3xl bg-emerald-500/20 border-2 border-emerald-400 flex items-center justify-center shadow-2xl">
            <span class="text-6xl">⚡</span>
          </div>
          <h2 class="text-6xl font-black text-white leading-tight">
            ¿Listo para automatizar tu empresa?
          </h2>
          <p class="text-2xl text-slate-300 leading-relaxed">
            Deja de perder horas en hojas de cálculo. Recibe hoy la arquitectura digital para tu negocio.
          </p>
          <div class="p-8 rounded-3xl bg-gradient-to-r from-emerald-400 to-cyan-400 text-slate-950 shadow-2xl">
            <span class="text-xs font-mono uppercase tracking-widest font-black block mb-1">ESCRIBE EN LOS COMENTARIOS:</span>
            <span class="text-5xl font-black tracking-wider">💬 "SISTEMA"</span>
          </div>
          <p class="text-xl text-emerald-300 font-semibold">
            Nuestro bot te enviará el acceso directo a tu bandeja de mensajes (DM) en 3 segundos 👇
          </p>
        </div>
        """
    }
]

HTML_SHELL = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1080px;
      height: 1920px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #060a12;
      color: #f1f5f9;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 110px 76px 140px 76px;
      position: relative;
    }
    .bg-glow {
      position: absolute;
      inset: 0;
      background:
        radial-gradient(circle at 85% 15%, rgba(16, 185, 129, 0.22) 0%, transparent 50%),
        radial-gradient(circle at 15% 85%, rgba(56, 189, 248, 0.16) 0%, transparent 50%);
      pointer-events: none;
    }
    .grid-overlay {
      position: absolute;
      inset: 0;
      background-image: radial-gradient(rgba(255,255,255,0.06) 1px, transparent 1px);
      background-size: 36px 36px;
      pointer-events: none;
    }
  </style>
</head>
<body>
  <div class="bg-glow"></div>
  <div class="grid-overlay"></div>

  <!-- Top Bar -->
  <div class="relative z-10 flex items-center justify-between border-b border-slate-800/90 pb-6">
    <div class="flex items-center gap-4">
      <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 border border-emerald-400/50 flex items-center justify-center font-mono font-black text-emerald-400 text-2xl">K</div>
      <div>
        <span class="font-extrabold text-white text-2xl tracking-tight block">@kinetix.ops</span>
        <span class="text-xs font-mono text-emerald-400 uppercase tracking-widest">Software & Automatización IA</span>
      </div>
    </div>
    <span class="px-4 py-2 rounded-xl bg-slate-900 border border-slate-700 font-mono text-sm text-slate-300 font-bold">__TAG__</span>
  </div>

  <!-- Main Content -->
  <div class="relative z-10 flex-1 flex flex-col justify-center py-8">
    __BODY__
  </div>

  <!-- Kinetic Subtitle Box -->
  <div class="relative z-10 space-y-5">
    <div class="p-7 rounded-3xl bg-slate-950/90 border-2 border-slate-800 shadow-2xl text-center">
      <p class="text-3xl font-extrabold text-white leading-snug">
        “__SUBTITLE__”
      </p>
    </div>
    <!-- Progress Bar -->
    <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden">
      <div class="h-full bg-gradient-to-r from-emerald-400 to-cyan-400" style="width: __PROGRESS__%;"></div>
    </div>
  </div>
</body>
</html>
"""

async def generate_voiceovers():
    for s in SCENES:
        mp3_path = os.path.join(TEMP_DIR, f"vo_{s['id']}.mp3")
        wav_path = os.path.join(TEMP_DIR, f"vo_{s['id']}.wav")
        communicate = edge_tts.Communicate(s["voice"], VOICE, rate="+8%", pitch="-2Hz")
        await communicate.save(mp3_path)
        # Convert to 44100Hz stereo WAV using ffmpeg
        subprocess.run([
            FFMPEG_EXE, "-y", "-i", mp3_path,
            "-ar", "44100", "-ac", "2", wav_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with wave.open(wav_path, "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            s["duration"] = frames / float(rate) + 0.35  # Slight breathing room
            s["wav_path"] = wav_path
        print(f"Voz escena {s['id']} lista ({s['duration']:.2f}s)")

def render_scene_images():
    total = len(SCENES)
    for idx, s in enumerate(SCENES, 1):
        progress = int((idx / total) * 100)
        html = (HTML_SHELL
                .replace("__TAG__", s["tag"])
                .replace("__BODY__", s["html"])
                .replace("__SUBTITLE__", s["subtitle"])
                .replace("__PROGRESS__", str(progress)))
        html_file = os.path.join(TEMP_DIR, f"scene_{s['id']}.html")
        png_file = os.path.join(TEMP_DIR, f"scene_{s['id']}.png")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)
        subprocess.run([
            CHROME_PATH,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1080,1920",
            f"--screenshot={png_file}",
            f"file:///{html_file.replace(os.sep, '/')}"
        ], check=True)
        s["png_path"] = png_file
        print(f"Imagen escena {s['id']} renderizada (1080x1920)")

def build_master_audio_and_clips():
    sr = 44100
    master_chunks = []

    for idx, s in enumerate(SCENES):
        with wave.open(s["wav_path"], "rb") as wf:
            raw = wf.readframes(wf.getnframes())
            vo = np.frombuffer(raw, dtype=np.int16).astype(np.float32).reshape(-1, 2) / 32768.0

        pad_samples = int(0.35 * sr)
        vo_padded = np.vstack([vo, np.zeros((pad_samples, 2), dtype=np.float32)])
        n_samples = len(vo_padded)
        t = np.arange(n_samples, dtype=np.float32) / sr

        # Dark futuristic ambient drone (A1 = 55Hz, E2 = 82.4Hz, A2 = 110Hz) + subtle pulse
        pulse = 0.5 + 0.5 * np.sin(2 * np.pi * 2.0 * t)
        bass = (
            0.45 * np.sin(2 * np.pi * 55.0 * t) +
            0.30 * np.sin(2 * np.pi * 82.41 * t) +
            0.20 * np.sin(2 * np.pi * 110.0 * t) * pulse
        )
        # Transition soft sub-drop whoosh at the first 0.25s of each scene
        whoosh_env = np.exp(-t / 0.08)
        freq_sweep = 160.0 * np.exp(-t / 0.12) + 45.0
        sfx = 0.35 * np.sin(2 * np.pi * freq_sweep * t) * whoosh_env

        bg = (bass * 0.075 + sfx * 0.18)[:, None]
        mixed = np.clip(vo_padded * 1.12 + bg, -0.98, 0.98)

        scene_wav = os.path.join(TEMP_DIR, f"mixed_{s['id']}.wav")
        pcm = (mixed * 32767.0).astype(np.int16)
        with wave.open(scene_wav, "wb") as out_w:
            out_w.setnchannels(2)
            out_w.setsampwidth(2)
            out_w.setframerate(sr)
            out_w.writeframes(pcm.tobytes())

        # Create 30fps video segment with subtle smooth zoom effect
        dur = n_samples / float(sr)
        frames_count = int(dur * 30) + 2
        seg_mp4 = os.path.join(TEMP_DIR, f"seg_{s['id']}.mp4")

        # Alternate zoom-in and zoom-out slightly for dynamic feel
        if idx % 2 == 0:
            zp = f"zoompan=z='min(zoom+0.0004,1.05)':d={frames_count}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"
        else:
            zp = f"zoompan=z='if(eq(on,1),1.04,max(1.0,zoom-0.0004))':d={frames_count}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30"

        subprocess.run([
            FFMPEG_EXE, "-y",
            "-loop", "1", "-i", s["png_path"],
            "-i", scene_wav,
            "-vf", zp,
            "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-shortest",
            seg_mp4
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        s["seg_mp4"] = seg_mp4
        print(f"Segmento de video {s['id']} codificado ({dur:.2f}s)")

def concat_all_segments():
    concat_txt = os.path.join(TEMP_DIR, "concat_list.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for s in SCENES:
            p = s["seg_mp4"].replace("\\", "/")
            f.write(f"file '{p}'\n")

    final_output = os.path.join(BASE_DIR, "reel_1_kinetix.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        final_output
    ], check=True)
    print(f"REEL FINAL GENERADO CON ÉXITO: {final_output}")

if __name__ == "__main__":
    asyncio.run(generate_voiceovers())
    render_scene_images()
    build_master_audio_and_clips()
    concat_all_segments()
