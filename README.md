# llm-rag-api
LLM + RAG-Based Function Execution API using FastAPI
# LLM + RAG-Based Function Execution API

This project implements an API that integrates a Large Language Model (LLM) with a Retrieval-Augmented Generation (RAG) system to dynamically execute automation functions on a Windows machine.

## 🚀 Features
- Execute system functions dynamically (open applications, get system info, take screenshots, etc.)
- Uses FastAPI for API development
- Implements function calling using LLM + RAG approach

---
## 📌 Prerequisites
Ensure you have the following installed on your system:

- Python (>=3.8)
- Virtual Environment (Recommended)

---
## 🔧 Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/llm-rag-api.git
   cd llm-rag-api
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On MacOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---
## 📜 Dependencies
The project uses the following Python libraries:
- `fastapi` - Web framework for the API
- `uvicorn` - ASGI server to run the FastAPI app
- `pyautogui` - For GUI automation
- `psutil` - System information utilities
- `requests` - For making API calls
- `pillow` - Required for PyAutoGUI to take screenshots
- `pyscreeze` - Used internally by PyAutoGUI

---
## ▶️ Running the API
To start the FastAPI server, run:
```bash
uvicorn main:app --reload
```
The API will be available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---
## 🔥 API Usage
### 1️⃣ List Available Functions
**Endpoint:** `GET /list-functions`
```bash
curl -X 'GET' 'http://127.0.0.1:8000/list-functions' -H 'accept: application/json'
```

### 2️⃣ Execute a Function
**Endpoint:** `POST /execute`
#### Example Request (JSON):
```json
{
  "function_name": "open_chrome",
  "arguments": {}
}
```
**Curl Command:**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/execute' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"function_name": "open_chrome", "arguments": {}}'
```

---
## 🛠️ Troubleshooting
### "PyAutoGUI was unable to import pyscreeze" Error
Run:
```bash
pip install pyscreeze pillow
```

### "ModuleNotFoundError: No module named 'path'"
Ensure you installed all dependencies:
```bash
pip install -r requirements.txt
```


