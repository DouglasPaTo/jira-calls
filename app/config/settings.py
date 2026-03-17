import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    jira_url = os.getenv("JIRA_URL", "")
    jira_email = os.getenv("JIRA_EMAIL", "")
    jira_api_token = os.getenv("JIRA_API_TOKEN", "")
    jira_project = os.getenv("JIRA_PROJECT", "")
    jira_status_filter = os.getenv("JIRA_STATUS_FILTER", "")
    secret_key = os.getenv("SECRET_KEY", "super-secret-key")

settings = Settings()
