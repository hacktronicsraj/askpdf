from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
import traceback

app = Flask(__name__)

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "sk-123"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Check if a file was uploaded
            if "file" not in request.files:
                return jsonify({"error": "No file uploaded"}), 400

            file = request.files["file"]

            # Check if the file is a PDF
            if file.filename.split(".")[-1].lower() != "pdf":
                return jsonify({"error": "Uploaded file is not a PDF"}), 400

            # Read the PDF
            pdf_reader = PdfReader(file)
            raw_text = ""
            for page in pdf_reader.pages:
                content = page.extract_text()
                if content:
                    raw_text += content

            # Split the text
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=800,
                chunk_overlap=200,
                length_function=len,
            )
            texts = text_splitter.split_text(raw_text)

            # Create embeddings and document search
            embeddings = OpenAIEmbeddings()
            document_search = FAISS.from_texts(texts, embeddings)

            # Load QA chain
            chain = load_qa_chain(OpenAI(), chain_type="stuff")

            # Get the query from the form
            query = request.form["query"]

            # Perform the search and get the answer
            docs = document_search.similarity_search(query)
            answer = chain.run(input_documents=docs, question=query)

            return jsonify({"answer": answer})

        except Exception as e:
            app.logger.error(f"An error occurred: {str(e)}")
            app.logger.error(traceback.format_exc())
            return jsonify({"error": str(e)}), 500

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
