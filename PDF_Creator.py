# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF
import json
from datetime import date
from fpdf import FPDF

today = date.today()
# Create a blank PDF Paper with a single border.
pdf = FPDF()
pdf = FPDF(orientation='P', unit='mm', format='Letter')
pdf.add_page()
pdf.rect(5.0, 5.0, 206.0, 269.0)

# Open the JSON file which contains the data and insert a .JPG file that contains my photo.
pdf.image('My_Picture.jpg', 140, 15, 55, 55)
with open('Resume_data.json') as data:
    info = json.load(data)

for line in info:
    # Convert the JSON data from variable Name up to Email into a PDF text/format.
    pdf.set_font("times", 'B', size=20)
    pdf.cell(80, 30, line['Name'], ln = 1, align = "L")
    pdf.set_font("times", size=14)
    pdf.cell(80, -15, txt = "Gender: " + line['Gender'], ln = 1, align ="L")
    pdf.cell(80, 28, txt = "Age: " + line['Age'], ln = 1, align ="L")
    pdf.cell(80, -15, txt = "Contact No. " + line['Contact No.'], ln = 1, align ="L")
    pdf.cell(80, 28, txt = "Email: " + line['Email'], ln = 1, align ="L")

    # Bold the text "Career Objective" and arrange the sentence in the variable Career Objective in JSON data in a short paragraph form.
    pdf.set_font("times", 'B', size = 17)
    pdf.cell(80, 15, txt = "Career Objective", ln = 1, align = "L")
    pdf.set_font("times", '', size = 14)
    pdf.multi_cell(0, 5, txt = "    " + line['Career Objective'])

    # Convert the data in the skills variable into a PDF text.
    pdf.set_font('times', size = 14)
    pdf.cell(80, 25, txt = "          Skills:", ln = 1, align = "L")
    pdf.cell(80, -10, txt = "              -" + line['Special Skill1'], ln = 1, align ="L")
    pdf.cell(80, 25, txt = "              -" + line['Special Skill2'], ln = 1, align ="L")
    pdf.cell(80, -10, txt = "              -" + line['Special Skill3'], ln = 1, align ="L")
    pdf.cell(80, 25, txt = "              -" + line['Special Skill4'], ln = 1, align ="L")

    # Arrange the data for Educational attainment of the applicant and convert it in PDF format.
    pdf.set_font("times", 'B', size = 17)
    pdf.cell(80, 4, txt = "Education", ln = 1, align = "L")
    pdf.set_font('times', size = 14)
    pdf.cell(80, 10, txt = "     High School:", ln = 1, align = "L")
    pdf.cell(80, 4, txt = "              " + line['Education1.1'], ln = 1, align ="L")
    pdf.cell(80, 10, txt = "              " + line['Education1.2'], ln = 1, align ="L")
    pdf.set_font("times", 'B', size = 14)
    pdf.cell(80, 4, txt = "              " + line['Education1.3'], ln = 1, align ="L")
    pdf.set_font('times', size = 14)
    pdf.cell(80, 10, txt = "     College:", ln = 1, align = "L")
    pdf.cell(80, 4, txt = "              " + line['Education2.1'], ln = 1, align ="L")
    pdf.cell(80, 10, txt = "              " + line['Education2.2'], ln = 1, align ="L")
    pdf.set_font("times", 'B', size = 14)
    pdf.cell(80, 5, txt = "              " + line['Education2.3'], ln = 1, align ="L")

    # Convert the last part of the resume which is the declaration into a PDF text.
    pdf.set_font('times', size = 14)
    pdf.cell(80, 20, txt = "Declaration", ln = 1, align = "L")
    pdf.multi_cell(0, 5, txt = "    " + line['Declaration'])

    # Generate the date today and save it as a part in the resume.
    pdf.set_font('times', 'U', size = 14)
    pdf.cell(80, 22, txt = f'{today}', ln = 1, align ="C")
    pdf.set_font('times', size = 14)
    pdf.cell(80, -10, txt = "                        " + line['Date'], ln = 1, align ="L")

# Insert the fake signature that I make in paint.
pdf.image('Fake_Signature.jpg', 135, 240, 50, 25)

# Generate the finished and final resume.
pdf.output("BARREDO_HAROLD_WENDELL.pdf")