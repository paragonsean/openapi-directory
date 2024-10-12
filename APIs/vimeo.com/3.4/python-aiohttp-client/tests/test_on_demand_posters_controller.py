# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_vod_poster_request import EditVodPosterRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture


pytestmark = pytest.mark.asyncio

async def test_add_vod_poster(client):
    """Test case for add_vod_poster

    Add a poster to an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ondemand/pages/{ondemand_id}/pictures'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_vod_poster(client):
    """Test case for edit_vod_poster

    Edit a poster of an On Demand page
    """
    body = openapi_server.EditVodPosterRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/ondemand/pages/{ondemand_id}/pictures/{poster_id}'.format(ondemand_id=61326, poster_id=12345),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_poster(client):
    """Test case for get_vod_poster

    Get a specific poster of an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/pictures/{poster_id}'.format(ondemand_id=61326, poster_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_posters(client):
    """Test case for get_vod_posters

    Get all the posters of an On Demand page
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
        path='/ondemand/pages/{ondemand_id}/pictures'.format(ondemand_id=61326),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

