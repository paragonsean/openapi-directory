# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.show import Show
from openapi_server.models.shows_get200_response import ShowsGet200Response


pytestmark = pytest.mark.asyncio

async def test_shows_get(client):
    """Test case for shows_get

    Returns scheduled shows optionally filtered by {start} and/or {end} datetimes
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
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
        path='/api/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shows_id_get(client):
    """Test case for shows_id_get

    Get a Show by id
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
        path='/api/shows/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

