from pypdf import PdfReader 

reader = PdfReader('/Users/sulaiman/Downloads/samplePDF.pdf') 
data = ""

for page_no in range(len(reader.pages)):
    page = reader.pages[page_no] 
    data += page.extract_text()

print(data)