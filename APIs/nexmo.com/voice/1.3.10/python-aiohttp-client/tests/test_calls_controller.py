# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_call_request import CreateCallRequest
from openapi_server.models.create_call_response import CreateCallResponse
from openapi_server.models.get_call_response import GetCallResponse
from openapi_server.models.get_calls_response import GetCallsResponse
from openapi_server.models.update_call_request import UpdateCallRequest


pytestmark = pytest.mark.asyncio

async def test_create_call(client):
    """Test case for create_call

    Create an outbound call
    """
    body = openapi_server.CreateCallRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/calls/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call(client):
    """Test case for get_call

    Get detail of a specific call
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/calls/{uuid}'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_calls(client):
    """Test case for get_calls

    Get details of your calls
    """
    params = [('status', 'started'),
                    ('date_start', '2016-11-14T07:45:14Z'),
                    ('date_end', '2016-11-14T07:45:14Z'),
                    ('page_size', 10),
                    ('record_index', 0),
                    ('order', asc),
                    ('conversation_uuid', 'conversation_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/calls/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_call(client):
    """Test case for update_call

    Modify an in progress call
    """
    body = openapi_server.UpdateCallRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/calls/{uuid}'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

