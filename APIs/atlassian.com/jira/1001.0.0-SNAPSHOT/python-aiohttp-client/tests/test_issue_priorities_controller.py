# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_priority_details import CreatePriorityDetails
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_priority import PageBeanPriority
from openapi_server.models.priority import Priority
from openapi_server.models.priority_id import PriorityId
from openapi_server.models.reorder_issue_priorities import ReorderIssuePriorities
from openapi_server.models.set_default_priority_request import SetDefaultPriorityRequest
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_priority_details import UpdatePriorityDetails


pytestmark = pytest.mark.asyncio

async def test_create_priority(client):
    """Test case for create_priority

    Create priority
    """
    body = {"statusColor":"statusColor","name":"name","description":"description","iconUrl":"/images/icons/priorities/blocker.png"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/priority',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_priority(client):
    """Test case for delete_priority

    Delete priority
    """
    params = [('replaceWith', 'replace_with_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/priority/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_priorities(client):
    """Test case for get_priorities

    Get priorities
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/priority',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_priority(client):
    """Test case for get_priority

    Get priority
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/priority/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_priorities(client):
    """Test case for move_priorities

    Move priorities
    """
    body = {"ids":["ids","ids"],"after":"after","position":"position"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/priority/move',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_priorities(client):
    """Test case for search_priorities

    Search priorities
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('id', ['id_example']),
                    ('onlyDefault', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/priority/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_default_priority(client):
    """Test case for set_default_priority

    Set default priority
    """
    body = {"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/priority/default',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_priority(client):
    """Test case for update_priority

    Update priority
    """
    body = {"statusColor":"statusColor","name":"name","description":"description","iconUrl":"/images/icons/priorities/blocker.png"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/priority/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

