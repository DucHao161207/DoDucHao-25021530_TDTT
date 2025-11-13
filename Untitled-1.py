# ...existing code...
def calculate_total(item_name: str, qty: int, price: float) -> float:
    return qty * price

def format_receipt(item_name: str, qty: int, price: float) -> str:
    total = calculate_total(item_name, qty, price)
    return (f"Item: {item_name}\n"
            f"Quantity: {qty}\n"
            f"Price per item: ${price:.2f}\n"
            f"Total payment: ${total:.2f}")

if __name__ == "__main__":
    # given variables
    item_name = "Book A"
    qty = 2
    price = 2.5

    print(format_receipt(item_name, qty, price))
# ...existing code...