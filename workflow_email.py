def summarize_note(note):
    return note
def generate_email(summary):
    return f"""
Subject: Great speaking with you!

Hi,

Thank you for the meeting. Based on our discussion, I understand that you are interested in {summary}.

We would love to help you further. Let me know a good time to connect again.

Best regards,
Sales Team
"""

note = "pricing and product demo"

summary = summarize_note(note)
email = generate_email(summary)

print(email)