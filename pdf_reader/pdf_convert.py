import PyPDF2

pdfFileObj = open('example.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
text = ""

for i in range(num_pages):
    pageObj = pdfReader.getPage(i)
    text += pageObj.extractText()

print(text)