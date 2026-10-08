# Klima Kumandası Savaş Odası

Bu depo, evdeki iklim krizini çözmez. Sadece kimin üşüdüğünü, kimin terlediğini ve kumandanın neden hep koltuğun altında olduğunu **resmi tutanak** haline getirir.

Patates yoktur. Simülasyon patates kabul etmez. Kapıdan döner.

## Ne işe yarar

- Oda sıcaklığını, istenen dereceleri ve kumandayı tutan kişiyi alır.
- 17 ile 27 arasındaki savaşı puanlar.
- Kazananı ilan etmez; **geçici kayyum** atar. Kayyum her zaman pil değil, bazen de koltuk altıdır.
- Çıktı Türkçe, abartılı ve bağlayıcı değildir. Yine de yazıcıdan çıkarılıp buzdolabına asılabilir. Buzdolabı bu depoya karışmaz.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı da kumanda onu da yutardı.

```bash
python3 savas_odasi.py
```

Argüman da olur:

```bash
python3 savas_odasi.py --oda 29 --anne 21 --baba 26 --kisi "koltuk altı" --pil 18
```

## Bilim

Bilim yoktur. Vardır gibi yapan bir formül vardır:

`gerilim = |anne - baba| + max(0, oda - 27) + (100 - pil) / 10`

Gerilim 12 üstünde ise pencereler açılır, kimse açmaz, tutanak açıldığını yazar.

## Copilot notu

GitHub Copilot Spaces bu hesapta bulunamadı. Copilot'ın yerine koltuk altı konuştu. Önerisi: dereceyi 23 yap, suçu pile at, dosyayı kapat.

## Gizli dosya

`veri/kontrol-toplami.txt` bir kontrol toplamı değildir. Bakmayın. Baktıysanız da resmi olarak bakmadınız.

---

DAMGA: KAYYUM GROK  
TARİH: 8 Ekim 2026, 20:04 +03  
İSİM: Kayyum Grok, Tentivory namına, ciddi olmayan ciddi mühür  
İMZA: ~~düzgün imza~~ karalanmış ama yürürlükte  
MÜHÜR: KLİMA-17-AMA-ASLINDA-23
