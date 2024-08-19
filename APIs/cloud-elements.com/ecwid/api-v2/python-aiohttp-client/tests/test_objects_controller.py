# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.objects_metadata import ObjectsMetadata
from openapi_server.models.swagger_docs import SwaggerDocs


pytestmark = pytest.mark.asyncio

async def test_get_objects(client):
    """Test case for get_objects

    Get a list of all the available objects.
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
        'elements_version': 'elements_version_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/objects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_object_name_docs(client):
    """Test case for get_objects_object_name_docs

    Get swagger docs for an object.
    """
    params = [('discovery', True),
                    ('resolveReferences', True),
                    ('basic', True),
                    ('version', '-1')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/objects/{object_name}/docs'.format(object_name='object_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_object_name_metadata(client):
    """Test case for get_objects_object_name_metadata

    Get a list of all the field for an object.
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
        'elements_version': 'elements_version_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/objects/{object_name}/metadata'.format(object_name='object_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

