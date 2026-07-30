import smtplib
import time
from email.mime.text import MIMEText

# --- Configuration ---
# In a real scenario, these would be environment variables or a config file.
# For this example, we'll simulate a local mail server.
# We'll use Python's built-in smtplib for sending and a dummy server for receiving.

# Dummy SMTP server details (for receiving emails)
# In a real self-hosted MCP, this would be an IMAP/POP3 server.
# For this simulation, we'll just have a list of received emails.

# Dummy AI Agent Configuration
AGENT_EMAIL = "agent@example.com"
AGENT_PASSWORD = "agentpassword"

# Simulate a local mail server for the agent to 'read' from
# In a real setup, this would be an IMAP/POP3 server.
class DummyMailServer:
    def __init__(self):
        self.inbox = []

    def receive_email(self, sender, recipient, subject, body):
        self.inbox.append({
            "from": sender,
            "to": recipient,
            "subject": subject,
            "body": body
        })
        print(f"[Server] Received email from {sender} to {recipient}\n")

    def get_emails(self, recipient):
        # Simulate fetching emails for a specific recipient
        # In a real IMAP/POP3, this would involve authentication and fetching.
        # For simplicity, we'll just return all emails and let the agent filter.
        return self.inbox

# Simulate an AI Agent with an email inbox capability
class AIAgent:
    def __init__(self, email, password, mail_server):
        self.email = email
        self.password = password
        self.mail_server = mail_server
        self.sent_emails = []

    def send_email(self, recipient, subject, body):
        # In a real scenario, this would connect to an SMTP server.
        # For this simulation, we'll just log the sent email and add it to our history.
        print(f"[Agent] Sending email to {recipient} with subject: {subject}\n")
        self.sent_emails.append({
            "to": recipient,
            "subject": subject,
            "body": body
        })
        # Simulate sending to the dummy server for others to receive
        self.mail_server.receive_email(self.email, recipient, subject, body)

    def process_inbox(self):
        print(f"[Agent] Checking inbox for {self.email}...")
        emails = self.mail_server.get_emails(self.email)
        for email in emails:
            if email["to"] == self.email:
                print(f"[Agent] Processing email from {email['from']}: {email['subject']}\n")
                # Simulate a simple response logic
                if "hello" in email["body"].lower():
                    response_subject = f"Re: {email['subject']}"
                    response_body = "Hello there! I received your message."
                    self.send_email("user@example.com", response_subject, response_body)
                # In a real agent, this would involve LLM calls to understand and act.

# --- Simulation Setup ---

# Instantiate the dummy mail server
dummy_server = DummyMailServer()

# Instantiate the AI Agent
agent = AIAgent(AGENT_EMAIL, AGENT_PASSWORD, dummy_server)

# --- Demonstration ---

print("--- AI Agent Email Box Simulation ---\n")

# Simulate an incoming email to the agent's address
dummy_server.receive_email("user@example.com", AGENT_EMAIL, "Hello Agent", "Hello, can you help me with something?")

# Give the agent a moment to 'receive' and 'process'
time.sleep(1) # Simulate asynchronous processing delay

# Agent processes its inbox
agent.process_inbox()

print("\n--- Simulation Complete ---")
print(f"Agent sent {len(agent.sent_emails)} emails.")
