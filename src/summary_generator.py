import os
import json
import logging
from pathlib import Path
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging to debug folder
debug_folder = Path(__file__).parent.parent / 'debug'
debug_folder.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(debug_folder / 'summary_generator.log'),
        logging.StreamHandler()  # Also print to console
    ]
)
logger = logging.getLogger(__name__)


def call_claude_api(transcript_text):
    """
    Call Gemini API through genai.mil endpoint to generate summary from transcript.
    
    Args:
        transcript_text (str): The meeting transcript text
    
    Returns:
        dict: Summary data with attendees, main_points, and action_items
    """
    # Configure API
    api_key = os.getenv('GENAI_API_KEY')
    if not api_key:
        raise ValueError("GENAI_API_KEY environment variable not set")
    
    client = openai.OpenAI(
        base_url="https://api.genai.mil/v1",
        api_key=api_key
    )
    
    prompt = """Analyze the following meeting transcript and extract:
1. List of attendees/stakeholders
2. Main points discussed (grouped by topic)
3. Action items with owner and due date

Respond with ONLY a valid JSON object (no other text) in this exact format:
{{
    "attendees": ["Name 1", "Name 2"],
    "main_points": [
        {{"topic": "Topic Name", "points": ["point 1", "point 2"]}},
        {{"topic": "Another Topic", "points": ["point 1"]}}
    ],
    "action_items": [
        {{"task": "Task description", "owner": "Owner Name", "due_date": "YYYY-MM-DD"}},
        {{"task": "Another task", "owner": "Owner Name", "due_date": "YYYY-MM-DD"}}
    ]
}}

Meeting Transcript:
{transcript}
""".format(transcript=transcript_text)
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    response_text = response.choices[0].message.content.strip()
    
    # Log the response
    logger.debug(f"Gemini API Response:\n{response_text}")
    
    # Try to parse JSON from the response
    try:
        # First, try to parse the entire response as JSON
        try:
            result = json.loads(response_text)
            logger.info("Successfully parsed JSON response")
            return result
        except json.JSONDecodeError as e1:
            logger.warning(f"Full JSON parse failed: {e1}")
            # If that fails, look for JSON within the response
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = response_text[json_start:json_end]
                logger.debug(f"Extracted JSON substring:\n{json_str}")
                result = json.loads(json_str)
                logger.info("Successfully parsed JSON from substring")
                return result
            else:
                raise json.JSONDecodeError("No JSON found in response", response_text, 0)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error: {e}")
        logger.error(f"Full response text:\n{response_text}")
        # Save full response to debug file for inspection
        with open(debug_folder / 'gemini_response.txt', 'w') as f:
            f.write(f"Error: {e}\n\n")
            f.write(f"Response text:\n{response_text}")
        # Fallback response if parsing fails
        return {
            'attendees': [],
            'main_points': [],
            'action_items': []
        }


def generate_summary(transcript_text):
    """
    Generate a structured summary from a meeting transcript.
    
    Args:
        transcript_text (str): The meeting transcript text
    
    Returns:
        dict: Summary with structure:
            {
                'attendees': list of names,
                'main_points': list of dicts with 'topic' and 'points' keys,
                'action_items': list of dicts with 'task', 'owner', 'due_date' keys
            }
    """
    return call_claude_api(transcript_text)
