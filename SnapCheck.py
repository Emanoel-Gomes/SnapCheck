import os
import pyautogui
import tkinter as tk
from tkinter import filedialog
from PIL import Image

class App:

    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.running = False
        self.screenshot_count = 0
        self.reference_image = Image.open("referencia.png")

    def take_screenshot(self):
        if not self.running:
            return
        screenshot = pyautogui.screenshot(region=(self.x, self.y, self.largura, self.altura))
        self.screenshot_count += 1
        screenshot.save("screenshot.png")
        if self.check_images_equal(screenshot, self.reference_image):
            print("São iguais")
        else:
            print("São diferentes")
        root.after(1000, self.take_screenshot)

    def check_images_equal(self, image1, image2):
        return image1.tobytes() == image2.tobytes()

    def start(self):
        if not self.running:
            self.running = True
            self.take_screenshot()

    def pause(self):
        self.running = False

    def resume(self):
        self.running = True
        self.take_screenshot()

    def select_directory(self):
        directory = filedialog.askdirectory()
        os.chdir(directory)

    def create_gui(self):
        global root
        root = tk.Tk()
        root.geometry("300x200")
        root.title("Screenshot Taker")
        start_button = tk.Button(root, text="Start", width=10, command=self.start)
        start_button.pack(pady=10)
        pause_button = tk.Button(root, text="Pause", width=10, command=self.pause)
        pause_button.pack(pady=10)
        resume_button = tk.Button(root, text="Resume", width=10, command=self.resume)
        resume_button.pack(pady=10)
        directory_button = tk.Button(root, text="Select Directory", width=15, command=self.select_directory)
        directory_button.pack(pady=10)
        root.mainloop()


if __name__ == "__main__":
    x = int(input("Digite a coordenada X da posição do screenshot: "))
    y = int(input("Digite a coordenada Y da posição do screenshot: "))
    largura = int(input("Digite a largura da região de captura: "))
    altura = int(input("Digite a altura da região de captura: "))
    app = App(x, y, largura, altura)
    app.create_gui()
