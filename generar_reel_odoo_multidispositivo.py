# -*- coding: utf-8 -*-
import asyncio
import os
import subprocess
import sys
import wave
import numpy as np
import edge_tts
import imageio_ffmpeg
import base64

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\User\Desktop\Nueva carpeta\Canal de Ventas"
TEMP_DIR = os.path.join(BASE_DIR, "_reel_odoo_temp")
os.makedirs(TEMP_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "es-MX-JorgeNeural"
BG_MUSIC_PATH = os.path.join(BASE_DIR, "musica_corporativa_confianza.mp3")

def img_to_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

pos_desktop_b64 = img_to_base64(os.path.join(BASE_DIR, "screenshot_pos_light_desktop.png"))
pos_mobile_b64 = img_to_base64(os.path.join(BASE_DIR, "screenshot_pos_light_mobile.png"))
clinica_desktop_b64 = img_to_base64(os.path.join(BASE_DIR, "screenshot_clinica_light_desktop.png"))
crm_desktop_b64 = img_to_base64(os.path.join(BASE_DIR, "screenshot_crm_light_desktop.png"))

SCENES = [
    {
        "id": 1,
        "voice": "¿Qué es mejor? ¿Pagar miles de dólares al año en sistemas complicados que nadie sabe usar, o controlar tu empresa en PC, laptop y celular con un solo pago de por vida? Mira esto.",
        "tag": "01 // ¿QUÉ ES MEJOR?",
        "subtitle": '¿Qué es mejor? <span class="text-red-500 font-bold">¿Pagar miles al año</span> o controlar tu empresa con un <span class="text-emerald-600 font-bold">pago de por vida</span>?',
        "html": """
        <div class="my-auto space-y-8 text-center">
          <div class="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-emerald-50 border border-emerald-300 text-emerald-800 font-bold text-lg uppercase tracking-wider">
            <span>⚡</span> Software 100% Práctico e Intuitivo
          </div>
          <h1 class="text-6xl font-black text-slate-900 leading-[1.15]">
            Controla tu empresa <span class="text-emerald-600 underline decoration-emerald-300">sin pagar miles de dólares</span>
          </h1>
          <p class="text-2xl text-slate-600 font-medium max-w-xl mx-auto">
            Tan sencillo y amigable que cualquier empleado aprende a cobrar y registrar datos en sus primeros 5 minutos.
          </p>
          <div class="w-full h-[360px] rounded-3xl bg-white border border-slate-200 shadow-xl overflow-hidden p-3">
            <img src='""" + pos_desktop_b64 + """' class="w-full h-full object-cover object-top rounded-2xl" alt="POS Light">
          </div>
        </div>
        """
    },
    {
        "id": 2,
        "voice": "Kinetix funciona en cualquier dispositivo. Tu computadora de mostrador, tu laptop o tu teléfono celular.",
        "tag": "02 // MULTI-DISPOSITIVO",
        "subtitle": 'Funciona en cualquier dispositivo: <span class="text-cyan-600 font-bold">PC, Laptop o Celular</span>.',
        "html": """
        <div class="my-auto space-y-8 text-center">
          <div class="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-cyan-50 border border-cyan-300 text-cyan-800 font-bold text-lg uppercase tracking-wider">
            <span>📱</span> Adaptabilidad Total
          </div>
          <h2 class="text-6xl font-black text-slate-900 leading-[1.15]">
            En la oficina, en tu mostrador o <span class="text-cyan-600">desde tu celular</span>
          </h2>
          <div class="grid grid-cols-3 gap-4 pt-2">
            <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-md">
              <div class="text-5xl mb-2">💻</div>
              <div class="font-bold text-xl text-slate-900">PC & Laptop</div>
            </div>
            <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-md">
              <div class="text-5xl mb-2">📱</div>
              <div class="font-bold text-xl text-slate-900">Smartphone</div>
            </div>
            <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-md">
              <div class="text-5xl mb-2">📋</div>
              <div class="font-bold text-xl text-slate-900">Tablet</div>
            </div>
          </div>
          <div class="w-full h-[320px] rounded-3xl bg-white border border-slate-200 shadow-xl overflow-hidden p-2">
            <img src='""" + clinica_desktop_b64 + """' class="w-full h-full object-cover object-top rounded-2xl" alt="Clinica Light">
          </div>
        </div>
        """
    },
    {
        "id": 3,
        "voice": "Diseñado para todo tipo de negocios. Grandes, medianas y pequeñas empresas: tiendas, consultorios médicos, agencias y talleres.",
        "tag": "03 // PARA TODAS LAS EMPRESAS",
        "subtitle": 'Para <span class="text-purple-600 font-bold">grandes, medianas y pequeñas</span> empresas.',
        "html": """
        <div class="my-auto space-y-7">
          <div class="text-center">
            <div class="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-purple-50 border border-purple-300 text-purple-800 font-bold text-lg uppercase tracking-wider">
              <span>🏢</span> Diseñado Para Todo Negocio
            </div>
            <h2 class="text-6xl font-black text-slate-900 leading-tight mt-4">
              La suite que se adapta a tu flujo
            </h2>
          </div>
          <div class="space-y-4 pt-2">
            <div class="p-5 rounded-2xl bg-white border border-slate-200 flex items-center justify-between shadow-sm">
              <span class="text-2xl font-bold text-slate-900">🛒 Punto de Venta & Inventarios</span>
              <span class="px-4 py-1.5 rounded-xl bg-emerald-100 text-emerald-800 font-bold text-sm">Retail</span>
            </div>
            <div class="p-5 rounded-2xl bg-white border border-slate-200 flex items-center justify-between shadow-sm">
              <span class="text-2xl font-bold text-slate-900">🩺 Citas Médicas & WhatsApp</span>
              <span class="px-4 py-1.5 rounded-xl bg-cyan-100 text-cyan-800 font-bold text-sm">Salud</span>
            </div>
            <div class="p-5 rounded-2xl bg-white border border-slate-200 flex items-center justify-between shadow-sm">
              <span class="text-2xl font-bold text-slate-900">💼 CRM & Cotizaciones en PDF</span>
              <span class="px-4 py-1.5 rounded-xl bg-purple-100 text-purple-800 font-bold text-sm">Servicios</span>
            </div>
          </div>
          <div class="w-full h-[260px] rounded-3xl bg-white border border-slate-200 shadow-xl overflow-hidden p-2">
            <img src='""" + crm_desktop_b64 + """' class="w-full h-full object-cover object-top rounded-2xl" alt="CRM Light">
          </div>
        </div>
        """
    },
    {
        "id": 4,
        "voice": "Olvídate de pagar suscripciones mensuales de cien dólares. Llévatelo hoy por solo ochenta y nueve dólares, pago único de por vida.",
        "tag": "04 // OFERTA $89 USD",
        "subtitle": 'Solo <span class="text-emerald-600 font-black">$89 USD</span> pago único vitalicio para 4 usuarios.',
        "html": """
        <div class="my-auto space-y-8 text-center">
          <div class="w-24 h-24 mx-auto rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center text-5xl font-black border-4 border-emerald-400 shadow-xl">
            $
          </div>
          <h2 class="text-6xl font-black text-slate-900 leading-tight">
            Ahorra más de <span class="text-emerald-600">$1,400 USD</span> al año
          </h2>
          <div class="grid grid-cols-2 gap-6 pt-2">
            <div class="p-7 rounded-3xl bg-white border border-slate-200 shadow-md">
              <div class="text-4xl font-black text-emerald-600">$89 USD</div>
              <p class="text-slate-600 font-medium text-lg mt-2">Pago único vitalicio</p>
            </div>
            <div class="p-7 rounded-3xl bg-white border border-slate-200 shadow-md">
              <div class="text-4xl font-black text-slate-900">4 Usuarios</div>
              <p class="text-slate-600 font-medium text-lg mt-2">Sin costos por usuario</p>
            </div>
          </div>
          <p class="text-xl text-slate-500 font-medium">
            🛡️ Incluye 7 asistencias técnicas gratuitas de soporte durante tu primer año.
          </p>
        </div>
        """
    },
    {
        "id": 5,
        "voice": "Comenta la palabra SISTEMA en este video y te enviamos el enlace de inmediato a tus mensajes privados para que pruebes las demos gratis hoy mismo.",
        "tag": "05 // DEMO GRATIS",
        "subtitle": 'Comenta <span class="text-emerald-600 font-black text-4xl">SISTEMA</span> y te enviamos la demo al DM.',
        "html": """
        <div class="my-auto space-y-8 text-center">
          <div class="w-28 h-28 mx-auto rounded-full bg-slate-900 text-white flex items-center justify-center text-6xl shadow-2xl">
            🎙️
          </div>
          <h2 class="text-6xl font-black text-slate-900 leading-tight">
            Pruébalo gratis en tu celular ahora
          </h2>
          <div class="p-8 bg-slate-900 text-white rounded-3xl max-w-xl mx-auto shadow-2xl space-y-2 border border-slate-700">
            <span class="text-3xl font-black text-amber-300 tracking-wider uppercase block">Comenta "SISTEMA" abajo 👇</span>
            <span class="text-slate-300 text-base font-normal block">Te enviamos el enlace directo para probar la demo en tu celular o PC</span>
          </div>
          <p class="text-lg font-mono text-slate-500">
            Kinetix Systems · https://tinyurl.com/kinetixsistemasPOS
          </p>
        </div>
        """
    }
]

html_shell = """<!DOCTYPE html>
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
      background-color: #f8fafc;
      color: #0f172a;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 90px 80px;
      position: relative;
    }
  </style>
</head>
<body>
  <!-- Header Branding Light -->
  <div class="relative z-10 flex items-center justify-between border-b border-slate-200 pb-6">
    <div class="flex items-center gap-3">
      <div class="w-12 h-12 rounded-2xl bg-emerald-500 flex items-center justify-center font-bold text-slate-950 font-mono text-xl shadow-md">K</div>
      <div>
        <div class="font-extrabold text-slate-900 text-xl tracking-tight">KINETIX SYSTEMS</div>
        <div class="text-xs font-mono uppercase tracking-widest text-slate-500 font-bold">SOFTWARE PROFESIONAL</div>
      </div>
    </div>
    <span class="px-4 py-2 rounded-full bg-emerald-50 border border-emerald-300 text-emerald-800 font-mono text-sm font-bold shadow-sm">
      __TAG__
    </span>
  </div>

  <!-- Body Content -->
  <div class="relative z-10 flex-1 flex flex-col justify-center py-6">
    __CONTENT__
  </div>

  <!-- Footer Subtitle Overlay Box -->
  <div class="relative z-10 border-t border-slate-200 pt-6">
    <div class="bg-white/95 backdrop-blur-md rounded-2xl p-6 border border-slate-200 shadow-xl text-center">
      <p class="text-3xl font-extrabold text-slate-800 leading-snug">
        __SUBTITLE__
      </p>
    </div>
  </div>
</body>
</html>
"""

async def generate_voiceovers():
    print("Generando voces de Jorge Neural con edge-tts...")
    for s in SCENES:
        mp3_path = os.path.join(TEMP_DIR, f"voice_{s['id']}.mp3")
        wav_path = os.path.join(TEMP_DIR, f"voice_{s['id']}.wav")
        communicate = edge_tts.Communicate(s["voice"], VOICE, rate="+6%")
        await communicate.save(mp3_path)
        subprocess.run([
            FFMPEG_EXE, "-y", "-i", mp3_path,
            "-ar", "44100", "-ac", "2",
            wav_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        s["wav_path"] = wav_path
        print(f"Voz {s['id']} lista")

def render_scene_images():
    print("Renderizando capturas 1080x1920 en Modo Claro con Chrome...")
    temp_html = os.path.join(TEMP_DIR, "_temp_scene.html")
    for s in SCENES:
        html = (
            html_shell
            .replace("__TAG__", s["tag"])
            .replace("__CONTENT__", s["html"])
            .replace("__SUBTITLE__", s["subtitle"])
        )
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html)

        png_path = os.path.join(TEMP_DIR, f"scene_{s['id']}.png")
        cmd = [
            CHROME_PATH,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1080,1920",
            f"--screenshot={png_path}",
            f"file:///{temp_html.replace(os.sep, '/')}"
        ]
        subprocess.run(cmd, check=True)
        s["png_path"] = png_path
        print(f"Imagen {s['id']} renderizada")

    if os.path.exists(temp_html):
        os.remove(temp_html)

def build_voice_segments():
    print("Ensamblando clips de video con zoom dinámico...")
    for idx, s in enumerate(SCENES):
        with wave.open(s["wav_path"], "rb") as w:
            sr = w.getframerate()
            n_frames = w.getnframes()
            data = w.readframes(n_frames)
            vo = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0

        # Pequeño padding de pausa al final de la frase
        pad_len = int(0.35 * sr)
        vo_padded = np.pad(vo.reshape(-1, 2), ((0, pad_len), (0, 0)))
        n_samples = len(vo_padded)
        dur = n_samples / float(sr)

        scene_wav = os.path.join(TEMP_DIR, f"scene_audio_{s['id']}.wav")
        pcm = (np.clip(vo_padded * 1.15, -0.98, 0.98) * 32767.0).astype(np.int16)
        with wave.open(scene_wav, "wb") as out_w:
            out_w.setnchannels(2)
            out_w.setsampwidth(2)
            out_w.setframerate(sr)
            out_w.writeframes(pcm.tobytes())

        frames_count = int(dur * 30) + 2
        seg_mp4 = os.path.join(TEMP_DIR, f"seg_{s['id']}.mp4")

        # Zoompan suave alternado
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
        s["dur"] = dur
        print(f"Clip {s['id']} generado ({dur:.2f}s)")

def concat_and_mix_bg_music():
    print("Concatenando escenas y mezclando música corporativa de alta confianza...")
    concat_txt = os.path.join(TEMP_DIR, "concat_list.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for s in SCENES:
            p = s["seg_mp4"].replace("\\", "/")
            f.write(f"file '{p}'\n")

    temp_concat_video = os.path.join(TEMP_DIR, "temp_concat.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c:v", "copy",
        "-c:a", "copy",
        temp_concat_video
    ], check=True)

    # Duración total del video
    total_dur = sum(s["dur"] for s in SCENES)
    fade_out_start = max(0.5, total_dur - 2.5)

    final_output = os.path.join(BASE_DIR, "reel_odoo_multidispositivo.mp4")

    # Mezclamos la voz del video (pista 0) con la música de fondo (pista 1)
    # Volumen de música al 14% para que la voz se entienda con total nitidez, con fade in al inicio y fade out al final
    filter_complex = (
        f"[1:a]volume=0.14,afade=t=in:ss=0:d=1.2,afade=t=out:st={fade_out_start:.2f}:d=2.5[bg];"
        f"[0:a]volume=1.15[vo];"
        f"[vo][bg]amix=inputs=2:duration=first:dropout_transition=2[aout]"
    )

    cmd = [
        FFMPEG_EXE, "-y",
        "-i", temp_concat_video,
        "-i", BG_MUSIC_PATH,
        "-filter_complex", filter_complex,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        final_output
    ]

    subprocess.run(cmd, check=True)
    print(f"REEL ODOO MULTIDISPOSITIVO CON MÚSICA DE FONDO FINALIZADO: {final_output}")

if __name__ == "__main__":
    asyncio.run(generate_voiceovers())
    render_scene_images()
    build_voice_segments()
    concat_and_mix_bg_music()
