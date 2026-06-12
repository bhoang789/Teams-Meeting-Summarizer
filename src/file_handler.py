from docx import Document
from pathlib import Path


def read_transcript(file_path):
    """
    Read a Teams meeting transcript from a .docx file.
    
    Args:
        file_path (str): Path to the .docx file
    
    Returns:
        str: The text content extracted from the document
    
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is not a valid .docx file
    """
    # Check if file exists
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Load the document
        doc = Document(file_path)
        
        # Extract all paragraph text
        text_content = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():  # Only add non-empty paragraphs
                text_content.append(paragraph.text)
        
        # Join paragraphs with newlines
        return '\n'.join(text_content)
    
    except Exception as e:
        raise ValueError(f"Error reading .docx file: {str(e)}")
