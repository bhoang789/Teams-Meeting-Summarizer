import pytest
import json
from src.summary_generator import generate_summary


class TestSummaryGenerator:
    """Test the summary generation with Claude"""
    
    def test_generate_summary_returns_dict_with_required_fields(self, monkeypatch):
        """
        Given a transcript text,
        When generate_summary() is called,
        Then it returns a dict with attendees, main_points, and action_items
        """
        # Mock Claude API response
        mock_response = {
            'attendees': ['John Smith', 'Jane Doe', 'Bob Johnson'],
            'main_points': [
                {'topic': 'Q3 Planning', 'points': ['Focus on budget', 'Timeline is critical']},
                {'topic': 'Resources', 'points': ['Need 2 engineers', 'Budget allocation approved']}
            ],
            'action_items': [
                {'task': 'Budget review', 'owner': 'Jane', 'due_date': '2024-06-20'},
                {'task': 'Timeline planning', 'owner': 'Bob', 'due_date': '2024-06-19'}
            ]
        }
        
        monkeypatch.setattr('src.summary_generator.call_claude_api', 
                          lambda text: mock_response)
        
        transcript = "Meeting notes about Q3 planning and resources"
        result = generate_summary(transcript)
        
        assert isinstance(result, dict)
        assert 'attendees' in result
        assert 'main_points' in result
        assert 'action_items' in result
    
    def test_generate_summary_attendees_is_list(self, monkeypatch):
        """
        When generate_summary() is called,
        Then attendees should be a list of strings
        """
        mock_response = {
            'attendees': ['John Smith', 'Jane Doe'],
            'main_points': [],
            'action_items': []
        }
        
        monkeypatch.setattr('src.summary_generator.call_claude_api', 
                          lambda text: mock_response)
        
        result = generate_summary("Meeting transcript")
        
        assert isinstance(result['attendees'], list)
        assert all(isinstance(name, str) for name in result['attendees'])
    
    def test_generate_summary_main_points_has_topic_and_points(self, monkeypatch):
        """
        When generate_summary() is called,
        Then each main point should have 'topic' and 'points' fields
        """
        mock_response = {
            'attendees': [],
            'main_points': [
                {'topic': 'Budget Discussion', 'points': ['Point 1', 'Point 2']}
            ],
            'action_items': []
        }
        
        monkeypatch.setattr('src.summary_generator.call_claude_api', 
                          lambda text: mock_response)
        
        result = generate_summary("Meeting transcript")
        
        assert isinstance(result['main_points'], list)
        for point in result['main_points']:
            assert 'topic' in point
            assert 'points' in point
            assert isinstance(point['points'], list)
    
    def test_generate_summary_action_items_has_task_owner_due_date(self, monkeypatch):
        """
        When generate_summary() is called,
        Then each action item should have 'task', 'owner', and 'due_date'
        """
        mock_response = {
            'attendees': [],
            'main_points': [],
            'action_items': [
                {'task': 'Review budget', 'owner': 'Jane', 'due_date': '2024-06-20'}
            ]
        }
        
        monkeypatch.setattr('src.summary_generator.call_claude_api', 
                          lambda text: mock_response)
        
        result = generate_summary("Meeting transcript")
        
        assert isinstance(result['action_items'], list)
        for item in result['action_items']:
            assert 'task' in item
            assert 'owner' in item
            assert 'due_date' in item
