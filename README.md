# 🎵 Media Overlay

Windows için şeffaf, ekranın üstünde çalışan bir medya kontrol overlay'i. Mouse ekranın üst kenarına geldiğinde otomatik görünür, uzaklaştığında kaybolur.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Özellikler

- 🖥️ Ekranın üst ortasında şeffaf kapsül tasarımı
- 🎵 Çalan şarkının adı ve sanatçısını gerçek zamanlı gösterir
- ⏯️ Oynat / Duraklat butonu
- ⏭️ Sonraki parça butonu
- 🖱️ Mouse ekran üstüne gelince otomatik açılır, çekilince kaybolur
- 🪟 Windows Media Session API ile tüm uygulamalarla uyumlu (Spotify, YouTube, vb.)

---

## 📋 Gereksinimler

- Windows 10 veya üzeri
- Python 3.10+

---

## 🚀 Kurulum

**1. Depoyu klonla:**
```bash
git clone https://github.com/kucukoglusami/MediaController.git
cd MediaController
```

**2. Gerekli kütüphaneleri yükle:**
```bash
pip install customtkinter pillow pyautogui winsdk
```

**3. Çalıştır:**
```bash
python main.py
```

---

## 📁 Dosya Yapısı

```
media-overlay/
├── main.py            # Giriş noktası, thread yönetimi
├── media_manager.py   # Windows Media Session API bağlantısı
├── overlay_ui.py      # CustomTkinter arayüzü
├── assets/
│   ├── placeholder.png
│   ├── pause_icon.png
│   └── next_icon.png
└── README.md
```

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane | Amaç |
|---|---|
| `customtkinter` | Modern tkinter arayüzü |
| `winsdk` | Windows Media Session API |
| `pillow` | Görsel işleme |
| `pyautogui` | Mouse konumu takibi |

---

## 📝 Lisans

MIT License — dilediğin gibi kullanabilirsin.
