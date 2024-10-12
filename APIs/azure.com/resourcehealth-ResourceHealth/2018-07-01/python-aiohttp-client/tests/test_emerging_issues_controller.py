# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.emerging_issue_list_result import EmergingIssueListResult
from openapi_server.models.emerging_issues_get_result import EmergingIssuesGetResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_emerging_issues_get(client):
    """Test case for emerging_issues_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ResourceHealth/emergingIssues/{issue_name}'.format(issue_name='issue_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_emerging_issues_list(client):
    """Test case for emerging_issues_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ResourceHealth/emergingIssues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

