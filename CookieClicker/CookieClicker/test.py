# import tkinter as tk
# import random

# # Function to create a sparkle effect
# def create_sparkle_effect(canvas, x, y, num_sparkles=50):
#     colors = ["#FFFFFF", "#FFD700", "#FF69B4", "#87CEEB", "#00FF00"]
#     sparkles = []

#     for _ in range(num_sparkles):
#         sparkle = canvas.create_oval(
#             x, y, x + 5, y + 5,
#             fill=random.choice(colors),
#             outline=""
#         )
#         sparkles.append(sparkle)

#     def animate_sparkles(sparkles, steps=10):
#         for _ in range(steps):
#             for sparkle in sparkles:
#                 dx = random.randint(-5, 5)
#                 dy = random.randint(-5, 5)
#                 canvas.move(sparkle, dx, dy)
#             canvas.update()
#             canvas.after(50)

#         for sparkle in sparkles:
#             canvas.delete(sparkle)

#     animate_sparkles(sparkles)

# # Function to handle button click with sparkle effect
# def on_button_click(event):
#     x, y = event.x, event.y
#     create_sparkle_effect(canvas, x, y)

# # Create the main window
# root = tk.Tk()
# root.title("Sparkle Effect Example")
# root.geometry("600x400")

# # Create a canvas to draw sparkles on
# canvas = tk.Canvas(root, bg="#a67c5e")
# canvas.pack(fill="both", expand=True)

# # Create a button
# button = tk.Button(root, text="Click me", font=("Arial", 18))
# button.pack(pady=50)
# button.bind("<Button-1>", on_button_click)

# # Run the application
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
tk.Label(root, text="If you see this, tkinter is working!").pack()
root.mainloop()