# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server.models.connection_collection import ConnectionCollection
from openapi_server.models.connection_test import ConnectionTest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_delete_connection(client):
    """Test case for delete_connection

    Delete a connection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connection(client):
    """Test case for get_connection

    Get a connection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connections(client):
    """Test case for get_connections

    List connections
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/connections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_connection(client):
    """Test case for patch_connection

    Update a connection
    """
    body = {"conn_type":"conn_type","schema":"schema","password":"password","connection_id":"connection_id","port":0,"extra":"extra","host":"host","description":"description","login":"login"}
    params = [('update_mask', ['update_mask_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_connection(client):
    """Test case for post_connection

    Create a connection
    """
    body = {"conn_type":"conn_type","schema":"schema","password":"password","connection_id":"connection_id","port":0,"extra":"extra","host":"host","description":"description","login":"login"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/connections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_connection(client):
    """Test case for test_connection

    Test a connection
    """
    body = {"conn_type":"conn_type","schema":"schema","password":"password","connection_id":"connection_id","port":0,"extra":"extra","host":"host","description":"description","login":"login"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/connections/test',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

