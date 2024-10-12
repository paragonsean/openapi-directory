from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_issue_counts200_response import GetIssueCounts200Response
from openapi_server.models.get_issue_counts400_response import GetIssueCounts400Response
from openapi_server.models.get_issue_counts_request import GetIssueCountsRequest
from openapi_server.models.get_list_of_issues200_response import GetListOfIssues200Response
from openapi_server.models.get_list_of_issues_request import GetListOfIssuesRequest
from openapi_server.models.get_project_counts200_response import GetProjectCounts200Response
from openapi_server.models.get_project_counts_request import GetProjectCountsRequest
from openapi_server.models.get_test_counts200_response import GetTestCounts200Response
from openapi_server.models.get_test_counts_request import GetTestCountsRequest
from openapi_server import util


async def get_issue_counts(request: web.Request, _from, to, group_by=None, body=None) -> web.Response:
    """Get issue counts

    

    :param _from: The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60;
    :type _from: str
    :param to: The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60;
    :type to: str
    :param group_by: The field to group results by
    :type group_by: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetIssueCountsRequest.from_dict(body)
    return web.Response(status=200)


async def get_latest_issue_counts(request: web.Request, group_by=None, body=None) -> web.Response:
    """Get latest issue counts

    

    :param group_by: The field to group results by
    :type group_by: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetIssueCountsRequest.from_dict(body)
    return web.Response(status=200)


async def get_latest_project_counts(request: web.Request, body=None) -> web.Response:
    """Get latest project counts

    

    :param body: 
    :type body: dict | bytes

    """
    body = GetProjectCountsRequest.from_dict(body)
    return web.Response(status=200)


async def get_list_of_issues(request: web.Request, _from, to, page=None, per_page=None, sort_by=None, order=None, group_by=None, body=None) -> web.Response:
    """Get list of issues

    

    :param _from: The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60;
    :type _from: str
    :param to: The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60;
    :type to: str
    :param page: The page of results to request
    :type page: 
    :param per_page: The number of results to return per page (Maximum: 1000)
    :type per_page: 
    :param sort_by: The key to sort results by
    :type sort_by: str
    :param order: The direction to sort results.
    :type order: str
    :param group_by: Set to issue to group the same issue in multiple projects
    :type group_by: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetListOfIssuesRequest.from_dict(body)
    return web.Response(status=200)


async def get_list_of_latest_issues(request: web.Request, page=None, per_page=None, sort_by=None, order=None, group_by=None, body=None) -> web.Response:
    """Get list of latest issues

    

    :param page: The page of results to request
    :type page: 
    :param per_page: The number of results to return per page (Maximum: 1000)
    :type per_page: 
    :param sort_by: The key to sort results by
    :type sort_by: str
    :param order: The direction to sort results.
    :type order: str
    :param group_by: Set to issue to group the same issue in multiple projects
    :type group_by: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetListOfIssuesRequest.from_dict(body)
    return web.Response(status=200)


async def get_project_counts(request: web.Request, _from, to, body=None) -> web.Response:
    """Get project counts

    

    :param _from: The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60;
    :type _from: str
    :param to: The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60;
    :type to: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetProjectCountsRequest.from_dict(body)
    return web.Response(status=200)


async def get_test_counts(request: web.Request, _from, to, group_by=None, body=None) -> web.Response:
    """Get test counts

    

    :param _from: The date you wish to count tests from, in the format &#x60;YYYY-MM-DD&#x60;
    :type _from: str
    :param to: The date you wish to count tests until, in the format &#x60;YYYY-MM-DD&#x60;
    :type to: str
    :param group_by: The field to group results by
    :type group_by: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetTestCountsRequest.from_dict(body)
    return web.Response(status=200)
