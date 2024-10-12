# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_clutter_request import AddClutterRequest


pytestmark = pytest.mark.asyncio

async def test_add_clutter(client):
    """Test case for add_clutter

    Upload clutter data as GeoJSON
    """
    body = openapi_server.AddClutterRequest()
    headers = { 
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/clutter/add',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Delete a calculation from the database.
    """
    params = [('cid', 56)]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/archive/delete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network(client):
    """Test case for delete_network

    Delete an entire network
    """
    params = [('nid', 'nid_example')]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/archive/delete/network',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export(client):
    """Test case for export

    Export a calculation in a GIS file format
    """
    params = [('file', 'file_example'),
                    ('fmt', 'fmt_example')]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/archive/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    List calculations from your archive
    """
    params = [('n', 3.4),
                    ('e', 3.4),
                    ('s', 3.4),
                    ('w', 3.4)]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/archive/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

