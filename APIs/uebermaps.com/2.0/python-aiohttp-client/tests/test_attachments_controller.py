# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attachment import Attachment


pytestmark = pytest.mark.asyncio

async def test_attachments_id_delete(client):
    """Test case for attachments_id_delete

    Delete attachment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/attachments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_attachments_get(client):
    """Test case for maps_id_attachments_get

    List attachments for a given map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}/attachments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_attachments_post(client):
    """Test case for maps_id_attachments_post

    Upload map attachment
    """
    image = 'image_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/maps/{id}/attachments'.format(id=56),
        headers=headers,
        json=image,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_attachments_get(client):
    """Test case for spots_id_attachments_get

    List attachments for a given spot
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots/{id}/attachments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_attachments_post(client):
    """Test case for spots_id_attachments_post

    Upload spot attachment
    """
    image = 'image_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/spots/{id}/attachments'.format(id=56),
        headers=headers,
        json=image,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

