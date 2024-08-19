# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.search200_response import Search200Response


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search for Item 
    """
    params = [('q', 'remaster%20track:Doxy%20artist:Miles%20Davis'),
                    ('type', ['type_example']),
                    ('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0),
                    ('include_external', 'include_external_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

