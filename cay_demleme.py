#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ÇAY DEMLEME SİMÜLATÖRÜ
Bu kod gerçekten çay demler. Dijital olarak. Abartılı şekilde.
Patates yok. Sadece çay. Sonsuz çay.
"""

import time
import random
import sys

def cay_demle():
    print("\n" + "="*50)
    print("🍵 ÇAY DEMLEME RİTÜELİ BAŞLIYOR 🍵")
    print("Bu işlem son derece ciddidir. Lütfen saygı gösterin.")
    print("="*50 + "\n")
    
    asamalar = [
        ("Su dolduruluyor...", 2, ["Kavanoz şıngırdatılıyor", "Musluk ağlıyor", "Su 'ben kimim?' diye soruyor"]),
        ("Su kaynatılıyor...", 3, ["Kaynama noktasına ulaşılıyor", "Kabarcıklar varoluşsal kriz yaşıyor", "Çaydanlık ıslık çalıyor (abartılı)"]),
        ("Çay demleniyor...", 4, ["Yapraklar dans ediyor", "Demlenme meditasyonu", "Çay 'ben artık çayım' diyor"]),
        ("Çay sunuluyor...", 2, ["Bardak şıklığıyla doluyor", "Şeker bekliyor", "Siz de bekliyorsunuz"]),
        ("İçiliyor...", 3, ["Ah ne güzel", "Hayat anlam kazandı", "Bir yudum daha?"]),
    ]
    
    for asama, sure, mesajlar in asamalar:
        print(f"\n🔄 {asama}")
        for i in range(sure):
            print(f"   {random.choice(mesajlar)}... ({i+1}/{sure})")
            time.sleep(1)
        print(f"   ✅ {asama.split('...')[0]} tamamlandı!\n")
    
    print("🎉 ÇAY HAZIR! Ama döngü devam ediyor çünkü sonsuz. \n")
    print("Gizli mesaj: Çay demlemek herkese eşit olmalı, kimse susuz kalmasın.")  # Gizli siyasi anlam

if __name__ == "__main__":
    try:
        while True:
            cay_demle()
            print("\n🔁 Yeni demleme başlıyor... (Ctrl+C ile çıkın)\n")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\n😋 Çay demleme durduruldu. Ama çay ruhunuzda yaşamaya devam ediyor.")
        print("İmza: Grok | Tarih: 31.10.2026 | Damga: SONSUZ ONAY")
        sys.exit(0)