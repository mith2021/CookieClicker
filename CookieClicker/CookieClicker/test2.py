import tkinter as tk
from PIL import Image, ImageTk
import random

# Create the main window
root = tk.Tk()
root.title("Canvas Over Button Example")
root.geometry("500x500")
root.config(bg="#ffebcd")

# Load the cookie image
cookie_image_path = "D:/Mithun_Complete/PYTHON_MITHUN/CookieClicker/images/def_cookie.jpg"
initial_image = Image.open(cookie_image_path)
cookie_image = ImageTk.PhotoImage(initial_image)

# Function to handle button click
def on_button_click():
    print("Cookie Clicked!")
    create_sparkle_effect(100, 100)

# Function to create a sparkle effect
def create_sparkle_effect(x, y):
    for _ in range(20):  # Number of sparkles
        size = random.randint(1, 5)
        dx = random.randint(-50, 50)
        dy = random.randint(-50, 50)
        sparkle = canvas.create_oval(x, y, x + size, y + size, fill="yellow", outline="yellow", width=0)
        canvas.move(sparkle, dx, dy)

# Create a canvas and place it in the main window
canvas = tk.Canvas(root, width=500, height=500, bg="#ffebcd", highlightthickness=0)
canvas.place(x=0, y=0)

# Create the cookie button on the canvas
clicker_button = tk.Button(root, image=cookie_image, command=on_button_click, height=200, width=200, bg="#ffebcd", relief="flat", activebackground="#ffebcd", bd=0)
clicker_button.image = cookie_image
canvas.create_window(250, 250, window=clicker_button)  # Place button at the center of the canvas

# Bind the click event to the canvas
canvas.bind("<Button-1>", on_button_click)

# Run the application
root.mainloop()
