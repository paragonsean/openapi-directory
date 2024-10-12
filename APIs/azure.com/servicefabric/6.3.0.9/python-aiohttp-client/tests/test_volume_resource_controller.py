# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.volume_resource_description import VolumeResourceDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_volume_resource(client):
    """Test case for create_volume_resource

    Creates or updates a volume resource.
    """
    volume_resource_description = openapi_server.VolumeResourceDescription()
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Volumes/{volume_resource_name}'.format(volume_resource_name='volume_resource_name_example'),
        headers=headers,
        json=volume_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_volume_resource(client):
    """Test case for delete_volume_resource

    Deletes the volume resource.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Volumes/{volume_resource_name}'.format(volume_resource_name='volume_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_volume_resource(client):
    """Test case for get_volume_resource

    Gets the volume resource.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Volumes/{volume_resource_name}'.format(volume_resource_name='volume_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

