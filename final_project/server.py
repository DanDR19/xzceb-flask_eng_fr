from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods = ["GET"])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translator_obj = translator.Translator()
    translated = translator_obj.english_to_french(textToTranslate)
    render_template("index.html", translated_text = translated)
    return translated

@app.route("/frenchToEnglish", methods = ["GET"])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translator_obj = translator.Translator()
    translated = translator_obj.french_to_english(textToTranslate)
    render_template("index.html", translated_text = translated)
    return translated

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)
