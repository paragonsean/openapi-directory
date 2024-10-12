# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.command import Command
from openapi_server.models.command_type import CommandType


pytestmark = pytest.mark.asyncio

async def test_commands_get(client):
    """Test case for commands_get

    Fetch a list of Saved Commands
    """
    params = [('all', True),
                    ('userId', 56),
                    ('deviceId', 56),
                    ('groupId', 56),
                    ('refresh', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/commands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commands_id_delete(client):
    """Test case for commands_id_delete

    Delete a Saved Command
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/commands/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commands_id_put(client):
    """Test case for commands_id_put

    Update a Saved Command
    """
    body = {"description":"description","attributes":"{}","id":6,"type":"type","deviceId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/commands/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commands_post(client):
    """Test case for commands_post

    Create a Saved Command
    """
    body = {"description":"description","attributes":"{}","id":6,"type":"type","deviceId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/commands',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commands_send_get(client):
    """Test case for commands_send_get

    Fetch a list of Saved Commands supported by Device at the moment
    """
    params = [('deviceId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/commands/send',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commands_send_post(client):
    """Test case for commands_send_post

    Dispatch commands to device
    """
    body = {"description":"description","attributes":"{}","id":6,"type":"type","deviceId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/commands/send',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commands_types_get(client):
    """Test case for commands_types_get

    Fetch a list of available Commands for the Device or all possible Commands if Device ommited
    """
    params = [('deviceId', 56),
                    ('protocol', 'protocol_example'),
                    ('textChannel', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/commands/types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

