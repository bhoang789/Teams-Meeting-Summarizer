import pytest
from src.file_handler import read_transcript


class TestFileHandler:
    """Test the file handling functionality"""
    
    def test_read_transcript_returns_text_from_docx(self, sample_transcript_docx):
        """
        Given a .docx transcript file exists,
        When read_transcript() is called with the file path,
        Then it returns the text content from the document
        """
        text_content = read_transcript(sample_transcript_docx)
        
        # Verify the function returns a string
        assert isinstance(text_content, str)
        
        # Verify content from the sample file is extracted
        assert "Teams Meeting Transcript" in text_content
        assert "Attendees" in text_content
        assert "Meeting Content" in text_content
    
    def test_read_transcript_preserves_paragraph_structure(self, sample_transcript_docx):
        """
        Given a .docx file with multiple paragraphs,
        When read_transcript() is called,
        Then it preserves the structure with newlines between paragraphs
        """
        text_content = read_transcript(sample_transcript_docx)
        
        # Should have multiple lines (paragraphs separated)
        lines = text_content.strip().split('\n')
        assert len(lines) > 1
    
    def test_read_transcript_with_nonexistent_file_raises_error(self):
        """
        Given a file path that doesn't exist,
        When read_transcript() is called,
        Then it raises an appropriate error
        """
        with pytest.raises((FileNotFoundError, IOError)):
            read_transcript("/nonexistent/path/file.docx")
