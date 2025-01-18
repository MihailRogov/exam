import tkinter as tk
from tkinter import ttk

# Функция для конвертации температуры
def convert_temperature():
  try:
    fahrenheit = float(entry_fahrenheit.get())
    target_unit = combo_target_unit.get()
    
    if target_unit == "Цельсии (ºC)":
      result = (fahrenheit - 32) * 5/9
    elif target_unit == "Кельвины (K)":
      result = (fahrenheit - 32) * 5/9 + 273.15
    else:
      result = "Ошибка"
    
    label_result.config(text=f"Результат: {result:.2f} {target_unit.split()[0]}")
  except ValueError:
    label_result.config(text="Ошибка: Введите числовое значение")
# Создаем главное окно
root = tk.Tk()
root.title("Конвертер температуры")
root.resizable(False, False)  # Блокируем изменение размера окна
# Создаем и размещаем метку и поле ввода для температуры в Фаренгейтах
label_fahrenheit = tk.Label(root, text="Введите температуру в Фаренгейтах:")
label_fahrenheit.grid(row=0, column=0, padx=10, pady=10)

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=0, column=1, padx=10, pady=10)

# Создаем и размещаем метку и выпадающий список для выбора целевой единицы измерения
label_target_unit = tk.Label(root, text="Выберите нужную температуру:")
label_target_unit.grid(row=1, column=0, padx=10, pady=10)

combo_target_unit = ttk.Combobox(root, values=["Цельсии (ºC)", "Кельвины (K)"])
combo_target_unit.grid(row=1, column=1, padx=10, pady=10)
combo_target_unit.current(0)  # Устанавливаем значение по умолчанию

# Создаем и размещаем кнопку для конвертации
button_convert = tk.Button(root, text="Конвертировать", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Создаем и размещаем метку для отображения результата
label_result = tk.Label(root, text="Результат: ")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Запускаем приложение
root.mainloop()