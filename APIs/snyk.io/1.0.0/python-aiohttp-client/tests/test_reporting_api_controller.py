# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_get_issue_counts(client):
    """Test case for get_issue_counts

    Get issue counts
    """
    body = openapi_server.GetIssueCountsRequest()
    params = [('from', '2017-07-01'),
                    ('to', '2017-07-03'),
                    ('groupBy', 'severity')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/counts/issues',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_issue_counts(client):
    """Test case for get_latest_issue_counts

    Get latest issue counts
    """
    body = openapi_server.GetIssueCountsRequest()
    params = [('groupBy', 'severity')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/counts/issues/latest',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_project_counts(client):
    """Test case for get_latest_project_counts

    Get latest project counts
    """
    body = openapi_server.GetProjectCountsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/counts/projects/latest',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_issues(client):
    """Test case for get_list_of_issues

    Get list of issues
    """
    body = openapi_server.GetListOfIssuesRequest()
    params = [('from', '2017-07-01'),
                    ('to', '2017-07-07'),
                    ('page', 1),
                    ('perPage', 100),
                    ('sortBy', 'issueTitle'),
                    ('order', 'asc'),
                    ('groupBy', 'issue')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/issues/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_latest_issues(client):
    """Test case for get_list_of_latest_issues

    Get list of latest issues
    """
    body = openapi_server.GetListOfIssuesRequest()
    params = [('page', 1),
                    ('perPage', 100),
                    ('sortBy', 'issueTitle'),
                    ('order', 'asc'),
                    ('groupBy', 'issue')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/issues/latest',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_counts(client):
    """Test case for get_project_counts

    Get project counts
    """
    body = openapi_server.GetProjectCountsRequest()
    params = [('from', '2017-07-01'),
                    ('to', '2017-07-03')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/counts/projects',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_counts(client):
    """Test case for get_test_counts

    Get test counts
    """
    body = openapi_server.GetTestCountsRequest()
    params = [('from', '2017-07-01'),
                    ('to', '2017-07-03'),
                    ('groupBy', 'isPrivate')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/reporting/counts/tests',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

