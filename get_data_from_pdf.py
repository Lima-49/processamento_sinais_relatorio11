import fitz

def pdf2image(filename, no_page, outname):
    pdf_document = fitz.open(filename)
    page = pdf_document[no_page]
    image = page.get_pixmap()
    image.save(outname)
    pdf_document.close()
    result = f'Success save page {str(no_page)} + from {filename} to {outname}'
    return result

