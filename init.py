from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    title = 'Report'
    reporter = "Omar"
    txt = "text"
    filename = "example.pdf"

    def header(self):
        # Header font
        self.set_font('Arial', 'B', 25)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 5, self.title, 0, 0, "C")
        # Line break
        self.ln(10)
        # Visible line
        self.line(0, 20, 210, 20)
        # Date and time font
        self.set_font('Arial', 'I', 10)
        # Reporter name
        self.cell(80, 10, "Reporter : " + self.reporter, 0, 0, "C")
        # Move to the right
        self.cell(60)
        # Generating time
        self.cell(20, 10, 'Date: ' + str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")), 0, 0, 'C')
        # Visible line
        self.line(0, 30, 210, 30)
        # Break line
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1..5 cm from bottom
        self.set_y(-15)
        # Arial italic
        self.set_font('Arial', 'IB', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
        # Signature font
        self.set_font('Arial', 'I', 8)
        # Signature message
        self.cell(0, 10, "This document was generated automatically.", 0, 0, "R")

    def content(self, txt):
        # add page
        self.add_page()
        # Break line
        self.ln(20)
        # Content font
        self.set_font('Times', '', 18)
        # Content text
        self.multi_cell(0, 10, txt, 0, "")


pdf = PDF()
pdf.title = "Report"
pdf.reporter = "Omar"
text = """We also publish the latest PuTTY installers for all Windows architectures as\
a free-of-charge download at the Microsoft Store; they usually take a few days to\
appear there after we release them."""
# add content
pdf.content(text)
# save new file or edit file
pdf.output("example.pdf", "F")
# show after saved
print("The document has been saved to: " + "example.pdf")