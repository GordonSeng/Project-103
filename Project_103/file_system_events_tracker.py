import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey,{event.src_path} has been Created!")

    def on_deleted(self,event):
        print(f"Oops! someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        print(f"File moved: {event.src_path} to {event.dest_path}")

from_dir = "/Users/rebeccaseng/Downloads"

observer = Observer()
observer.schedule(FileEventHandler(), from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()