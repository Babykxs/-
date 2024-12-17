
import tkinter as tk
from tkinter import messagebox
import pandas as pd

def authenticate():
    username = entry_username.get()
    password = entry_password.get()
    
    # Загрузка данных из Excel-файла
    try:
        df = pd.read_excel('users.xlsx')  # Укажите путь к вашему файлу
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")
        return
    
    # Проверка наличия пользователя
    user = df[(df['Логин'] == username) & (df['Пароль'] == password)]
    
    if not user.empty:
        messagebox.showinfo("Успех", "Авторизация успешна!")
        # Здесь можно добавить логику для перехода к следующему шагу или окну
    else:
        messagebox.showerror("Ошибка", "Неправильное имя пользователя или пароль.")

# Создание основного окна
root = tk.Tk()
root.title("Авторизация продавца")

# Метка и поле для логина
label_username = tk.Label(root, text="Логин:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Метка и поле для пароля
label_password = tk.Label(root, text="Пароль:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Кнопка для авторизации
button_login = tk.Button(root, text="Войти", command=authenticate)
button_login.pack(pady=20)

# Запуск главного цикла
root.mainloop()