import os
import json
import streamlit as st
from google import genai
from pydantic import BaseModel, Field
from typing import List,Dict, Any

# Define the structured output schema using pydantic

class Experience(BaseModel):
    
    title: str = Field(description = "The professional job title held")
    company: str = Field(description = "The name of the company")
    duration: str = Field(description = "The time period worked(e.g.,'Jan 2020 - Dec2023)")
    responsibilities: List[str] = Field(description = "A list of 3-5 key responsibilities or achievements")
    
class ResumeData(BaseModel):
    
    name: str = Field(description = "The full name of the candidate.")
    email: str = Field(description = "The primary email address.")
    skills: List[str] = Field(description = "A list of 10-15 core techinical and soft skills.")
    experience: List[Experience] = Field(description = "A list of all professional experiences.")
    

# Gemini Extraction Funciton

def extract_resume_data(resume_text: str, api_key: str) -> str:
    
    """
    Uses the Gemini API to extract structured resume data from unstructured text.
    
    Args:
        resume_text: Raw unstructured text from the resume.
        api_key: Your Gemini API key for authentication.

    Returns:
        A JSON string containing the structured resume data or an error message.
    """
    
    
    if not api_key:
        return json.dumps({"error": "Gemini API key is not set."}, indent = 2)
    
    try:
        client = genai.Client(api_key = api_key)
        
        prompt = (
            "Parse the following resume text. Extract all the information into the"
            "required JSON structure. Focus specifically on extracting a comprehensive"
            "list of 'skills', and a detailed list of 'experience' entries."
             
        )
        
        response = client.models.generate_content(
        
            model = "gemini-2.5-flash-lite",
            contents = [prompt, resume_text],
            config = {
                
                'response_mime_type': 'application/json',
                'response_schema': ResumeData,
                'temperature': 0.1,
                
            }
            
        )
        
        return response.text
    except Exception as e:
        
        return json.dumps({"error": f"An API error occurred: {e}"}, indent = 2)
    
    
# Streamlit Application Layout

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    
    st.warning("GEMINI_API_KEY environment variable not found. Please set it first.")
    
    # Allow user input if not set (for demonstration purposes)
    
    GEMINI_API_KEY = st.sidebar.text_input("Enter your Gemini API Key:", type = "password")
    
    st.set_page_config(page_title = "Resume Data Extractor", layout = "wide")
    
    st.title("📃 AI-Powered Resume Data Extractor")
    
    st.markdown("Use the Gemini API with a Pydantic schema to reliably extract structured data from unstructured text.")
    
EXAMPLE_RESUME = """
John Doe
(555) 123-4567 | john.doe@email.com | London, UK

Summary 
Highly driven software engineer with 5+ years of experience developing scalable web applications and working across the full stack. Proficient in Python, JavaScript, and cloud technologies.

Skills
Python, Django, JavaScript, React, Node.js, AWS, Docker, Kubernetes, SQL, NoSQL, Git, Agile Methodologies.

Professional Experience
Senior Software Engineer at Innovatech Solutions
Jan 2022 - Present
- Led a team of 5 engineers to develop a cloud-based inventory management system, improving efficiency by 30%.
- Implemented CI/CD pipelines using Jenkins and Docker, reducing deployment time by 50%.
-Developed and maintained RESTful APIs using Django, serving over 10,000 daily users.

Software Engineer at TechGen Corp
Aug 2018 - Dec 2021
- Designed and built new features for customer faciing portal using Flask and React.
- Managed PostgreSQL database schemas and optimized complex queries.

"""

# Create three columns for the layout

col1, col2, col3 = st.columns(3)

with col1:
    # Input section
    st.header("1. Unstructured Resume Text") 
    resume_input = st.text_area("Paste the raw text of resume here",
                                EXAMPLE_RESUME,
                                height = 400)
    
    if st.button("🎯Extract Data"):
        if not resume_input:
            st.error("Please place some resume text to proceed.")
    elif not GEMINI_API_KEY:
        st.error("Please enter your Gemini API key to proceed.")
    else:
        with st.spinner("Processing with Gemini..."):
            
            # Call the extraction function
            json_output_text = extract_resume_data(resume_input, GEMINI_API_KEY)
            
            #Store the result in session state for other columns to access
            st.session_state["json_output"] = json_output_text
        
with col2:
    # Required JSON Schema
    st.header("2. Required JSON Schema")
    st.markdown("This is the exact structure the Gemini model is instructed to follow.")
    
    # Generate the JSON schema from the Pydantic model for display
    schema_dict = ResumeData.model_json_schema()
    
    # We use st.json for a nicely formatted, expandable view
    st.json(schema_dict)
    
    
with col3:
    # Output Response Section
    st.header("3. Extracted JSON Output")
    st.markdown("The final structured output from the Gemini API.")
    
    # Retrieve the JSON output from session state
    output_text = st.session_state.get('json_output', 'Click "Extract Data" to see the results here.')
    
    if output_text.startswith("{"):
        # If it is valid JSON, parse it for display
        output_dict = json.loads(output_text)
        st.json(output_dict)
        
        # Additional section to display specific extracted fields
        st.subheader("Extracted Key Data")
        if "skills" in output_dict:
            st.success(f"**Skills Found:** {len(output_dict['skills'])}")
            st.markdown(f"**Top Skills:** {','.join(output_dict['skills'][:5])}")
        
        if 'experience' in output_dict:
            st.info(f"**Experience Entries:** {len(output_dict['experience'])}")
        
    else:
        # Display the error message
        st.code(output_text, language = "json")    
