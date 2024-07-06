import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_script()

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            if self.process:
                self.process.terminate()
            self.start_script()

    def start_script(self):
        self.process = subprocess.Popen([sys.executable, self.script])


if __name__ == "__main__":
    script = "sua_calculadora.py"  # substitua com o nome do seu script
    event_handler = ReloadHandler(script)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
