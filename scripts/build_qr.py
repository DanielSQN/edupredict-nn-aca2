"""Genera los códigos QR del póster a partir de los enlaces de ``src/project_info.py``.

Uso::

    python scripts/build_qr.py

Crea ``docs/poster/qr_app.png``, ``qr_video.png`` y ``qr_repositorio.png``, que es
donde ``build_poster.py`` los busca. Un enlace vacío se omite y el póster deja el
espacio reservado: nada se inventa. Después de generarlos hay que volver a correr
``python scripts/build_poster.py`` para que entren en el HTML.
"""

from __future__ import annotations

import sys
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src import project_info as info  # noqa: E402

POSTER_DIR = ROOT / "docs" / "poster"
AZUL_CUN = "#0B2545"


def build() -> list[Path]:
    enlaces = {
        "app": info.ENLACE_APP,
        "video": info.ENLACE_VIDEO,
        "repositorio": info.ENLACE_REPO,
    }
    generados = []
    for nombre, url in enlaces.items():
        destino = POSTER_DIR / f"qr_{nombre}.png"
        if not url:
            print(f"  qr_{nombre}.png       omitido: falta la URL en src/project_info.py")
            continue
        qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=12, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        qr.make_image(fill_color=AZUL_CUN, back_color="white").save(destino)
        print(f"  qr_{nombre}.png       {url}")
        generados.append(destino)
    return generados


if __name__ == "__main__":
    build()
