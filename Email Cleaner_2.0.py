import imaplib
import email
import getpass
import sys
IMAP_SERVER = 'imap.gmail.com'  
print("--- Email Organizer Setup ---")
EMAIL_USER = input("Enter your email address: ").strip()
try:
    EMAIL_PASS = getpass.getpass("Enter your App Password: ")
except Exception:
    print("(!) Hidden input failed. Switching to visible input.")
    EMAIL_PASS = input("Enter your App Password: ")
def connect_to_email():
    """
    Establishes a secure SSL connection to the IMAP server.
    Returns: The mail connection object if successful, None if failed.
    """
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)        
        mail.login(EMAIL_USER, EMAIL_PASS)
        print("[+] Logged in successfully.")
        return mail
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        print("    (Tip: Check if 2-Step Verification is on and you are using an App Password)")
        return None
def clean_inbox(mail, keyword, target_folder="[Gmail]/Trash"):
    """
    Searches Inbox for a keyword and moves matches to target_folder.
    """
    try:
        mail.select("inbox")        
        safe_keyword = keyword.replace('"', '').replace("'", "")
        print(f"[*] Searching for emails containing: '{safe_keyword}'...")        
        status, messages = mail.search(None, f'(BODY "{safe_keyword}")')
        if status != 'OK':
            print("[-] Search command failed.")
            return
        email_ids = messages[0].split()
        print(f"[*] Found {len(email_ids)} emails matching criteria.")
        if not email_ids:
            return
        for e_id in email_ids:
            try:
                _, msg_data = mail.fetch(e_id.decode(), '(BODY.PEEK[HEADER])')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = msg['subject']
                        if subject is None:
                            subject = "(No Subject)"
                        print(f"    - Found ID {e_id.decode()}: {subject[:50]}...")
                mail.copy(e_id, target_folder)
                mail.store(e_id, '+FLAGS', '\\Deleted')
            except Exception as loop_error:
                print(f"    [!] Error reading email ID {e_id.decode()}: {loop_error}")
                continue
        mail.expunge() 
        print(f"[+] Operation complete. Emails have been moved to {target_folder}.")
    except Exception as e:
        print(f"[-] Error during cleanup: {e}")
if __name__ == "__main__":
    connection = connect_to_email()
if connection:
        search_term = input("Enter keyword to search for (e.g., unsubscribe): ")
        clean_inbox(connection, search_term, target_folder="[Gmail]/Trash")        
        connection.logout()
