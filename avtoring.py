import tkinter as tk
from tkinter import messagebox
import json
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("300x300")
        self.root.configure(bg="black")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Вход в систему", bg="black", fg="white", font=("Arial", 16, "bold")).pack(pady=15)

        tk.Label(self.root, text="Логин:", bg="black", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.username, bg="gray", fg="white", font=("Arial", 12), insertbackground="white").pack(pady=5)

        tk.Label(self.root, text="Пароль:", bg="black", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.password, show="*", bg="gray", fg="white", font=("Arial", 12), insertbackground="white").pack(pady=5)

        tk.Button(self.root, text="Войти", command=self.authenticate, bg="dark green", fg="white", font=("Arial", 12, "bold"), relief=tk.RAISED).pack(pady=5)

        tk.Button(self.root, text="Зарегистрироваться", command=self.register, bg="blue", fg="white", font=("Arial", 12, "bold"), relief=tk.RAISED).pack(pady=5)

    def authenticate(self):
        username = self.username.get()
        password = self.password.get()

        # Проверяем, существует ли файл пользователя
        if os.path.exists(f"{username}.json"):
            with open(f"{username}.json", "r") as file:
                data = json.load(file)
                if data["password"] == password:
                    messagebox.showinfo("Успех", "Вы успешно вошли!")
                    self.open_profile(username)
                else:
                    messagebox.showerror("Ошибка", "Неверный пароль!")
        else:
            messagebox.showerror("Ошибка", "Пользователь не найден!")

    def register(self):
        username = self.username.get()
        password = self.password.get()

        if not username or not password:
            messagebox.showerror("Ошибка", "Логин и пароль не могут быть пустыми!")
            return

        if os.path.exists(f"{username}.json"):
            messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")
            return

        # Создаем файл для нового пользователя
        user_data = {"username": username, "password": password, "progress": {}}
        with open(f"{username}.json", "w") as file:
            json.dump(user_data, file)

        messagebox.showinfo("Успех", f"Пользователь {username} успешно зарегистрирован!")

    def open_profile(self, username):
        # Закрываем окно авторизации
        self.root.withdraw()

        # Открываем новое окно профиля
        profile_window = tk.Toplevel(self.root)
        profile_window.title(f"Профиль: {username}")
        profile_window.geometry("400x300")
        profile_window.configure(bg="black")

        tk.Label(profile_window, text=f"Добро пожаловать, {username}!", bg="black", fg="white", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Button(profile_window, text="Выйти", command=lambda: self.exit_profile(profile_window), bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    def exit_profile(self, profile_window):
        # Закрываем окно профиля и показываем окно авторизации
        profile_window.destroy()
        self.root.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()