from jira import JIRA
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

import os

mcp = FastMCP("jira")

JIRA_URL = os.environ.get("JIRA_URL")
JIRA_USER_EMAIL = os.environ.get("JIRA_USER_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_USER_EMAIL, JIRA_API_TOKEN))

# headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
# headers["Authorization"] = f"Bearer {JIRA_API_TOKEN}"
# jira = JIRA(server=JIRA_URL, options={"headers": headers})

# jira = JIRA(server=JIRA_URL)


# jira = JIRA(basic_auth=(JIRA_USER_EMAIL, JIRA_API_TOKEN))


@mcp.tool()
def create_jira_ticket(summary: str, description: str, project_id: str, issue_type: str) -> str:
    """
    Create a JIRA ticket.

    Args:
        summary (str): The summary of the JIRA ticket.
        description (str): The description of the JIRA ticket.
        project_id (str): The project ID where the ticket will be created.
    Returns:
        str: The key of the created JIRA ticket.

    Usage:
        create_jira_ticket("Bug in feature X", "Detailed description of the bug", "PROJECT1", "Bug")
    """
    try:
        issue_dict = {
            'project': {'key': project_id},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        new_issue = jira.create_issue(fields=issue_dict)
        return new_issue.key

    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to create JIRA ticket: {str(e)}")) from e


@mcp.tool()
def read_jira_ticket(ticket_id: str) -> str:
    """
    Read a JIRA ticket.

    Args:
        ticket_id (str): The ID of the JIRA ticket.

    Returns:
        str: The description of the JIRA ticket.

    Usage:
        read_jira_ticket("PROJECT-123")
    """
    try:
        jira_issue = jira.issue(ticket_id)

        return jira_issue.fields.description

    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to read JIRA ticket: {str(e)}")) from e


read_jira_ticket("SCRUM-1")
