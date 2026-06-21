from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

pdf = canvas.Canvas("example.pdf", pagesize=A4)  # A4 size in points (width, height)

width, height = A4
pdf.setFont("Times-Roman", 18)
pdf.drawCentredString(width/2, height-30, "Report")

pdf.drawString((width/14),(height-50),"This is an example of a PDF document created using ReportLab in Python.")
pdf.drawString(100, 750, "Hello, PDF!")
pdf.drawString((width/2)-150, (height/8)-100, "This document was generated automatically.", shaping=True)


pdf.save()

print("PDF created successfully!")