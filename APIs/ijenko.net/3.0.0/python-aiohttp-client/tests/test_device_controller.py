# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.device import Device
from openapi_server.models.device_item import DeviceItem
from openapi_server.models.device_patch import DevicePatch
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.functionality_created import FunctionalityCreated
from openapi_server.models.functionality_new import FunctionalityNew
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.tags_patch import TagsPatch


pytestmark = pytest.mark.asyncio

async def test_device_add_functionality(client):
    """Test case for device_add_functionality

    Add dynamically a functionality
    """
    functionality_info = {"endpoint":20,"metadata":{},"name":"name","class":"class","tags":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/devices/{device_id}/functionalities'.format(device_id='device_id_example'),
        headers=headers,
        json=functionality_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_get_metadata(client):
    """Test case for device_get_metadata

    List metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/devices/{device_id}/metadata'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_get_tags(client):
    """Test case for device_get_tags

    List tags
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/devices/{device_id}/tags'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_patch_metadata(client):
    """Test case for device_patch_metadata

    Modify metadata
    """
    metadata_patch = {"add":{},"remove":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/devices/{device_id}/metadata'.format(device_id='device_id_example'),
        headers=headers,
        json=metadata_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_patch_tags(client):
    """Test case for device_patch_tags

    Modify tags
    """
    tags_patch = {"add":[null,null],"remove":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/devices/{device_id}/tags'.format(device_id='device_id_example'),
        headers=headers,
        json=tags_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get(client):
    """Test case for devices_get

    Information about a Device
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/devices/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_patch(client):
    """Test case for devices_patch

    Update a Device
    """
    device_patch = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/devices/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        json=device_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_devices(client):
    """Test case for place_devices

    List of Devices
    """
    params = [('devices', 'devices_example'),
                    ('embed-metadata', ['embed_metadata_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/devices'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

