# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF
import json
from fpdf import FPDF

pdf = FPDF()
pdf = FPDF(orientation='P', unit='mm', format='Letter')
pdf.add_page()
pdf.rect(5.0, 5.0, 206.0, 269.0)

with open('Resume_data.json') as data:
    info = json.load(data)

for line in info:
    pdf.set_font("Arial", 'B', size=20)
    pdf.cell(80, 30, line['Name'], ln = 1, align = "L")
    pdf.set_font("Arial", size=14)
    pdf.cell(80, -15, txt = "Gender: " + line['Gender'], ln = 1, align ="L")
    pdf.cell(80, 28, txt = "Age: " + line['Age'], ln = 1, align ="L")
    pdf.cell(80, -15, txt = "Contact No. " + line['Contact No.'], ln = 1, align ="L")
    pdf.cell(80, 28, txt = "Email: " + line['Email'], ln = 1, align ="L")

pdf.output("BARREDO_HAROLD_WENDELL.pdf")