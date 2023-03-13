import os
import openai
from flask import Flask, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.json["content"]
        MODEL = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": generate_prompt(text)},
            ],
            temperature=1,
        )
        return {'reply':response['choices'][0]['message']['content']}
    else:
        return {'reply':"hello"}

def generate_prompt(text):
    return text
