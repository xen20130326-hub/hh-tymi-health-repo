import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from AI.env
env_path = os.path.join(os.path.dirname(__file__), "../AI.env")
load_dotenv(env_path)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_triage_analysis(patient_data):
    """
    Analyzes patient symptoms and vitals using Groq AI.
    Returns a dictionary of detailed medical analysis.
    """
    prompt = f"""
    Analyze the following patient data for nurse triage and provide a detailed health plan:
    Name: {patient_data.get('name')}
    Age: {patient_data.get('age')}
    Weight: {patient_data.get('weight')}kg
    Height: {patient_data.get('height')}cm
    Blood Pressure: {patient_data.get('bp')}
    Allergies: {patient_data.get('allergies')}
    Symptoms: {patient_data.get('symptoms')}

    Provide the following details in JSON format:
    1. triage_status: (Red, Orange, Yellow, Green)
    2. recommendation: A brief overall advice.
    3. illness: Potential illness or disease based on symptoms.
    4. scan_reports: Recommended scan reports or tests to be done.
    5. medicines: Suggested over-the-counter medicines or categories.
    6. nutrition: Food meals, composition, and nutrition advice.
    7. hydration: Specific hydration needs.
    8. rest: Rest and sleep recommendations.
    9. avoid: Things to avoid (foods, activities, etc.).
    10. special_notes: Any other important medical notes.

    Respond ONLY with a valid JSON object.
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional medical assistant. Provide accurate and structured health advice in JSON format."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"}
        )
        response_json = json.loads(chat_completion.choices[0].message.content)
        return response_json
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return {
            "triage_status": "Yellow",
            "recommendation": "AI analysis unavailable. Please consult a doctor.",
            "illness": "Unknown",
            "scan_reports": "Consult doctor for required tests.",
            "medicines": "Consult pharmacist.",
            "nutrition": "Maintain balanced diet.",
            "hydration": "Drink plenty of water.",
            "rest": "Get adequate rest.",
            "avoid": "Avoid strenuous activity.",
            "special_notes": "Please visit a clinic for physical examination."
        }
