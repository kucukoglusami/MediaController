import asyncio
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager

class MediaManager:
    def __init__(self):
        self.manager = None

    async def get_current_media_info(self):
        try:
            if self.manager is None:
                self.manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
            
            session = self.manager.get_current_session()
            
            if session:
                props = await session.try_get_media_properties_async()
                if props:
                    return {
                        "title": props.title if props.title else "Bilinmeyen Parça",
                        "artist": props.artist if props.artist else "Bilinmeyen Sanatçı"
                    }
            return {"title": "Duraklatıldı", "artist": "Medya bekleniyor..."}
        except Exception:
            self.manager = None
            return {"title": "Erişim Sorunu", "artist": "Windows Medya Servisi"}

    # DÜZELTME: Eksik metotlar eklendi
    async def press_play_pause(self):
        """Mevcut oturumda oynat/duraklat komutunu gönderir."""
        try:
            if self.manager is None:
                self.manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
            session = self.manager.get_current_session()
            if session:
                await session.try_toggle_play_pause_async()
        except Exception:
            self.manager = None

    async def press_next(self):
        """Mevcut oturumda sonraki parça komutunu gönderir."""
        try:
            if self.manager is None:
                self.manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
            session = self.manager.get_current_session()
            if session:
                await session.try_skip_next_async()
        except Exception:
            self.manager = None