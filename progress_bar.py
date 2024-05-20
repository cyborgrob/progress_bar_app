import tkinter as tk
from tkinter import ttk
import time

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Progress Bar")

        self.progress = 0
        self.total_time = 360 * 60  # 360 minutes * 60 seconds (6 hours)
        self.start_time = None
        self.running = False

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=self.total_time)
        self.progress_bar.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=20, pady=20)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.progress
            self.update_progress()

    def stop(self):
        if self.running:
            self.running = False
            self.progress = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.progress = 0
        self.progress_var.set(0)

    def update_progress(self):
        if self.running:
            elapsed = time.time() - self.start_time
            self.progress_var.set(elapsed)
            if elapsed < self.total_time:
                self.root.after(100, self.update_progress)
            else:
                self.running = False
                self.progress_var.set(self.total_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()
