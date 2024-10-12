# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_action_request import CreateActionRequest
from openapi_server.models.create_action_response import CreateActionResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_action_response import FetchActionResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.update_action_request import UpdateActionRequest
from openapi_server.models.update_action_response import UpdateActionResponse


pytestmark = pytest.mark.asyncio

async def test_create_action(client):
    """Test case for create_action

    Create action
    """
    body = openapi_server.CreateActionRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/action',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_action(client):
    """Test case for fetch_action

    Get an action
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/action/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_action(client):
    """Test case for update_action

    Update an action
    """
    body = openapi_server.UpdateActionRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='PATCH',
        path='/pub/action/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

