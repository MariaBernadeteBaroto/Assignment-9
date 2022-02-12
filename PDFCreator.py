
# Imports


from fpdf import FPDF
import json


class PDF(FPDF):
    def header(self):
        #logo
        self.image('i.d.png', 150, 20, 50)
        #font
        self.set_font('Arial', 'B', 20)
        # TITLE
        self.cell(0, 10, 'Resume', border = False, ln = 1, align = 'C')
        #line break
        self.ln(20)


pdf = PDF('P', 'mm', 'Letter')


pdf.add_page()


pdf.set_font('Arial', '', 12)

resumeData = open('resume.json','r')

for line in resumeData:
    pdf.cell(20, 5, txt=line, ln=1, align='L')



pdf.output('BAROTO_MA. BERNADETE.pdf')










