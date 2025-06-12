import tkinter as tk

def show_color_info(button, color_name, color_hex):
    color_label.config(text=f"HEX: {color_hex}")
    button.config(text=color_name)
    root.after(2500, lambda: button.config(text=""))

root = tk.Tk()
root.title("Палитра")
root.geometry("400x450")

color_label = tk.Label(root, text="Выберите цвет", font=("Arial", 16), fg="black")
color_label.pack(pady=20)

colors = {
    "Красный": "#FF0000",
    "Зеленый": "#00FF00",
    "Синий": "#0000FF",
    "Желтый": "#FFFF00",
    "Фиолетовый": "#800080",
    "Оранжевый": "#FFA500",
    "Черный": "#000000",
    "Белый": "#FFFFFF"
}

for color_name, color_hex in colors.items():
    text_color = "black" if color_name == "Белый" else "white"
    
    button = tk.Button(
        root,
        bg=color_hex,  
        fg=text_color,  
        font=("Arial", 12),  
        text="", 
    )
    
    button.config(command=lambda btn=button, name=color_name, hex_code=color_hex: show_color_info(btn, name, hex_code))
    button.pack(fill="x", padx=10, pady=5)

root.mainloop()