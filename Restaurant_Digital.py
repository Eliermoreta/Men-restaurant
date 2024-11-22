import tkinter as tk

class Menu:
    def __init__(self):
        # Diccionario que contiene los platos del menú y sus precios
        self.menu_items = {
            "hamburguesa": 300,
            "pizza": 350,
            "ensalada": 400,
            "pasta": 1000,
            "sopa": 200,
            "arroz con pollo": 700,
            "sancocho": 800,
            "pechuga a la plancha": 900,
            "tostones con pescado frito": 1500,
            "arroz con camarones": 1200,
            "flan": 200,
            "pastel de chocolate": 250,
            "helado": 150,
            "batido de frutas": 300,
            "refresco": 100,
            "café": 80,
            "té": 70
        }

    def display_menu(self):
        # Método para mostrar el menú con los platos y sus precios
        menu_text = "------ Menú --------\n"
        for item, price in self.menu_items.items():
            menu_text += f"{item.capitalize()}: ${price}\n"
        return menu_text

    def place_order(self, item, quantity):
        # Método para realizar un pedido
        item = item.lower()
        if item in self.menu_items:
            total_price = self.menu_items[item] * quantity
            return total_price
        else:
            return None


class Restaurante:
    def __init__(self):
        self.menu = Menu()
        self.orders = []
        self.discount = 0  # Porcentaje de descuento aplicado

    def apply_discount(self, discount_code):
        valid_discounts = {"PROMO10": 10, "PROMO20": 20}
        if discount_code in valid_discounts:
            self.discount = valid_discounts[discount_code]
            return f"¡Descuento del {self.discount}% aplicado!"
        else:
            return "Código de descuento no válido."

   class Restaurante:
    def finalizar_pedido(self):
        if not self.orders:
            return "No ha realizado ningún pedido. Por favor, añada platos antes de finalizar."
        

    else:
        return "No ha realizado ningún pedido."

def make_order():
    item = item_entry.get().strip()
    if not item:
        result_label.config(text="¡Error! Por favor, ingrese un nombre de plato.")
        return

    quantity_text = quantity_entry.get().strip()
    if not quantity_text.isdigit():
        result_label.config(text="¡Error! Por favor, ingrese un número entero para la cantidad.")
        return

    quantity = int(quantity_text)
    if quantity <= 0:
        result_label.config(text="¡Error! La cantidad debe ser un número positivo.")
        return

    if item.lower() not in restaurante.menu.menu_items:
        result_label.config(text="¡Error! Ese plato no existe en el menú.")
        return

    result = restaurante.take_order(item, quantity)
    result_label.config(text=result)


def finish_order():
    result = restaurante.finalizar_pedido()
    result_label.config(text=result)

# Crear la interfaz gráfica
root = tk.Tk()
root.geometry("1950x900")
root.configure(bg="Silver")
root.title("Restaurante")

restaurante = Restaurante()

# Sustituir el bloque donde se define el menú y el marco (menu_frame)
menu_frame = tk.Frame(root, bg="white", bd=2)
menu_frame.pack(side=tk.LEFT, padx=20, fill=tk.Y)

menu_scrollbar = tk.Scrollbar(menu_frame)
menu_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

menu_label = tk.Text(menu_frame, bg="black", fg="white", font=("Arial", 14), wrap=tk.WORD, yscrollcommand=menu_scrollbar.set)
menu_label.insert(tk.END, restaurante.menu.display_menu())
menu_label.config(state=tk.DISABLED)
menu_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

menu_scrollbar.config(command=menu_label.yview)

# Sustituir el diseño del result_label
result_label = tk.Label(root, text="", bg="lightgrey", fg="blue", font=("Arial", 12))
result_label.pack(side=tk.LEFT, padx=10, fill=tk.X)


root.mainloop()
