# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_command_request import CreateCommandRequest
from openapi_server.models.create_command_response import CreateCommandResponse
from openapi_server.models.delete_command_response import DeleteCommandResponse
from openapi_server.models.get_command_response import GetCommandResponse
from openapi_server.models.list_commands_response import ListCommandsResponse
from openapi_server.models.update_command_request import UpdateCommandRequest
from openapi_server.models.update_command_response import UpdateCommandResponse


pytestmark = pytest.mark.asyncio

async def test_create_command(client):
    """Test case for create_command

    Create command
    """
    body = {"args":"args","set":"set","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/commands',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_command(client):
    """Test case for delete_command

    Delete command
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/commands/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_command(client):
    """Test case for get_command

    Get command
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/commands/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_commands(client):
    """Test case for list_commands

    List commands
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/commands',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_command(client):
    """Test case for update_command

    Update command
    """
    body = {"args":"args","set":"set","description":"description","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/commands/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

