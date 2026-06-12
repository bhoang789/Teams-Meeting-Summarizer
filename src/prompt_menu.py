def prompt_user():
    """
    Display the menu and prompt the user for their choice.
    
    Returns:
        str: 'upload' if user selects 1, 'exit' if user selects 2
    """
    while True:
        menu = """
1. Upload a file
2. Exit
"""
        print(menu)
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            return 'upload'
        elif choice == '2':
            return 'exit'
        else:
            print("Invalid choice. Please try again.")
