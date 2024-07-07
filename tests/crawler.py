from pdf_class import PDF
from retrieve_pdf import retrieve_pdf

def crawler(url):
    [dom_name, pdf_bytes] = retrieve_pdf(url)
    pdf = PDF(pdf_bytes)
    dom_name_reversed = dom_name[::-1]
    text_year_reversed = dom_name_reversed[0:4]
    text_month_reversed = dom_name_reversed[5:7]
    text_day_reversed = dom_name_reversed[8:10]
    text_year = int(text_year_reversed[::-1])
    text_month = int(text_month_reversed[::-1])
    text_day = int(text_day_reversed[::-1])

    document = {
        "text_year": text_year,
        "text_month": text_month,
        "text_day": text_day,
        "dom_name": dom_name,
        "page_count": pdf.page_count,
        "page_content": pdf.pages[1::],
        "full_summary": pdf.summary,
    }

    return dom_name, document