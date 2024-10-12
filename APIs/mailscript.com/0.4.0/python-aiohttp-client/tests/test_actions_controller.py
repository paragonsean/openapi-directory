# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_action_request import AddActionRequest
from openapi_server.models.add_action_response import AddActionResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_actions_response import GetAllActionsResponse
from openapi_server.models.key import Key


pytestmark = pytest.mark.asyncio

async def test_add_action(client):
    """Test case for add_action

    Add an action
    """
    body = openapi_server.AddActionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/actions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_action(client):
    """Test case for delete_action

    Delete an action
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/actions/{action}'.format(action='action_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_actions(client):
    """Test case for get_all_actions

    Get all actions for the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/actions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_action(client):
    """Test case for update_action

    Update an action key
    """
    body = openapi_server.AddActionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/actions/{action}'.format(action='action_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

