import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
from app.config.settings import settings

BATCH_SIZE = 50

def get_jira_auth():
    return HTTPBasicAuth(settings.jira_email, settings.jira_api_token)


def fetch_done_tickets(update_mode=False):
    session = requests.Session()
    session.auth = get_jira_auth()
    session.headers.update({"Accept": "application/json"})
    
    search_url = f"{settings.jira_url}/rest/api/3/search/jql"
    
    max_tickets = 100 if update_mode else None
    
    if max_tickets:
        params = {
            "jql": f"project = {settings.jira_project} AND statusCategory = done",
            "maxResults": max_tickets,
            "fields": "key"
        }
    else:
        params = {
            "jql": f"project = {settings.jira_project} AND statusCategory = done",
            "maxResults": 5000,
            "fields": "key"
        }
    
    r = session.get(search_url, params=params, timeout=30)
    issues = r.json().get("issues", [])
    keys = [i.get("key") for i in issues]
    
    fields_to_fetch = "summary,description,labels,status,assignee,created,updated,duedate,timespent,customfield_10002,comment"
    
    all_issues = []
    for i in range(0, len(keys), BATCH_SIZE):
        batch_keys = keys[i:i+BATCH_SIZE]
        jql = f'key IN ("' + '","'.join(batch_keys) + '")'
        
        params = {"jql": jql, "maxResults": BATCH_SIZE, "fields": fields_to_fetch}
        r = session.get(search_url, params=params, timeout=30)
        batch_issues = r.json().get("issues", [])
        all_issues.extend(batch_issues)
    
    return all_issues


def extract_ticket_data(issue):
    fields = issue.get('fields', {})
    
    desc_obj = fields.get('description', {})
    desc_text = ""
    if desc_obj and desc_obj.get('content'):
        for block in desc_obj['content']:
            if block.get('type') == 'paragraph':
                for item in block.get('content', []):
                    if item.get('type') == 'text':
                        desc_text += item.get('text', '') + ' '
    
    comments = fields.get('comment', {}).get('comments', [])
    last_comment = ""
    if comments:
        last_comment_obj = comments[-1].get('body', {})
        if last_comment_obj.get('content'):
            for block in last_comment_obj['content']:
                if block.get('type') == 'paragraph':
                    for item in block.get('content', []):
                        if item.get('type') == 'text':
                            last_comment += item.get('text', '') + ' '
    
    timespent = fields.get('timespent')
    time_spent_formatted = ""
    if timespent:
        hours = timespent // 3600
        minutes = (timespent % 3600) // 60
        time_spent_formatted = f"{hours}h {minutes}m" if hours else f"{minutes}m"
    
    labels = fields.get('labels', [])
    
    orgs = fields.get('customfield_10002', [])
    organizations = [org.get('name', '') for org in orgs]
    
    assignee = fields.get('assignee', {})
    assignee_name = assignee.get('displayName', '') if assignee else ''
    
    due_date_str = fields.get('duedate', '')
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except:
            pass
    
    return {
        'jira_id': str(issue.get('id')),
        'key': issue.get('key'),
        'summary': fields.get('summary', ''),
        'description': desc_text.strip(),
        'last_comment': last_comment.strip(),
        'time_spent': time_spent_formatted,
        'labels': json.dumps(labels),
        'organizations': json.dumps(organizations),
        'assignee': assignee_name,
        'due_date': due_date,
    }
