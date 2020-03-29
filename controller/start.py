import time
import tkinter as tk
import threading as th
from model.model import Model
from view.main_view import MainView
from concurrent.futures import ThreadPoolExecutor

root = tk.Tk()
mainView = MainView(master=root)

model = Model(mainView)
model.load_entries("https://www.theguardian.com/us/rss")


def ten_second_loop():
    """
    Python-RSS-ticker.controller.start.ten_second_loop should be spawned
    in a separate thread from tkinter and should call model.switch_displayed_entry
    and then sleep for 10 seconds
    """
    while True:
        model.switch_displayed_entry()
        time.sleep(10)


# Thread setup, execution and termination
with ThreadPoolExecutor(max_workers=1) as spool:
    spool.submit(ten_second_loop())

# KEEP THIS LAST
mainView.mainloop()
