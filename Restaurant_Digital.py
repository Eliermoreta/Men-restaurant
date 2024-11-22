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
        # Inicialización del restaurante con un menú y una lista de pedidos vacía
        self.menu = Menu()
        self.orders = []

    def take_order(self, item, quantity):
        # Método para tomar un pedido del cliente
        item = item.lower()
        if item in self.menu.menu_items:
            total_price = self.menu.place_order(item, quantity)
            if total_price is not None:
                self.orders.append((item, quantity, total_price))
                return f"Pedido añadido: {quantity} {item}(s), Total: ${total_price}"
            else:
                return "¡Lo siento, ese plato no está en el menú!"
        else:
            return "¡Lo siento, ese plato no está en el menú!"

    def display_orders(self):
        # Método para mostrar los pedidos realizados
        orders_text = "---- Pedidos ----\n"
        for item, quantity, total_price in self.orders:
            orders_text += f"{quantity} {item}(s), Total: ${total_price}\n"
        return orders_text

    def finalizar_pedido(self):
        # Método para finalizar el pedido y mostrar el resumen final
        if self.orders:
            final_summary = "¡Gracias por su pedido! Aquí está el resumen final:\n"
            final_summary += self.display_orders()
            total_a_pagar = sum(order[2] for order in self.orders)
            final_summary += f"Total a pagar: ${total_a_pagar}"
            return final_summary
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

menu_frame = tk.Frame(root, bg="white", bd=2)
menu_frame.pack(side=tk.LEFT, padx=20)

menu_label = tk.Label(menu_frame, text=restaurante.menu.display_menu(), bg="black", fg="white", font=("Arial", 14))
menu_label.pack()

item_label = tk.Label(root, text="Plato:", bg="black", fg="white", font=("Arial", 14))
item_label.pack(side=tk.LEFT, padx=10)
item_entry = tk.Entry(root)
item_entry.pack(side=tk.LEFT, padx=5)

quantity_label = tk.Label(root, text="Cantidad:", bg="black", fg="white", font=("Arial", 14))
quantity_label.pack(side=tk.LEFT, padx=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack(side=tk.LEFT, padx=5)

order_button = tk.Button(root, text="Realizar Pedido", command=make_order, bg="green", fg="white", font=("Arial", 15))
order_button.pack(side=tk.LEFT, padx=10)

finish_button = tk.Button(root, text="Finalizar Pedido", command=finish_order, bg="red", fg="white", font=("Arial", 15))
finish_button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", bg="white", fg="red", font=("Arial", 12))
result_label.pack(side=tk.LEFT, padx=10)

root.mainloop()
