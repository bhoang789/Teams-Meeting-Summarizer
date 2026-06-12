from src.prompt_menu import prompt_user
from src.file_handler import read_transcript
from src.summary_generator import generate_summary
from src.summary_writer import write_summary_to_docx
import os
from pathlib import Path
import traceback


def main():
    """
    Main entry point for the CLI application.
    Displays the menu, handles user selection, and processes files.
    """
    while True:
        choice = prompt_user()
        
        if choice == 'upload':
            # Prompt user for file path
            file_path = input("Enter the path to the transcript file: ")
            
            try:
                # Read the transcript
                transcript_content = read_transcript(file_path)
                print(f"\n✓ Successfully read transcript ({len(transcript_content)} characters)")
                
                # Generate summary using Gemini
                print("\n⏳ Generating summary with Gemini API...")
                summary = generate_summary(transcript_content)
                print("✓ Summary generated")
                
                # Write summary to .docx
                input_path = Path(file_path)
                output_filename = f"{input_path.stem}_summary.docx"
                output_path = input_path.parent / output_filename
                
                write_summary_to_docx(summary, str(output_path))
                print(f"✓ Summary saved to: {output_path}\n")
                
            except FileNotFoundError as e:
                print(f"\n✗ Error: {e}\n")
                print(f"Full traceback:\n{traceback.format_exc()}")
            except ValueError as e:
                print(f"\n✗ Error: {e}\n")
                print(f"Full traceback:\n{traceback.format_exc()}")
            except Exception as e:
                print(f"\n✗ Unexpected error: {e}\n")
                print(f"Full traceback:\n{traceback.format_exc()}")
        
        elif choice == 'exit':
            print("Exiting program")
            break


if __name__ == '__main__':
    main()
