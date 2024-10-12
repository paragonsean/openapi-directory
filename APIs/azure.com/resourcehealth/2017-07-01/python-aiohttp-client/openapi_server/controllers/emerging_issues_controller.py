from typing import List, Dict
from aiohttp import web

from openapi_server.models.emerging_issue_list_result import EmergingIssueListResult
from openapi_server.models.emerging_issues_get_result import EmergingIssuesGetResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def emerging_issues_get(request: web.Request, issue_name, api_version) -> web.Response:
    """emerging_issues_get

    Gets Azure services&#39; emerging issues.

    :param issue_name: The name of the emerging issue.
    :type issue_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def emerging_issues_list(request: web.Request, api_version) -> web.Response:
    """emerging_issues_list

    Lists Azure services&#39; emerging issues.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
