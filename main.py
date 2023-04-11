# - *- coding: utf- 8 - *-
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)

def get_name(code):
    try:
        url = f"https://go-upc.com/search?q={code}"
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        name = soup.find("h1", attrs={"class":"product-name"}).text
        return name.strip()
    except: return "No info about code"

@app.route('/api')
def info():
    return "API get started"

@app.route('/api/info', methods=['POST'])
def get_data():
    try:
        data = request.get_json()
        code = data['code']
        print(code)
        name = get_name(code)
        return jsonify({"name":name})
    except Exception as exp: return str(exp)

if __name__ == "__main__":
    app.run()