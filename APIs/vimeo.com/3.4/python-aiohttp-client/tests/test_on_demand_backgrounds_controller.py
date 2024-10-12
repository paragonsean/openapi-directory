# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_vod_background_request import EditVodBackgroundRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture


pytestmark = pytest.mark.asyncio

async def test_create_vod_background(client):
    """Test case for create_vod_background

    Add a background to an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ondemand/pages/{ondemand_id}/backgrounds'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vod_background(client):
    """Test case for delete_vod_background

    Remove a background from an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}/backgrounds/{background_id}'.format(background_id=12345, ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_vod_background(client):
    """Test case for edit_vod_background

    Edit a background of an On Demand page
    """
    body = openapi_server.EditVodBackgroundRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/ondemand/pages/{ondemand_id}/backgrounds/{background_id}'.format(background_id=12345, ondemand_id=61326),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_background(client):
    """Test case for get_vod_background

    Get a specific background of an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/backgrounds/{background_id}'.format(background_id=12345, ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_backgrounds(client):
    """Test case for get_vod_backgrounds

    Get all the backgrounds of an On Demand page
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/backgrounds'.format(ondemand_id=61326),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

