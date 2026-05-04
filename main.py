import tkinter as tk
from tkinter import ttk, messagebox
from api import get_rate
from storage import save_history, load_history

def convert():
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            raise ValueError

        from_cur = combo_from.get()
        to_cur = combo_to.get()

        rate = get_rate(from_cur, to_cur)
        result = amount * rate

        label_result.config(text=f"{result:.2f} {to_cur}")

        record = {
            "amount": amount,
            "from": from_cur,
            "to": to_cur,
            "result": result
        }

        history.append(record)
        save_history(history)
        update_table()

    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительное число")

def update_table():
    table.delete(*table.get_children())
    for item in history:
        table.insert("", "end", values=(
            item["amount"], item["from"], item["to"], f'{item["result"]:.2f}'
        ))

# GUI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")

currencies = ["USD", "EUR", "GBP", "JPY", "RUB"]

combo_from = ttk.Combobox(root, values=currencies)
combo_from.set("USD")
combo_from.pack()

combo_to = ttk.Combobox(root, values=currencies)
combo_to.set("EUR")
combo_to.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

btn = tk.Button(root, text="Конвертировать", command=convert)
btn.pack()

label_result = tk.Label(root, text="Результат")
label_result.pack()

# Таблица истории
table = ttk.Treeview(root, columns=("amount", "from", "to", "result"), show="headings")
for col in ("amount", "from", "to", "result"):
    table.heading(col, text=col)
table.pack(fill="both", expand=True)

# Загрузка истории
history = load_history()
update_table()

root.mainloop()