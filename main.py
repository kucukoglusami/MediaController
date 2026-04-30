import asyncio
import threading
from media_manager import MediaManager
from overlay_ui import MediaOverlay

async def core_logic(window, scanner):
    while True:
        try:
            data = await scanner.get_current_media_info()
            if data:
                window.after(0, window.update_display, data['title'], data['artist'])
        except Exception:
            pass
        await asyncio.sleep(1)

def run_async_loop(loop, window, scanner):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(core_logic(window, scanner))

if __name__ == "__main__":
    logic = MediaManager()
    
    event_loop = asyncio.new_event_loop()
    
    ui = MediaOverlay(media_manager=logic, event_loop=event_loop)
    
    logic_thread = threading.Thread(
        target=run_async_loop,
        args=(event_loop, ui, logic),
        daemon=True
    )
    logic_thread.start()
    
    ui.mainloop()