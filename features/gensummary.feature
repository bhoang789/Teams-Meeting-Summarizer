Feature: Generate summary from transcript

  As a person who wants to refer to past meetings
  I want to have a concise summary no longer than 2 pages
  that I can refer back to after a meeting ends.
  I would like the summary to contain a bullet list of the main points and a bullet list of tasks assigned
  Each bulllet can have a short subparagraph underneath
  I would like the beginning to have a list of all attendees/stakeholders
  Generate this summary in a Word document in the same directory as the transcript


  Scenario: Generating a meeting summary
    User will pass the file path to the program
    Program will pass file to the AI agent and generates a summary
    Text gets stored in a Word document
