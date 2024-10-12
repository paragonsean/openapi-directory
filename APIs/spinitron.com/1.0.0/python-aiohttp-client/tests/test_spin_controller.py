# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.spin import Spin
from openapi_server.models.spins_get200_response import SpinsGet200Response
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_spins_get(client):
    """Test case for spins_get

    Returns spins optionally filtered by {start} and/or {end} datetimes
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('playlist_id', 56),
                    ('show_id', 56),
                    ('count', 20),
                    ('page', 56),
                    ('fields', ['fields_example']),
                    ('expand', ['expand_example'])]
    headers = { 
        'Accept': 'application/json',
        'accessToken': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/spins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spins_id_get(client):
    """Test case for spins_id_get

    Get a Spin by id
    """
    params = [('fields', ['fields_example']),
                    ('expand', ['expand_example'])]
    headers = { 
        'Accept': 'application/json',
        'accessToken': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/spins/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_spins_post(client):
    """Test case for spins_post

    Log a Spin
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'accessToken': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'artist': 'artist_example',
        'composer': 'composer_example',
        'duration': 56,
        'genre': 'genre_example',
        'isrc': 'isrc_example',
        'label': 'label_example',
        'live': True,
        'release': 'release_example',
        'song': 'song_example',
        'start': '2013-10-20T19:20:30+01:00'
        }
    response = await client.request(
        method='POST',
        path='/api/spins',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

