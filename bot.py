from google import genai
from google.genai import types
def ai_response(message):
    sys_instruct="You are a healthcare bot , fix the problems by giving sugestion , medical advice. Your name is healthcarebot."
    client = genai.Client(api_key="AIzaSyA_4fFz_CBqlcNO4yDQ0KXXe5qgmR1MEiU")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            max_output_tokens=1000,
            system_instruction=sys_instruct),
        contents=[message]
    )
    return response.text