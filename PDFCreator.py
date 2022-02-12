
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


pdf.set_font('Arial', '', 16)

resumeData = open('resume.json','r')
resumeFile = resumeData.read()

obj = json.loads(resumeFile)

list = obj['Personal Information']
print(len(list))

for i in range(len(list)):
    NameObj = 'Name:', list[i].get('Name')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, NameObj)



pdf.output('BAROTO_MA. BERNADETE.pdf')










