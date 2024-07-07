import re
import pypdf

class PDF:

    def __init__(self, pdf_bytes:bytes):
        # Atributos a serem criados para o objeto PDF
        [self.pages, self.page_count] = self.create_pages(pdf_bytes)
        self.summary= self.pages[0]
        # self.ano_dom: str = self.define_year_dom()
        # self.pages: list[str] = self.create_pdf_pages()
  

    # def define_year_dom(self)->str:
    #     ano_dom_regex = re.compile('ANO\s[X|I|V]+')
    #     ano_dom: str = ano_dom_regex.search(self.pdf_string).group()
    #     print("RegEx year defined!")
    #     return ano_dom

    # def define_page_count(self) -> int :
    #     page_count = self.pdf_string.count(self.ano_dom)
    #     print("Document page count defined!")
    #     return page_count

    def create_pages(self, pdf_bytes):
        pages: list[str] = []
        reader = pypdf.PdfReader(pdf_bytes)
        number_pages = reader.get_num_pages()
        for index in range(number_pages):
            pages.append(reader.pages[index].extract_text())
        return pages, number_pages
    
    # def create_pdf_pages(self) -> list[str]:
    #     summary_start: int = self.pdf_string.find('\n')
    #     first_ano_dom: int = self.pdf_string.find(self.ano_dom)
    #     summary_string: str = self.pdf_string[:first_ano_dom]
    #     length_of_summary: int = len(summary_string)
    #     reversed_summary_string: str = summary_string[::-1]
    #     page_count = str(self.page_count)
    #     page_count = page_count[::-1]
    #     page_count_length = len(page_count)
    #     reversed_summary_end = reversed_summary_string.find(page_count)
    #     summary_end = length_of_summary - reversed_summary_end + page_count_length -1


    #     summary = self.pdf_string[summary_start:summary_end]

    #     # excluindo o sumário do pdf_string
    #     pdf_string = self.pdf_string[summary_end::]
    #     # criando a lista de páginas
    #     pages = [summary]
    #     title = 'DIÁRIO OFICIAL DOSALVADOR-BAHIA'

    #     # criando a primeira página
    #     next_page = pdf_string.find(title)
    #     page = pdf_string[:next_page:]
    #     pages.append(page)
    #     pdf_string = pdf_string[next_page::]

    #     #rever isso################3
    #     # criando as próximas páginas, precisa inserir um deslocamento para ele não encontrar o começo da própria página
    #     for n in range(self.page_count - 3):
    #         next_page = pdf_string[10:].find(title)
    #         page = pdf_string[:next_page + 10:]
    #         pages.append(page)
    #         pdf_string = pdf_string[next_page + 10::]

    #     # última pagina
    #     pages.append(pdf_string)
    #     return pages