# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.putindices_request import PutindicesRequest


pytestmark = pytest.mark.asyncio

async def test_deleteindexbyname(client):
    """Test case for deleteindexbyname

    Delete index by name
    """
    headers = { 
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dataentities/{data_entity_name}/indices/{index_name}'.format(data_entity_name='Client', index_name='{{index_name}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getindexbyname(client):
    """Test case for getindexbyname

    Get index by name
    """
    headers = { 
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/indices/{index_name}'.format(data_entity_name='Client', index_name='{{index_name}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getindices(client):
    """Test case for getindices

    Get indices
    """
    headers = { 
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/indices'.format(data_entity_name='Client'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_putindices(client):
    """Test case for putindices

    Put indices
    """
    body = {"fields":"fieldName","multiple":False,"name":"indexName"}
    headers = { 
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{data_entity_name}/indices'.format(data_entity_name='Client'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

