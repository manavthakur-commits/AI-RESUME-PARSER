# 📃 AI-Powered Resume Data Extractor

An interactive web application built with Streamlit that leverages the Google Gemini API and Pydantic to reliably extract structured data (JSON) from unstructured resume text.

By utilizing the newly supported `response_schema` configuration in the Gemini API, this tool ensures the Large Language Model (LLM) strictly adheres to a predefined data structure, making it ideal for automated parsing pipelines, ATS systems, and AI-driven recruitment workflows.

---

# ✨ Features

## ✅ Reliable Structured Output
Uses Pydantic models to define an exact JSON schema for the LLM to follow, eliminating:
- Hallucinated keys
- Malformed JSON
- Inconsistent response structures

---

## ⚡ Powered by Gemini 2.5
Utilizes Google's highly efficient `gemini-2.5-flash-lite` model for:
- Fast inference
- Accurate extraction
- Low-latency parsing

---

## 🖥️ Interactive 3-Column Streamlit UI

### 📥 Input Panel
Paste raw resume text directly into the application.

### 📜 Schema Panel
View the dynamically generated JSON schema enforced by the model.

### 📤 Output Panel
Visualize:
- Parsed JSON response
- Extracted resume insights
- Candidate summary metrics

---

## 🎯 Targeted Resume Extraction

Automatically extracts:

- Candidate Name
- Email Address
- Technical Skills
- Professional Experience
  - Job Titles
  - Companies
  - Duration
  - Responsibilities

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| LLM Integration | google-genai SDK |
| Data Validation | Pydantic |
| Language | Python |
| Model | Gemini 2.5 Flash Lite |

---

# 📂 Project Structure

```bash
resume-data-extractor/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

# 🚀 Getting Started

## 📌 Prerequisites

Make sure you have:

- Python 3.8 or higher
- A valid Google Gemini API Key

You can generate an API key from Google AI Studio.

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/resume-data-extractor.git

cd resume-data-extractor
```

---

## 2️⃣ Create a Virtual Environment

### Mac/Linux

```bash
python -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install streamlit google-genai pydantic
```

Or install using:

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

You can provide your Gemini API key in two ways.

---

## Option 1: Environment Variable (Recommended)

### Mac/Linux

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Windows CMD

```cmd
set GEMINI_API_KEY=your_api_key_here
```

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

---

## Option 2: In-App API Input

If the environment variable is not found, the application will securely prompt you to enter the API key from the Streamlit sidebar.

---

# ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run main.py
```

The application will automatically open in your browser:

```bash
http://localhost:8501
```

---

# 🧠 How It Works

## 1️⃣ Schema Definition

Two Pydantic models define the required structure:

### `Experience`
Captures:
- Title
- Company
- Duration
- Responsibilities

### `ResumeData`
Captures:
- Name
- Email
- Skills
- Experience List

---

## 2️⃣ Prompt Engineering

The raw resume text is sent to Gemini along with instructions to extract structured information.

---

## 3️⃣ Structured Generation

The application passes the Pydantic schema directly into the Gemini configuration:

```python
response_schema=ResumeData
response_mime_type="application/json"
```

This constrains the model output to valid JSON matching the schema.

---

## 4️⃣ Visualization

Streamlit:
- Displays the generated schema
- Shows parsed JSON output
- Provides quick extraction insights

---

# 📌 Example Output

```json
{
  "name": "John Doe",
  "email": "john.doe@email.com",
  "skills": [
    "Python",
    "Machine Learning",
    "TensorFlow"
  ],
  "experience": [
    {
      "title": "Machine Learning Engineer",
      "company": "ABC Technologies",
      "duration": "2022 - Present",
      "responsibilities": [
        "Built ML pipelines",
        "Deployed AI models"
      ]
    }
  ]
}
```

---

# 🎯 Use Cases

- ATS Resume Parsing
- HR Automation
- Recruitment Platforms
- Candidate Skill Analysis
- Resume Intelligence Systems
- AI Hiring Pipelines

---

# 🔥 Why This Project Stands Out

Unlike traditional regex-based resume parsers, this project:

✅ Uses LLM-powered semantic understanding  
✅ Guarantees structured JSON output  
✅ Reduces parsing failures  
✅ Is easily extensible for production pipelines  
✅ Demonstrates modern AI engineering practices

---

# 📈 Future Improvements

- PDF Resume Upload Support
- OCR Integration
- LinkedIn Profile Parsing
- Multi-language Resume Support
- Resume Scoring Engine
- Vector Database Integration
- Candidate Ranking System

---

# 🤝 Contributing

Contributions are welcome.

Feel