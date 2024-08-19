# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.search_code200_response import SearchCode200Response
from openapi_server.models.search_commits200_response import SearchCommits200Response
from openapi_server.models.search_issues_and_pull_requests200_response import SearchIssuesAndPullRequests200Response
from openapi_server.models.search_labels200_response import SearchLabels200Response
from openapi_server.models.search_repos200_response import SearchRepos200Response
from openapi_server.models.search_topics200_response import SearchTopics200Response
from openapi_server.models.search_users200_response import SearchUsers200Response
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_search_code(client):
    """Test case for search_code

    Search code
    """
    params = [('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('order', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_commits(client):
    """Test case for search_commits

    Search commits
    """
    params = [('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('order', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/commits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_issues_and_pull_requests(client):
    """Test case for search_issues_and_pull_requests

    Search issues and pull requests
    """
    params = [('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('order', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/issues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_labels(client):
    """Test case for search_labels

    Search labels
    """
    params = [('repository_id', 56),
                    ('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('order', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/labels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_repos(client):
    """Test case for search_repos

    Search repositories
    """
    params = [('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('order', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/repositories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_topics(client):
    """Test case for search_topics

    Search topics
    """
    params = [('q', 'q_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/topics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_users(client):
    """Test case for search_users

    Search users
    """
    params = [('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('order', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/search/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

