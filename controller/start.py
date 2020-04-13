import tkinter as tk
import sys

sys.path.append("..")
from controller.title_loop import ten_second_loop
from controller.argument_parser import ticker_argument_parser
from view.main_view import MainView
from model.model import parse


if __name__ == "__main__":
    arguments = ticker_argument_parser()
    feed = parse(arguments.url[0])
    feed.reverse()
    seconds = 10

    if arguments.timer is not None:
        seconds = arguments.timer

    root = tk.Tk()
    mainView = MainView(master=root)

    ten_second_loop(mainView, seconds, feed)

    # KEEP THIS LAST
    mainView.mainloop()
