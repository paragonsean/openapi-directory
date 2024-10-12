# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_matches import IssueMatches
from openapi_server.models.issue_picker_suggestions import IssuePickerSuggestions
from openapi_server.models.issues_and_jql_queries import IssuesAndJQLQueries
from openapi_server.models.search_request_bean import SearchRequestBean
from openapi_server.models.search_results import SearchResults


pytestmark = pytest.mark.asyncio

async def test_get_issue_picker_resource(client):
    """Test case for get_issue_picker_resource

    Get issue picker suggestions
    """
    params = [('query', 'query'),
                    ('currentJQL', 'current_jql_example'),
                    ('currentIssueKey', 'current_issue_key_example'),
                    ('currentProjectId', 'current_project_id_example'),
                    ('showSubTasks', True),
                    ('showSubTaskParent', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/picker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_match_issues(client):
    """Test case for match_issues

    Check issues against JQL
    """
    body = {"issueIds":[0,0],"jqls":["jqls","jqls"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/jql/match',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_for_issues_using_jql(client):
    """Test case for search_for_issues_using_jql

    Search for issues using JQL (GET)
    """
    params = [('jql', 'project = HSP'),
                    ('startAt', 0),
                    ('maxResults', 50),
                    ('validateQuery', strict),
                    ('fields', ['fields_example']),
                    ('expand', 'expand_example'),
                    ('properties', ['properties_example']),
                    ('fieldsByKeys', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_for_issues_using_jql_post(client):
    """Test case for search_for_issues_using_jql_post

    Search for issues using JQL (POST)
    """
    body = {"expand":["expand","expand"],"jql":"jql","maxResults":0,"validateQuery":"strict","fieldsByKeys":True,"fields":["fields","fields"],"properties":["properties","properties"],"startAt":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

