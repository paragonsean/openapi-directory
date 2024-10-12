# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_value import AttributeValue
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.error_sub_entity import ErrorSubEntity
from openapi_server.models.functionality import Functionality
from openapi_server.models.functionality_created import FunctionalityCreated
from openapi_server.models.functionality_item import FunctionalityItem
from openapi_server.models.functionality_new import FunctionalityNew
from openapi_server.models.functionality_patch import FunctionalityPatch
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.tags_patch import TagsPatch


pytestmark = pytest.mark.asyncio

async def test_device_add_functionality_0(client):
    """Test case for device_add_functionality_0

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

async def test_functionalities_get(client):
    """Test case for functionalities_get

    Information about a Functionality
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/functionalities/{functionality_id}'.format(functionality_id='functionality_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_get_metadata(client):
    """Test case for functionality_get_metadata

    List metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/functionalities/{functionality_id}/metadata'.format(functionality_id='functionality_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_get_tags(client):
    """Test case for functionality_get_tags

    List tags
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/functionalities/{functionality_id}/tags'.format(functionality_id='functionality_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_patch(client):
    """Test case for functionality_patch

    Modify a Functionality
    """
    functionality_patch = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/functionalities/{functionality_id}'.format(functionality_id='functionality_id_example'),
        headers=headers,
        json=functionality_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_patch_metadata(client):
    """Test case for functionality_patch_metadata

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
        path='/functionalities/{functionality_id}/metadata'.format(functionality_id='functionality_id_example'),
        headers=headers,
        json=metadata_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_patch_tags(client):
    """Test case for functionality_patch_tags

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
        path='/functionalities/{functionality_id}/tags'.format(functionality_id='functionality_id_example'),
        headers=headers,
        json=tags_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_set(client):
    """Test case for functionality_set

    Modify an Attribute value
    """
    value = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/functionalities/{functionality_id}/attributes/{attribute_name}'.format(functionality_id='functionality_id_example', attribute_name='attribute_name_example'),
        headers=headers,
        json=value,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_value(client):
    """Test case for functionality_value

    Get an Attribute value
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/functionalities/{functionality_id}/attributes/{attribute_name}'.format(functionality_id='functionality_id_example', attribute_name='attribute_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_values(client):
    """Test case for functionality_values

    Get history of multiple attributes
    """
    params = [('names', ['names_example']),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('surround', True)]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/functionalities/{functionality_id}/attributes'.format(functionality_id='functionality_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_functionalities(client):
    """Test case for place_functionalities

    List Functionalities
    """
    params = [('devices', 'devices_example'),
                    ('functionalities', 'functionalities_example'),
                    ('embed-metadata', ['embed_metadata_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/functionalities'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

