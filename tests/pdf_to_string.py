from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import *


def pdf2str(pdf_file):
    pdf_rm = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(pdf_rm, retstr, laparams=laparams)
    process_pdf(pdf_rm, device, pdf_file)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content


def pdf2txt(file):
    #pdf = open(file,'rb')
    pdf_string = pdf2str(pdf_file=file)
    print("Start convertion PDF -> Text")
    #pdf.close()
    print("Done convertion PDF -> Text")
    return pdf_string