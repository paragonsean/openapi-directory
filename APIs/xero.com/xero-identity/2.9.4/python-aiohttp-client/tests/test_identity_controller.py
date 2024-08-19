# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection import Connection


pytestmark = pytest.mark.asyncio

async def test_delete_connection(client):
    """Test case for delete_connection

    Deletes a connection for this user (i.e. disconnect a tenant)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Connections/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connections(client):
    """Test case for get_connections

    Retrieves the connections for this user
    """
    params = [('authEventId', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Connections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

