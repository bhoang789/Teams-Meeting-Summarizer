import pytest
from src.prompt_menu import prompt_user


class TestPromptUser:
    """Test user interaction with the menu"""
    
    def test_prompt_user_displays_menu(self, monkeypatch, capsys):
        """
        Given prompt_user is called,
        When the menu is displayed,
        Then the menu should be printed to stdout
        """
        monkeypatch.setattr('builtins.input', lambda _: '1')
        prompt_user()
        captured = capsys.readouterr()
        assert "1" in captured.out
        assert "2" in captured.out
    
    def test_prompt_user_option_1_returns_upload(self, monkeypatch):
        """
        Given the user enters 1,
        When prompt_user is called,
        Then it should return 'upload'
        """
        monkeypatch.setattr('builtins.input', lambda _: '1')
        result = prompt_user()
        assert result == 'upload'
    
    def test_prompt_user_option_2_returns_exit(self, monkeypatch):
        """
        Given the user enters 2,
        When prompt_user is called,
        Then it should return 'exit'
        """
        monkeypatch.setattr('builtins.input', lambda _: '2')
        result = prompt_user()
        assert result == 'exit'
    
    def test_prompt_user_invalid_input_reprompts(self, monkeypatch):
        """
        Given the user enters an invalid option,
        When prompt_user is called,
        Then it should reprompt until valid input is received
        """
        # Simulate: invalid input, then valid input
        inputs = iter(['3', '1'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = prompt_user()
        assert result == 'upload'
