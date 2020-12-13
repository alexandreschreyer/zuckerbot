import tkinter as tk
from datetime import datetime

from botlogic import BotLogic, State


class App:
    def __init__(self, master):
        self.master = master
        master.title("ZuckerBot")

        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()

        labels = [
            "username:",
            "password:",
            "max. likes:",
            "hashtags:"
        ]

        for idx, text in enumerate(labels):
            label = tk.Label(master=self.frm_form, text=text)
            entry = tk.Entry(master=self.frm_form, width=50)
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)

        self.frm_log = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_log.pack()

        self.txt_edit_log = tk.Text(master=self.frm_log)
        self.txt_edit_log.grid(row=len(labels))

        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

        self.btn_go_text = tk.StringVar()
        self.btn_go_text.set("Start")
        self.btn_go = tk.Button(master=self.frm_buttons, textvariable=self.btn_go_text, command=self.btn_go_event)
        self.btn_go.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def log(self, log_text):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S - ")
        final_text = dt_string + log_text + "\n"

        self.txt_edit_log.insert(tk.END, final_text)

    def btn_go_event(self):
        current_state = self.btn_go_text.get()
        if current_state == "Start":
            self.btn_go_text.set("Stop")
            instance = BotLogic.get_instance(self)
            instance.set_state(State.STARTED)
            instance.start()
        else:
            self.btn_go_text.set("Stopping...")
            instance = BotLogic.get_instance(self)
            instance.set_state(State.STOPPED)
            self.btn_go_text.set("Start")


root = tk.Tk()
gui = App(root)
root.mainloop()
