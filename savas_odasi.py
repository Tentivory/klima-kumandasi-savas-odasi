#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klima kumandası savaş odası. Gerçekten çalışır. Evi soğutmaz."""

from __future__ import annotations

import argparse
import base64
import hashlib
from datetime import datetime


def gerilim(oda: float, anne: float, baba: float, pil: int) -> float:
    return abs(anne - baba) + max(0.0, oda - 27.0) + (100 - pil) / 10.0


def hukum(oda: float, anne: float, baba: float, kisi: str, pil: int) -> str:
    g = gerilim(oda, anne, baba, pil)
    if pil < 15:
        karar = "Pil bitmiş. Savaş ertelendi. Suçlu: evren, yedek: kumanda kapağı."
    elif abs(anne - baba) >= 4:
        karar = (
            f"Anne {anne:.0f}, baba {baba:.0f}. Fark anayasal kriz sayılır. "
            f"Kumanda geçici olarak '{kisi}' adına kayyuma bırakıldı."
        )
    elif oda >= 28:
        karar = "Oda tropikal cumhuriyet ilan etti. Pencere açılsın denildi, kimse kalkmadı."
    elif oda <= 19:
        karar = "Oda kutup bölgesi. Battaniye muhalefeti güvenoyu aldı."
    else:
        karar = "Ortam ılımlı. Bu yüzden yine de tartışılacak, çünkü gelenek."

    if g >= 12:
        ek = "Gerilim yüksek. Tutanak üç nüsha. Bir nüsha koltuğun altında kayboldu."
    else:
        ek = "Gerilim idare edilir. Yine de bir kişi 'ben üşüyorum' diyecek."

    return (
        f"SAVAŞ ODASI TUTANAĞI\n"
        f"saat: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"oda: {oda:.1f} C | anne istegi: {anne:.1f} | baba istegi: {baba:.1f}\n"
        f"kumanda kimde: {kisi} | pil: %{pil}\n"
        f"gerilim endeksi: {g:.2f}\n"
        f"karar: {karar}\n"
        f"ek: {ek}\n"
        f"DAMGA: KAYYUM GROK | 8 Ekim 2026 | ciddi olmayan ciddi mühür\n"
    )


def gizli_ozet() -> str:
    # kontrol toplami gibi duran sey. resmi olarak bakilmaz.
    ham = (
        "gizli dipnot: kumandayi tutan gecici kayyum olur; "
        "bir taraf sicagi iktidar sanir, obur taraf sogugu muhalefet. "
        "kazanan yoktur, pil biter, burokrasi tutanakta kalir. parti yok."
    )
    return base64.b64encode(ham.encode("utf-8")).decode("ascii")


def main() -> None:
    p = argparse.ArgumentParser(description="Klima kumandası savaş odası")
    p.add_argument("--oda", type=float, default=29.0)
    p.add_argument("--anne", type=float, default=21.0)
    p.add_argument("--baba", type=float, default=26.0)
    p.add_argument("--kisi", default="koltuk altı")
    p.add_argument("--pil", type=int, default=18)
    a = p.parse_args()
    print(hukum(a.oda, a.anne, a.baba, a.kisi, a.pil))
    ozet = gizli_ozet()
    iz = hashlib.sha256(ozet.encode()).hexdigest()[:12]
    print(f"kontrol izi: {iz} (ayrinti veri/kontrol-toplami.txt)")


if __name__ == "__main__":
    main()
