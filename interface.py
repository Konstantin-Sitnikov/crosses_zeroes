import tkinter as tk
from tkinter import ttk

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        self.name = None
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)
        self.controller = controller

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.grid(row=1, column=0, pady=0)

        self.playinig_field = {(0, 0): "-", (0, 1): "-", (0, 2): "-",
                               (1, 0): "-", (1, 1): "-", (1, 2): "-",
                               (2, 0): "-", (2, 1): "-", (2, 2): "-"}


        # We use the switch_window_button in order to call the show_frame() method as a lambda function

        self.button_creation()


        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.grid(row=5, pady=0)

    def button_creation(self):
        for row in range(1, 4):
            for col in range(1, 4):
                switch_window_button = tk.Button(self,
                                                 text=f"{self.playinig_field[row-1, col-1]}",
                                                 command=lambda i=row, j=col: self.set_symbol(i-1, j-1))
                switch_window_button.grid(row=row, column=col)


    def set_symbol(self, row, col):
        self.playinig_field[row,col] = "X"
        self.button_creation()
        print(self.playinig_field)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)



if __name__ == "__main__":
    test = windows()
    test.mainloop()