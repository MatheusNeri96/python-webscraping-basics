from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from json2html import *
from .crawler import crawler
from pymongo import MongoClient

app = FastAPI()
client: MongoClient = MongoClient()
db = client['diaries']
collection = db["salvador"]
url = "http://www.dom.salvador.ba.gov.br/"


@app.get("/diaries/create_pdf_files")
def create_dom():
    [dom_name, document] = crawler(url)
    to_search = {"dom_name": dom_name}
    if db['salvador'].find_one(to_search):
        return {'message': 'The DOM was NOT inserted because it already exists in the Database'}
    else:
        post_id = db['salvador'].insert_one(document).inserted_id
        print(f'The DOM was inserted and the id on the DB is: {post_id}')
        return {'message': f'The DOM was inserted and the id on the DB is: {post_id}'}


@app.get("/diaries/get_pdf_files")
def read_dom():
    json_finding = collection.find_one()
    html_content: str = json2html.convert(json = json_finding)
    return HTMLResponse(content=html_content)