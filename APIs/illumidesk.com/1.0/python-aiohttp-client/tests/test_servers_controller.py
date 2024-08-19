# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.server_size import ServerSize
from openapi_server.models.server_size_data import ServerSizeData
from openapi_server.models.server_size_error import ServerSizeError


pytestmark = pytest.mark.asyncio

async def test_servers_options_resources_read(client):
    """Test case for servers_options_resources_read

    Get a server size by id
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers/options/server-size/{size}'.format(size='size_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_options_server_size_create(client):
    """Test case for servers_options_server_size_create

    Create a new server size item
    """
    serversize_data = {"memory":6,"name":"name","active":True,"cpu":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/options/server-size/',
        headers=headers,
        json=serversize_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_options_server_size_delete(client):
    """Test case for servers_options_server_size_delete

    Delete a server size by id
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/servers/options/server-size/{size}'.format(size='size_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_options_server_size_replace(client):
    """Test case for servers_options_server_size_replace

    Replace a server size by id
    """
    serversize_data = {"memory":6,"name":"name","active":True,"cpu":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/servers/options/server-size/{size}'.format(size='size_example'),
        headers=headers,
        json=serversize_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_options_server_size_update(client):
    """Test case for servers_options_server_size_update

    Update a server size by id
    """
    serversize_data = {"memory":6,"name":"name","active":True,"cpu":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/servers/options/server-size/{size}'.format(size='size_example'),
        headers=headers,
        json=serversize_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_options_sizes_list(client):
    """Test case for servers_options_sizes_list

    Retrieve available server sizes
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers/options/server-size/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

