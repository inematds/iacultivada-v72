#!/usr/bin/env python3
"""Aponta o vídeo de conteudo/en|es/curso.json para a versão do idioma (o tradutor mantém o mp4/vtt do PT)."""
import json
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
REL = "https://github.com/inematds/iacultivada/releases/download/video-v2.0.0/"
DUR = {"en": "9 min 54 s", "es": "8 min 59 s"}
for lang in ("en", "es"):
    f = raiz / "conteudo" / lang / "curso.json"
    if not f.exists():
        continue
    c = json.loads(f.read_text())
    v = c["videos"]["iacultivada"]
    v["mp4"] = f"{REL}iacultivada-{lang}.mp4"
    v["vtt"] = f"assets/vtt/iacultivada-{lang}.vtt"
    v["duracao"] = DUR[lang]
    v["pagina"] = f"https://inematds.github.io/iacultivada/videos/{lang}/"
    f.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n")
    print(f"{lang}: vídeo → {v['mp4']}")
