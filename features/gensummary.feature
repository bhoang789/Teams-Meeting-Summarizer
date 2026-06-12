Feature: Generate summary from transcript when upload file is selected in the prompt menu

  As a person who wants to refer to past meetings
  I want to have a concise summary no longer than 2 pages
  that I can refer back to after a meeting ends.
  I would like the summary to contain a bulleted list of the main points and a bulleted list of tasks assigned (action items)
  Each bullet can have a short subparagraph underneath
  I would like the beginning to have a list of all attendees/stakeholders
  Generate this summary in a Word document in the same directory as the transcript


  Scenario: Generating a meeting summary
    User will pass the file path to the program either by typing or dragging and dropping the file into terminal
    Program will pass file to the AI agent and generates a summary
    Output text gets stored in a Word document in the same directory as the input file



Story 1 — Upload a Teams Meeting Transcript Document
As a meeting member, 
I want to upload a teams meeting transcript .docx file to the app, 
So that it can generate a summary document no longer than 2-pages of the main points discussed, and the action items that need to be addressed

Acceptance Criteria
Given there is a Teams meeting transcript document in the working directory, 
When the file is read by the application, 
Then the system generates a new summary document containg the main points and action items
