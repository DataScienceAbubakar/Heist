import requests
from msal import ConfidentialClientApplication

# Replace these with your Azure AD app credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
TENANT_ID = "your_tenant_id"

# Microsoft Graph API endpoints
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"
 
def get_access_token():
    """Authenticate and get an access token."""
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=SCOPES)
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("Could not acquire access token.")

def create_email(access_token, subject, body, recipient):
    """Create and send an email using Microsoft Graph API."""
    url = f"{GRAPH_API_ENDPOINT}/me/sendMail"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    email_data = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body,
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": recipient,
                    }
                }
            ],
        },
        "saveToSentItems": "true",
    }
    response = requests.post(url, headers=headers, json=email_data)
    if response.status_code == 202:
        print("Email sent successfully.")
    else:
        print(f"Failed to send email: {response.status_code}, {response.text}")

if __name__ == "__main__":
    try:
        token = get_access_token()
        subject = "Test Email"
        body = "This is a test email sent using Microsoft Graph API."
        recipient = "recipient@example.com"
        create_email(token, subject, body, recipient)
    except Exception as e:
        print(f"Error: {e}")