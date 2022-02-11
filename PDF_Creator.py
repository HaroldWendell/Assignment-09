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