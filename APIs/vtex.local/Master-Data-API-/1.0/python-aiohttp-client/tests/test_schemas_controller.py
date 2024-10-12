# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.saveschemabyname_request import SaveschemabynameRequest


pytestmark = pytest.mark.asyncio

async def test_deleteschemabyname(client):
    """Test case for deleteschemabyname

    Delete schema by name
    """
    headers = { 
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dataentities/{data_entity_name}/schemas/{schema_name}'.format(data_entity_name='Client', schema_name='{{schema}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getschemabyname(client):
    """Test case for getschemabyname

    Get schema by name
    """
    headers = { 
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/schemas/{schema_name}'.format(data_entity_name='Client', schema_name='{{schema}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getschemas(client):
    """Test case for getschemas

    Get schemas
    """
    headers = { 
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/schemas'.format(data_entity_name='Client'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saveschemabyname(client):
    """Test case for saveschemabyname

    Save schema by name
    """
    body = {"properties":{"name":{"type":"string"}}}
    headers = { 
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{data_entity_name}/schemas/{schema_name}'.format(data_entity_name='Client', schema_name='{{schema}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

