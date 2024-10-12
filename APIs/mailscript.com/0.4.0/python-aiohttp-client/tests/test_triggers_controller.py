# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_trigger_request import AddTriggerRequest
from openapi_server.models.add_trigger_response import AddTriggerResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_triggers_response import GetAllTriggersResponse


pytestmark = pytest.mark.asyncio

async def test_add_trigger(client):
    """Test case for add_trigger

    Setup a trigger
    """
    body = {"criteria":{"sentTo":"sentTo","domain":"domain","from":"from","subjectContains":"subjectContains","hasAttachments":True,"hasTheWords":"hasTheWords"},"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/triggers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_trigger(client):
    """Test case for delete_trigger

    Delete a trigger
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/triggers/{trigger}'.format(trigger='trigger_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_triggers(client):
    """Test case for get_all_triggers

    Get all triggers you have access to
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/triggers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_trigger(client):
    """Test case for update_trigger

    Update a trigger
    """
    body = {"criteria":{"sentTo":"sentTo","domain":"domain","from":"from","subjectContains":"subjectContains","hasAttachments":True,"hasTheWords":"hasTheWords"},"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/triggers/{trigger}'.format(trigger='trigger_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

