Smart Email Organizer
A robust Python automation tool designed to declutter email inboxes using the IMAP protocol.
This project demonstrates how to programmatically interact with email servers to search, filter, and organize messages based on specific keywords (e.g., "unsubscribe", "newsletter"). 
It features a "Dry Run" safety mode to prevent accidental data loss.

 Key Features
Secure Authentication: Uses App Passwords and SSL encryption to ensure credentials remain safe.
IMAP Protocol Integration: Direct interaction with mail servers using Python's imaplib.
Efficient Filtering: server-side searching to minimize bandwidth usage (only fetches headers, not attachments).
Safety First: Includes a default "Dry Run" mode to preview actions before deletion.

Technologies Used
Language: Python 3.x
Libraries: imaplib, email, getpass
Protocols: IMAP (Internet Message Access Protocol), SSL/TLS

lone the Repository
git clone [https://github.com/yourusername/smart-email-organizer.git]
cd smart-email-organizer

2. Security Requirement: App Passwords
Critical: You cannot use your standard Gmail or Outlook login password due to modern security standards (OAuth2). You must generate an App Password.
Gmail Users:
Go to Google Account Settings.
Enable 2-Step Verification.
Search for "App Passwords".
Create a new one named "Python Script" and copy the 16-character code.

Outlook/Hotmail Users:
Go to Security Settings > Advanced Security Options.
Create a new App Password.

How to Run
Open your terminal or command prompt.
Navigate to the project folder.
Run the script:
python full_email_organizer.py
Follow the prompts:
Enter your Email Address.
Enter your App Password (Input will be hidden for security).
Enter the Keyword you want to clean up (e.g., unsubscribe).

To enable actual deletion/moving:
Open full_email_organizer.py in your code editor.
Scroll to the Action Section (around line 90).
Uncomment (remove the #) from the following lines:
# mail.copy(e_id, target_folder)
# mail.store(e_id, '+FLAGS', '\\Deleted')

How It Works (The Logic)
Connection: The script establishes an SSL connection to imap.gmail.com on port 993.
Handshake: It authenticates using the provided credentials.
Search: It sends a command to the server: SEARCH BODY "keyword".
Fetch (Optimized): It retrieves only the BODY.PEEK[HEADER] (Subject, Date, Sender) to avoid downloading large attachments, preventing timeouts.
Action: It iterates through the list of IDs and performs the user-defined action (Move/Delete).

Future Improvements
Add a Graphical User Interface (GUI) using Tkinter.
Implement a schedule to run automatically every Friday.
Add support for "Sender" based filtering (not just body keywords).


Go to Security Settings > Advanced Security Options.

Create a new App Password.
