from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
import traceback
import requests
import json

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = "sk-rok"  # Replace with your actual key
JINA_RERANKER_URL = "https://api.jina.ai/v1/rerank"
JINA_API_KEY = "jina_ee32c8d9f5cb4a8ea2e3919666331fb2jijtSGniMqZ8maS9_l7Ho0EiTyksL"  # Replace with your actual Jina API key


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if "file" not in request.files:
                return jsonify({"error": "No file uploaded"}), 400

            file = request.files["file"]

            if file.filename.split(".")[-1].lower() != "pdf":
                return jsonify({"error": "Uploaded file is not a PDF"}), 400

            pdf_reader = PdfReader(file)
            raw_text = ""
            for page in pdf_reader.pages:
                content = page.extract_text()
                if content:
                    raw_text += content

            text_splitter = CharacterTextSplitter(
                separator="\n", chunk_size=800, chunk_overlap=200, length_function=len
            )
            texts = text_splitter.split_text(raw_text)

            embeddings = OpenAIEmbeddings()
            document_search = FAISS.from_texts(texts, embeddings)

            chain = load_qa_chain(OpenAI(), chain_type="stuff")

            query = request.form["query"]

            docs = document_search.similarity_search(query, k=5)

            text_list = [doc.page_content for doc in docs]
            reranked_results = jina_rerank(query, text_list)
            print(reranked_results)

            most_relevant_doc = docs[reranked_results["results"][0]["index"]]

            answer = chain.run(input_documents=[most_relevant_doc], question=query)

            return jsonify({"answer": answer})

        except Exception as e:
            app.logger.error(f"An error occurred: {str(e)}")
            app.logger.error(traceback.format_exc())
            return jsonify({"error": str(e)}), 500

    return render_template("index.html")


def jina_rerank(query: str, text_list: list):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer jina_ee32c8d9f5cb4a8ea2e3919666331fb2jijtSGiMqZ8maS9_l7Ho0EiTyksL",
    }

    json_data = {
        "model": "jina-reranker-v2-base-multilingual",
        "documents": text_list,
        "query": query,
        "top_n": 3,
    }

    response = requests.post(
        JINA_RERANKER_URL, headers=headers, data=json.dumps(json_data)
    )
    return response.json()


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
