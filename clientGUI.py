import tkinter as tk


class ClientGUI():
    def __init__(self) -> None:
        # creating the graphical interface
        self.window = tk.Tk()
        self.connection_status_lbl = tk.Label(text="connecting...")

        self.chatBox = tk.Text()
        self.messageBox = tk.Entry()
        self.sendButton = tk.Button(text="send")

        self.connection_status_lbl.pack()
        self.chatBox.pack()
        self.messageBox.pack()
        self.sendButton.pack()

        self.window.mainloop()

        # creating the client socket
        

    def send_message(self):
        ...


