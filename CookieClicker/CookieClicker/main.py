import tkinter as tk
from PIL import Image, ImageTk
import pygame
from pygame import mixer  
import random

#RBG to Hexadecimal
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

mixer.init()

# did on own
# def get_image_size(image_path):
#     image = tk.PhotoImage(image_path)
#     height = image.height()
#     width = image.width()
#     return height, width

#UI Creation
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("550x700")
rgb_color = (196, 157, 112)
hex_color = rgb_to_hex(rgb_color)
root.config(bg=hex_color)



#Global variables
click_count = 0
money = 1000
multiplier = 1

#Image Loading
inital_image = Image.open(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\images\def_cookie.jpg")
cookie = ImageTk.PhotoImage(inital_image)

#  counter initializer
def initialize__counter():
    on_upgrade1_click.is_bought = False
    
    on_upgrade2_click.is_bought = False

    on_upgrade3_click.is_bought = False 

    on_cookie1_click.is_bought = False 

    on_cookie2_click.is_bought = False 

    on_cookie3_click.is_bought = False 

# Main Clicker Function
def on_button_click():
    global click_count
    global money
    global multiplier
    click_count += 1
    # money = click_count * multiplier
    money += (1 * multiplier)
    label.config(text=f"Button clicked: {click_count} times")
    moneydisplay.config(text=f"Money: ${money}")
    mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\Cute-click.mp3")
    mixer.music.set_volume(0.05)
    mixer.music.play()
    return money , multiplier


#Upgrade Buttons
def on_upgrade1_click( ):
    global money
    global multiplier
    mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\cha ching-sound effect.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play()
    if on_upgrade1_click.is_bought:
        return    
    if not on_upgrade3_click.is_bought:
        if not on_upgrade2_click.is_bought:
            if money >= 50 and not on_upgrade1_click.is_bought:
                money -= 50
                moneydisplay.config(text=f"Money: ${money}")
                multiplier = 2
                on_upgrade1_click.is_bought = True
                return money, multiplier
    return

def on_upgrade2_click( ):
    global money
    global multiplier
    if on_upgrade2_click.is_bought:
        return    
    if not on_upgrade3_click.is_bought:        
            if money >= 100 and not on_upgrade2_click.is_bought:
                money -= 100
                moneydisplay.config(text=f"Money: ${money}")
                multiplier = 6
                on_upgrade2_click.is_bought = True
                mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\cha ching-sound effect.mp3")
                mixer.music.set_volume(0.1)
                mixer.music.play()
                return money, multiplier
    


def on_upgrade3_click( ):   
    global money
    global multiplier
    if on_upgrade3_click.is_bought:
        return    
    if money >= 150 and not on_upgrade3_click.is_bought:
        money -= 150
        moneydisplay.config(text=f"Money: ${money}")
        multiplier = 12
        on_upgrade3_click.is_bought = True
        mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\cha ching-sound effect.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play()
        return money, multiplier
    
     
#Cookie Buttons

def on_cookie1_click():
    global money
    global inital_image 
    if on_cookie1_click.is_bought:
        return    
    if money >= 200:
        money -= 200
        #Update Image
        new_image = Image.open(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\images\rainbow_cookie.png")
        new_photo = ImageTk.PhotoImage(new_image)
        clicker_button.config(image=new_photo)
        clicker_button.image = new_photo
        moneydisplay.config(text=f"Money: ${money}")
        on_cookie1_click.is_bought = True
        mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\cha ching-sound effect.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play()
        return money, new_photo
    

def on_cookie2_click():
    global money
    global multiplier
    if on_cookie2_click.is_bought:
        return    
    if money >= 300:
        money -= 300
        #Update Image
        new_image = Image.open(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\images\Golden_cookie.webp")
        new_photo = ImageTk.PhotoImage(new_image)
        clicker_button.config(image=new_photo)
        clicker_button.image = new_photo
        moneydisplay.config(text=f"Money: ${money}")
        on_cookie2_click.is_bought = True
        mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\cha ching-sound effect.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play()
        return money, new_photo
    
# def on_cookie3_click():
def on_cookie3_click():
    global money
    global multiplier
    if on_cookie3_click.is_bought:
        return    
    if money >= 400:
        money -= 400
        #Update Image
        new_image = Image.open(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\images\god cookie.png")
        new_photo = ImageTk.PhotoImage(new_image)
        clicker_button.config(image=new_photo)
        clicker_button.image = new_photo
        moneydisplay.config(text=f"Money: ${money}")
        on_cookie3_click.is_bought = True
        mixer.music.load(r"C:\Users\mithu\Downloads\Programming\CookieClicker\CookieClicker\Sounds\cha ching-sound effect.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play()
        return money, new_photo
    
#Effect Buttons
# def on_effect1_click():
#     create_sparkle_effect(100, 100)

# def create_sparkle_effect(x , y):
#     colors = ["#FFFFFF", "#FFD700", "#FF69B4", "#87CEEB", "#00FF00"]
#     for _ in range(100):
#         size = random.randint(1,5)
#         dx = random.randint(-5,5)
#         dy = random.randint(-5,5)
#         sparkle = canvas.create_oval(x, y, x+size, y+size, 
#                                      fill=random.choice(colors), 
#                                      outline="", width=0)

# canvas = tk.Canvas(root,width=200, height=200, bg=hex_color, highlightthickness=0 )
# canvas.place(x=0,y=0)

initialize__counter()

label = tk.Label(root, text=f"Button clicked: 0 times", font = ('Comic Sans MS', 18),bg="#a67c5e", borderwidth=5, relief="solid")
label.pack(padx=20, pady=20, fill="both",expand=True)

# Exit = tk.Button(root, text="Exit Game", font = ('Comic Sans MS', 18) )
# Exit.pack( sticky='e', command = exit_game)

moneydisplay = tk.Label(root, text=f"Money: ", font = ('Comic Sans MS', 16), bg="#a67c5e",  borderwidth=5, relief="solid")
moneydisplay.pack(padx=20, pady=20, fill="both",expand=True)

# Main Clicker
clicker_button = tk.Button(root, image= cookie, text="Click Me",command= on_button_click,
                           height = 200
                           ,width=200,
                            font=("Comic Sans MS",12), bg=hex_color, relief="flat" , activebackground= hex_color, bd=0)
clicker_button.image = cookie
clicker_button.pack(padx = 20,pady=20,expand=True)
# canvas.create_window(250, 300, window=clicker_button)
# canvas.bind("<Button-1>", on_effect1_click)


#Shop
#Shop Titles
shop_title = tk.Label(root, text="Shop:", font = ('Comic Sans MS',18), bg="#a67c5e",  borderwidth=5, relief="solid")
shop_title.pack(fill="both",expand=True,padx=10)

shop_frame = tk.Frame(root,borderwidth=2,relief="solid",bg="#a67c5e")
shop_frame.pack(padx=20,pady=10,fill="both",expand=True)

upgrade = tk.Label(shop_frame, text="Upgrades:", font=('Comic Sans MS', 15), bg="#a67c5e") 
upgrade.grid(row=0, column=0, sticky="nsew")

cookie = tk.Label(shop_frame, text="Cookies:", font=('Comic Sans MS', 15), bg="#a67c5e")
cookie.grid(row=0, column=1, sticky="nsew")

effect = tk.Label(shop_frame, text="Effects:", font=('Comic Sans MS', 15), bg="#a67c5e")
effect.grid(row=0, column=2, sticky="nsew")

#Shop Items
Times_2_Multiplier = tk.Button(shop_frame, text = "2X Money Multipler \n Cost: $50",\
                                font=('Comic Sans MS',14), command= on_upgrade1_click, bg='#d19560', relief="solid")
Times_2_Multiplier.grid(row=1, column=0, sticky="n",)

Times_3_Multiplier = tk.Button(shop_frame, text = "6X Money Multipler \n Cost: $100", 
                               font=('Comic Sans MS',14), command= on_upgrade2_click, bg='#d19560', relief="solid")
Times_3_Multiplier.grid(row=2, column=0, sticky="n",)

Times_4_Multiplier = tk.Button(shop_frame, text = "12X Money Multipler \n Cost: $150", 
font=('Comic Sans MS',14), command= on_upgrade3_click, bg='#d19560', relief="solid")
Times_4_Multiplier.grid(row=3, column=0, sticky="n",)

#Cookie Types
cookie_option_1 = tk.Button(shop_frame, text = "Rainbow Cookie \n Cost: $200", font=('Comic Sans MS',14),
                            command=on_cookie1_click, bg='#d19560', relief="solid")
cookie_option_1.grid(row=1, column = 1, sticky = "n",)

cookie_option_2 = tk.Button(shop_frame, text = "Golden Cookie \n Cost: $300", font=('Comic Sans MS',14),
                             command=on_cookie2_click, bg='#d19560', relief="solid")
cookie_option_2.grid(row=2, column = 1, sticky = "n", )

cookie_option_3 = tk.Button(shop_frame, text = "God Cookie \n Cost: $400", font=('Comic Sans MS',14)
                            ,command=on_cookie3_click, bg='#d19560', relief="solid")
cookie_option_3.grid(row=3, column = 1, sticky = "n", )

#Effects
effect_option_1 = tk.Button(shop_frame, text = "Sparkels \n Cost: $200", font=('Comic Sans MS',14),
                            bg='#d19560', relief="solid")
effect_option_1.grid(row=1, column = 2, sticky = "n")

effect_option_2 = tk.Button(shop_frame, text = " TBD \n Cost: $200", font=('Comic Sans MS',14),
                            bg='#d19560', relief="solid")
effect_option_2.grid(row=2, column = 2, sticky = "n")

effect_option_3 = tk.Button(shop_frame, text = " TBD 2 \n Cost: $200", font=('Comic Sans MS',14),
                            bg='#d19560', relief="solid")
effect_option_3.grid(row=3, column = 2, sticky = "n")


# Configure rows and columns
for i in range(4):
    shop_frame.grid_rowconfigure(i, weight=1)
for i in range(3):
    shop_frame.grid_columnconfigure(i, weight=1)

# canvas.bind("<Button-1>", on_effect1_click)

root.mainloop()