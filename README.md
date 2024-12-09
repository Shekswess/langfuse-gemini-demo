# langfuse-gemini-demo
This is a demo app for the `Gemini Chat Assistant` mainly to showcase how to use [Langfuse](https://langfuse.com) in combination with [Google Generative AI](https://ai.google.dev/gemini-api/docs/models/gemini) or any other LLM provider.

## 🛠️ Usage

1. Clone the repository
```bash
git clone https://github.com/langfuse/langfuse-gemini-demo.git
```

2. Make sure you have installed [uv](https://docs.astral.sh/uv/)

3. Install Python for the project
```bash
uv install python
```

4. Install all the dependencies
```bash
uv sync --all-extras
```

5. Create and fill the `.env` file
```bash
cp .env.example .env
```

6. Run the application
```bash
uv run streamlit run app.py
```

## 🖼️ Showcase
![image](https://github.com/user-attachments/assets/2ff4252b-0e33-4a0c-af55-4e0b66635bac)


## 🗂️ Repository Structure
```plaintext
.
├── .env                                    # Environment variables       
├── .pre-commit-config.yaml                 # Configuration for pre-commit
├── .python-version                         # Python version
├── app.py                                  # Streamlit app  
├── LICENSE                                 # License
├── pyproject.toml                          # Configuration for the project (uv, ruff)
├── README.md                               # This file
└── uv.lock                                 # Lock file for uv
```
