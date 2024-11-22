# PDF Query System

This project provides a user-friendly web application that allows you to query PDF documents using natural language. It leverages the power of OpenAI's language models and Jina AI's Reranker to provide accurate and relevant answers to your questions.

## Features

- **Intuitive Interface:** Upload a PDF and ask questions in plain English.
- **Accurate Answers:** Utilizes advanced AI models for accurate information extraction.
- **Relevance Ranking:** Jina AI's Reranker ensures the most relevant answers are presented.
- **Visually Appealing UI:** Modern and user-friendly design for a better experience.
- **Easy to Use:** Simple and straightforward workflow for quick results.

Made with Guidance of Ved Prakash Chaubey

## How It Works

1. **Upload:** Upload your PDF document.
2. **Query:** Enter your question in the text input field.
3. **Process:** The application processes the PDF and uses AI to extract relevant information.
4. **Answer:** The most relevant answer to your query is displayed.

## Technologies Used

- **Python:** Core programming language.
- **Flask:** Web framework for building the application.
- **OpenAI:** Language models for understanding and answering queries.
- **Jina AI:** Reranker for improving the relevance of search results.
- **PyPDF2:** Library for reading PDF documents.
- **LangChain:** Framework for building language model applications.
- **FAISS:** Library for efficient similarity search (used temporarily for local development).
- **Bootstrap:** CSS framework for styling the UI.
- **HTML, CSS, JavaScript:** Front-end technologies for the user interface.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/pdf-query-system.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd pdf-query-system
   ```

3. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up API keys:**
   * Open the `app.py` file in a text editor.
   * Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.
   * Replace `YOUR_JINA_API_KEY` with your actual Jina AI API key.
   * Save the `app.py` file.

6. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

1. **Access the application:** Open your web browser and go to `http://127.0.0.1:5000/` (or the address where your Flask app is running).
2. **Upload a PDF document:** Click on the "Choose File" button and select the PDF file you want to query.
3. **Enter your query:** Type your question or query related to the content of the PDF in the text input field.
4. **Submit:** Click the "Submit" button.
5. **View the answer:** The answer to your query will be displayed below the form.

## Troubleshooting

* If you encounter errors, check the terminal or command prompt for error messages.
* Double-check that you've correctly replaced the placeholder API keys in `app.py` with your actual OpenAI and Jina AI API keys.
* Ensure that all required packages are installed correctly.

## Future Enhancements

* **Persistent Vector Database:** Replace FAISS with a persistent vector database like Pinecone or Weaviate for production use.
* **Enhanced UI:** Further improvements to the user interface and design.
* **Support for More File Types:** Extend support to handle other document formats.
* **Advanced Analytics:** Provide insights into the query results and document understanding.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
