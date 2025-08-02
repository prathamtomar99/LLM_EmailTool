from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv  # Fixed import
from langchain_community.agent_toolkits import GmailToolkit 
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain_google_community.gmail.send_message import GmailSendMessage
import re
load_dotenv()

credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)

gmail_tool = GmailSendMessage(api_resource=api_resource)

toolkit = GmailToolkit()
llm = ChatGroq(model = 'deepseek-r1-distill-llama-70b')

def define_email(email_id, name, subject, message):
    email_details = {
        "to": [email_id],  # Correctly formatted email recipient list
        "subject": subject,
        "message": f"""
            <html>
                <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; margin: 0; padding: 0;">
                    <div style="border: 2px solid #333333; margin: 20px auto; max-width: 620px; border-radius: 12px;">
                        <table align="center" width="600" style="border-spacing: 0; border-collapse: collapse; background-color: #ffffff; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
                            <tr>
                                <td style="background-color: #2b2b2b; color: #ffffff; padding: 20px; text-align: center; border-top-left-radius: 10px; border-top-right-radius: 10px;">
                                    <img src="https://drive.google.com/uc?export=view&id=11h8n4DhwvnhhymYm4v993Z5KAJ3NDyM4" 
                                        alt="IEEE Logo" 
                                        style="width:250px;height:auto;">
                                    <h1>Welcome to IEEE!</h1>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; color: #333333; line-height: 1.6;">
                                    <p>Dear {name},</p>
                                    <p>{message}</p>
                                    <p style="margin-bottom: 25px;"></p>
                                    <p style="text-align: center;">
                                        <strong>This was brought to you by our own AI Agent.</strong><br>
                                        Join us to learn how to automate tasks like this.
                                    </p>
                                </td>
                            </tr>
                            <tr>
                                <td style="background-color: #f1f1f1; padding: 20px; text-align: center; color: #4d4b4b;">
                                    <p>Connect with us on Instagram:</p>
                                    <p>
                                        <a href="https://instagram.com/ieee_vit_studentbranch" 
                                        target="_blank" 
                                        style="color: #004080; text-decoration: none; font-weight: bold;">
                                            @ieee_vit_studentbranch
                                        </a>
                                    </p>
                                    <p style="font-size: 12px;">If you have any questions, feel free to 
                                        <a href="mailto:ieee.sb@vit.edu" style="color: #004080; text-decoration: none; font-weight: bold;">
                                            contact us
                                        </a>.
                                    </p>
                                    <p>We look forward to welcoming you!</p>
                                    <p>Best regards,</p>
                                    <p><strong>The IEEE Team</strong></p>
                                </td>
                            </tr>
                        </table>
                    </div>
                </body>
            </html>
        """
    }

    result = gmail_tool.run(email_details)
    print(result)
    return result

def is_valid_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# @tool(name="send_email", description="Send an email using Gmail API to a valid email address.")
@tool
def send_email(email_id: str, name: str, subject: str, message: str):
    '''Use this tool ONLY when the user explicitly asks to send an email AND provides all required information.
    
    Parameters:
    email_id (str): Valid email address of the receiver (must contain @ symbol)
    name (str): Name of the receiver
    subject (str): Subject line for the email
    message (str): The message content for the receiver
    
    IMPORTANT: Only use this tool when:
    1. User explicitly requests to send an email
    2. All parameters are provided and valid
    3. email_id contains a valid email format with @ symbol
    '''
    print("\n\nNow will call tool\n\n")
    # Validate inputs before proceeding
    if not email_id or not email_id.strip():
        return "Error: Email address is required and cannot be empty"
    
    if not is_valid_email(email_id.strip()):
        return f"Error: '{email_id}' is not a valid email address format"
    
    if not name or not name.strip():
        return "Error: Recipient name is required and cannot be empty"
    
    if not subject or not subject.strip():
        return "Error: Email subject is required and cannot be empty"
    
    if not message or not message.strip():
        return "Error: Email message is required and cannot be empty"
    
    print(f"Sending mail to {email_id.strip()} for {name.strip()}")
    
    try:
        result = define_email(email_id.strip(), name.strip(), subject.strip(), message.strip())
        return f"Email sent successfully to {email_id.strip()}"
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return f"Failed to send email: {str(e)}"
    
# if __name__ == "__main__":
#     result = send_email.invoke({
#         "email_id": "partham68209@gmail.com",
#         "name": "John Doe", 
#         "subject": "Test Subject",
#         "message": "Hello, this is a test message!"
#     })
#     print(result)