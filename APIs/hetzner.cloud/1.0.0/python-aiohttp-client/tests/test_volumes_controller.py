# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_volume_request import CreateVolumeRequest
from openapi_server.models.update_volume_request import UpdateVolumeRequest
from openapi_server.models.volumes_get200_response import VolumesGet200Response
from openapi_server.models.volumes_id_get200_response import VolumesIdGet200Response
from openapi_server.models.volumes_post201_response import VolumesPost201Response


pytestmark = pytest.mark.asyncio

async def test_volumes_get(client):
    """Test case for volumes_get

    Get all Volumes
    """
    params = [('status', 'status_example'),
                    ('sort', 'sort_example'),
                    ('name', 'name_example'),
                    ('label_selector', 'label_selector_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/volumes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_delete(client):
    """Test case for volumes_id_delete

    Delete a Volume
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/volumes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_get(client):
    """Test case for volumes_id_get

    Get a Volume
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/volumes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_id_put(client):
    """Test case for volumes_id_put

    Update a Volume
    """
    body = {"name":"database-storage","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/volumes/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_post(client):
    """Test case for volumes_post

    Create a Volume
    """
    body = {"server":0,"automount":False,"size":42,"format":"xfs","name":"databases-storage","location":"nbg1","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/volumes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

