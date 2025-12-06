"""
Author: Aysa Jordan
Date: December 6, 2025
Assignment: Module 10.2
"""

"""
This modified version is based on Listing 2.2, Tkinter-By-Example and has been updated to meet the assignment 
requirements. Changes include setting the window title to a last-name format, adding a File → Exit menu option, 
changing task deletion to a right-click, providing instructions directly in the task label, and alternating task 
colors between blue and dark golden yellow for clarity. These modifications improve usability and align 
with the assignment instructions.
"""

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # ---- REQUIRED CHANGES ----
        self.title("Jordan-ToDo App")
        self.geometry("300x400")

        # menu bar with complementary colors (dark blue + golden yellow)
        menubar = tk.Menu(self, bg="#003366", fg="white")
        file_menu = tk.Menu(menubar, tearoff=0, bg="#DAA520", fg="black")
        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)
        # ---------------------------

        self.tasks = []

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical",
                                      command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0),
                                                            window=self.tasks_frame,
                                                            anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # FIRST LINE (ALWAYS BLUE)
        first_line = tk.Label(
            self.tasks_frame,
            text="--- Add items here (right-click to delete) ---",
            bg="#003366",
            fg="white",
            pady=10
        )
        first_line.bind("<Button-3>", self.remove_task)
        self.tasks.append(first_line)
        first_line.pack(side=tk.TOP, fill=tk.X)

        # alternating colors for the *real tasks only*
        self.colour_schemes = [
            {"bg": "#DAA520", "fg": "black"},  # yellow first
            {"bg": "#003366", "fg": "white"}   # blue second
        ]

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            # IMPORTANT:
            # Start the pattern AFTER the first line.
            real_index = len(self.tasks) - 1  # subtract the blue line
            scheme_index = real_index % 2
            scheme = self.colour_schemes[scheme_index]

            new_task.configure(bg=scheme["bg"], fg=scheme["fg"])
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        # Re-apply alternating colors starting AFTER the first line
        for i, task in enumerate(self.tasks):
            if i == 0:
                task.configure(bg="#003366", fg="white")
                continue

            real_index = i - 1
            scheme_index = real_index % 2
            scheme = self.colour_schemes[scheme_index]

            task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()

# SOURCES
# Lab 12. (n.d.). https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
# Love, D. (2018). Python Tkinter by example. https://geossc.ma/wp-content/uploads/2020/06/Tkinter-By-Example.pdf
# Python Tkinter menu example - Create menu options. (2025, August 25). W3resource. http://w3resource.com/python-exercises/tkinter/python-tkinter-events-and-event-handling-exercise-11.php
# Python Tkinter Widgets - StudyTonight. (n.d.). https://www.studytonight.com/tkinter/python-tkinter-widgets