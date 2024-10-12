# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_store_device import DataStoreDevice
from openapi_server.models.tag_definition import TagDefinition
from openapi_server.models.tag_reference import TagReference
from openapi_server.models.tag_value import TagValue


pytestmark = pytest.mark.asyncio

async def test_batch_read_tags(client):
    """Test case for batch_read_tags

    
    """
    tags = [openapi_server.TagReference()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/data-store/read',
        headers=headers,
        json=tags,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_tags(client):
    """Test case for list_all_tags

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data-store/tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_device_tags(client):
    """Test case for list_device_tags

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data-store/devices/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_devices(client):
    """Test case for list_devices

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data-store/devices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_tag(client):
    """Test case for read_tag

    
    """
    params = [('index', 0.0),
                    ('count', 1.0)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data-store/read/{id}'.format(id=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_tag(client):
    """Test case for write_tag

    
    """
    params = [('value', 'value_example'),
                    ('index', 0.0)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/data-store/write/{id}'.format(id=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

