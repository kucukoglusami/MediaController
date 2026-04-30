import customtkinter as ctk
import pyautogui
import asyncio
import os
from PIL import Image

MASK    = "#000001"
WIN_W   = 380
WIN_H   = 80


class MediaOverlay(ctk.CTk):
    def __init__(self, media_manager, event_loop):
        super().__init__()
        self.mm    = media_manager
        self._loop = event_loop

        sw = self.winfo_screenwidth()
        self.geometry(f"{WIN_W}x{WIN_H}+{(sw // 2) - WIN_W // 2}+0")

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.config(bg=MASK)
        self.attributes("-transparentcolor", MASK)

        self.container = ctk.CTkFrame(
            self,
            fg_color="#1a1a2e",
            bg_color=MASK,
            corner_radius=40,
            border_width=1,
            border_color="#3a3a5c",
        )
        self.container.pack(fill="both", expand=True, padx=6, pady=6)

        self.load_images()
        self._setup_ui()
        self.check_loop()

    def load_images(self):
        base   = os.path.dirname(os.path.abspath(__file__))
        assets = os.path.join(base, "assets")
        self.img_placeholder = ctk.CTkImage(
            Image.open(os.path.join(assets, "placeholder.png")), size=(44, 44)
        )
        self.img_pause = ctk.CTkImage(
            Image.open(os.path.join(assets, "pause_icon.png")), size=(16, 16)
        )
        self.img_next = ctk.CTkImage(
            Image.open(os.path.join(assets, "next_icon.png")), size=(16, 16)
        )

    def _setup_ui(self):
        self.btn_next = ctk.CTkButton(
            self.container,
            image=self.img_next,
            text="",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#2a2a4e",
            corner_radius=15,
            command=self._next_wrapper,
        )
        self.btn_next.pack(side="right", padx=(0, 14))

        self.btn_play = ctk.CTkButton(
            self.container,
            image=self.img_pause,
            text="",
            width=34,
            height=34,
            fg_color="#e0e0ff",
            hover_color="#c0c0ee",
            corner_radius=17,
            command=self._play_pause_wrapper,
        )
        self.btn_play.pack(side="right", padx=(0, 8))

        # ── Sol taraf: albüm kapağı ──
        self.album_art = ctk.CTkLabel(
            self.container, image=self.img_placeholder, text=""
        )
        self.album_art.pack(side="left", padx=(12, 10))

        text_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        text_frame.pack(side="left", fill="both", expand=True)

        self.title_label = ctk.CTkLabel(
            text_frame,
            text="Yükleniyor...",
            font=("Segoe UI", 12, "bold"),
            text_color="#ffffff",
            anchor="w",
        )
        self.title_label.pack(anchor="w", pady=(10, 2))

        self.artist_label = ctk.CTkLabel(
            text_frame,
            text="",
            font=("Segoe UI", 10),
            text_color="#9090bb",
            anchor="w",
        )
        self.artist_label.pack(anchor="w")

    def _play_pause_wrapper(self):
        asyncio.run_coroutine_threadsafe(self.mm.press_play_pause(), self._loop)

    def _next_wrapper(self):
        asyncio.run_coroutine_threadsafe(self.mm.press_next(), self._loop)

    def check_loop(self):
        mx, my = pyautogui.position()
        try:
            wx = self.winfo_x()
            wy = self.winfo_y()
            ww = self.winfo_width()
            wh = self.winfo_height()
            on_window = (wx - 10 <= mx <= wx + ww + 10) and (wy - 5 <= my <= wy + wh + 10)
            self.attributes("-alpha", 1.0 if on_window else 0.0)
        except Exception:
            pass
        self.after(50, self.check_loop)

    def update_display(self, title: str, artist: str):
        self.title_label.configure(text=title[:22])
        self.artist_label.configure(text=artist[:28])