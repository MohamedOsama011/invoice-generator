import os
from project import add_item, calculate_total, generate_invoice

def test_add_item():
    item = add_item("Keyboard", 2, 150.0)
    assert item["name"] == "Keyboard"
    assert item["quantity"] == 2
    assert item["price"] == 150.0
    assert item["total"] == 300.0

def test_calculate_total():
    items = [
        {"name": "Mouse", "quantity": 1, "price": 100.0, "total": 100.0},
        {"name": "Monitor", "quantity": 2, "price": 200.0, "total": 400.0}
    ]
    assert calculate_total(items) == 500.0

def test_generate_invoice_creates_pdf():
    # Arrange
    customer_name = "Test Customer"
    items = [
        add_item("Pen", 3, 10.0),
        add_item("Notebook", 2, 20.0)
    ]
    total = calculate_total(items)

    # Act
    filename = generate_invoice(customer_name, items)

    # Assert
    assert os.path.exists(filename)
    assert filename.endswith(".pdf")
    assert os.path.getsize(filename) > 0

    # Cleanup (remove the file after test)
    os.remove(filename)

