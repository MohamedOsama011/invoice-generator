from fpdf import FPDF
from datetime import datetime
import uuid

def add_item(name: str, quantity: int, price: float) -> dict:
    """
    Adds a single item to the invoice.
    Returns a dictionary with item details including total price.
    """
    total = quantity * price
    return {
        "name": name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

def calculate_total(items: list) -> float:
    total = 0
    for item in items:
        total += item["total"]
    return total

def generate_invoice(customer_name: str, items: list, filename: str = None) -> str:

    if filename is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
        safe_name = customer_name.replace(" ", "_")
        filename = f"invoice_{safe_name}_{date_str}.pdf"

    # Generate a unique invoice ID
    invoice_id = str(uuid.uuid4())[:8]

    # Generates a PDF invoice
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="INVOICE", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", "",11)
    pdf.cell(0, 10, txt=f"Invoice ID: {invoice_id}", ln=1)

    # Customer Name label (bold)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(45, 10, txt="Customer Name:", ln=0)
    # Customer Name value (normal)
    pdf.set_font("Arial", "", 12)
    pdf.cell(60, 10, txt=customer_name, ln=0)

    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Date label (bold)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(20, 10, txt="Date:", ln=0)

    # Date value (normal)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, txt=date_str, ln=1)

    # table headers
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Item", border=1)
    pdf.cell(30, 10, "Quantity", border=1)
    pdf.cell(40, 10, "Price", border=1)
    pdf.cell(40, 10, "Total", border=1)
    pdf.ln()

    # data rows
    pdf.set_font("Arial", size=12)
    for item in items:
        pdf.cell(60, 10, item["name"], border=1)
        pdf.cell(30, 10, str(item["quantity"]), border=1)
        pdf.cell(40, 10, f"${item['price']:.2f}", border=1)
        pdf.cell(40, 10, f"${item['total']:.2f}", border=1)
        pdf.ln()

    # total price
    total_price = calculate_total(items)
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(130, 10, "Total", border=1)
    pdf.cell(40, 10, f"${total_price:.2f}", border=1)
    
    # Save the PDF to a file
    pdf.output(filename)
    return filename

def main():
    
    print("Welcome to Invoice Generator!")
    items = []
    customer_name = input("Enter customer name: ").title()
    if not customer_name:
        print("Customer name cannot be empty.")
        return
    
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))

        item = add_item(name, quantity, price)
        items.append(item)

    total = calculate_total(items)
    print(f"Total: ${total:.2f}")

    generate_invoice(customer_name, items)
    print("Invoice generated successfully.")

if __name__ == "__main__":
    main()
