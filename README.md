# 🧾 Automatic Invoice Generator (Python)

A simple and customizable invoice generator built with **Python** using the lightweight [`fpdf`](https://py-pdf.github.io/fpdf2/) library. It generates professional PDF invoices dynamically based on customer information and purchased items.

---

## 🚀 Features

* Add **Customer Name** and **Date** dynamically
* Items with quantity and unit price
* Auto-calculated **Total**
* Clean, readable PDF layout
* Outputs `.pdf` file ready for download or email

---

## 🧰 Requirements

* Python 3.6+
* fpdf (`pip install fpdf`)

---

## 📦 Installation

```bash
git clone https://github.com/MohamedOsama011/invoice-generator.git
cd invoice-generator
pip install fpdf
```

---

## 🧪 Example Usage

```python
from invoice import generate_invoice

items = [
    {"name": "Product A", "quantity": 2, "price": 10},
    {"name": "Product B", "quantity": 1, "price": 20}
]

generate_invoice("mohamed osama", items)
```

This will generate a file called `invoice.pdf` in the current directory.

---

## 👨‍💼 Output Sample

* Customer Name: **Mohamed Osama**
* Date: **2025-08-04 18:15:22**
* Items:

  * Product A (x2) - \$20.00
  * Product B (x1) - \$20.00
* **Total: \$40.00**

---

## 📁 File Structure

```
invoice-generator/
│
├── invoice.py        # Main PDF generation logic
├── invoice.pdf       # Sample output file
└── README.md         # Project documentation
```

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use and modify it for personal or commercial use.

---

## 👨‍💻 Author

**Mohamed Osama** – *Python Developer*
Feel free to connect or ask questions!
