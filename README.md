**📃 AI-Powered Resume Data Extractor**

An interactive web application built with Streamlit that leverages the Google Gemini API and Pydantic to reliably extract structured data (JSON) from unstructured, raw resume text.

By utilizing the newly supported response_schema configuration in the Gemini API, this tool ensures the Large Language Model (LLM) strictly adheres to a predefined data structure, making it perfect for automated parsing pipelines.

**✨ Features**

Reliable Structured Output: Uses Pydantic to define an exact JSON schema for the LLM to follow, eliminating hallucinated keys or malformed JSON.

Powered by Gemini 2.5: Utilizes the highly efficient gemini-2.5-flash-lite model for fast and accurate data extraction.

Interactive 3-Column UI: * Input: Paste raw resume text.

Schema: View the dynamically generated JSON schema the model must follow.

Output: View the fully parsed JSON payload and a quick summary of extracted metrics.

Targeted Extraction: Automatically parses the candidate's Name, Email, a comprehensive list of Skills, and detailed Professional Experience (including titles, companies, durations, and responsibilities).

**🛠️ Tech Stack**

Frontend: Streamlit

LLM Integration: google-genai (Official Google GenAI SDK)

Data Validation: Pydantic

Language: Python

**🚀 Getting Started**

Prerequisites
Python 3.8 or higher installed on your machine.

A valid Google Gemini API Key. You can get one from Google AI Studio.

Installation
Clone the repository (or create a new directory and save the main.py file).

Create a virtual environment (recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the required dependencies:

Bash
pip install streamlit google-genai pydantic
Configuration
You can provide your Gemini API key in two ways:

Option 1: Environment Variable (Recommended)
Export the key in your terminal before running the app:

Bash
export GEMINI_API_KEY="your_api_key_here"
Option 2: In-App Input
If the environment variable is not found, the app will gracefully prompt you to enter your API key securely via the Streamlit sidebar.

Running the App
Execute the following command in your terminal:

Bash
streamlit run main.py
The application will launch in your default web browser at http://localhost:8501.

**🧠 How It Works**  

Schema Definition: Two Pydantic models (Experience and ResumeData) define the exact shape, types, and descriptions of the data we want to extract.

Prompting: The raw resume text is passed to the Gemini API alongside a prompt instructing it to parse the data.

Structured Generation: The Pydantic model is passed into the Gemini client's config under response_schema, with response_mime_type set to application/json. This physically constrains the model's output to match the required format.

Display: Streamlit captures the text, updates the session state, and visualizes the structured JSON output alongside the expected schema.
