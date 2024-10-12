# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.jira_status import JiraStatus
from openapi_server.models.page_of_statuses import PageOfStatuses
from openapi_server.models.status_create_request import StatusCreateRequest
from openapi_server.models.status_update_request import StatusUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_create_statuses(client):
    """Test case for create_statuses

    Bulk create statuses
    """
    body = {"scope":{"project":{"id":"id"},"type":"PROJECT"},"statuses":[{"name":"name","description":"description","statusCategory":"TODO"},{"name":"name","description":"description","statusCategory":"TODO"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/statuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_statuses_by_id(client):
    """Test case for delete_statuses_by_id

    Bulk delete Statuses
    """
    params = [('id', ['id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statuses_by_id(client):
    """Test case for get_statuses_by_id

    Bulk get statuses
    """
    params = [('expand', 'expand_example'),
                    ('id', ['id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search statuses paginated
    """
    params = [('expand', 'expand_example'),
                    ('projectId', 'project_id_example'),
                    ('startAt', 0),
                    ('maxResults', 200),
                    ('searchString', 'search_string_example'),
                    ('statusCategory', 'status_category_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/statuses/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_statuses(client):
    """Test case for update_statuses

    Bulk update statuses
    """
    body = {"statuses":[{"name":"name","description":"description","id":"id","statusCategory":"TODO"},{"name":"name","description":"description","id":"id","statusCategory":"TODO"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/statuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

