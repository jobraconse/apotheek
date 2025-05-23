from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(pdf_path, text, prijs):
    current_date = datetime.now().strftime("%d/%m/%Y")  # noqa: DTZ005
    y = 690
    # Create a canvas
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add content to the PDF
    c.drawString(100, 750, "Bestelling Apotheker")
    c.drawString(100, 730, f"Date: {current_date}")
    for line in text:
        c.drawString(100, y, line)
        y = y - 20
    y = y - 20
    c.drawString(100, y, f"Totale prijs bestelling: {prijs}")
    # Close the canvas and save the PDF
    c.save()

    print(f"PDF created successfully: {pdf_path}")
