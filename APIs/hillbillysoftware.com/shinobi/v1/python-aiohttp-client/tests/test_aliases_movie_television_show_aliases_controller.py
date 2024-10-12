# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aliases import Aliases


pytestmark = pytest.mark.asyncio

async def test_aliases_by_id_get(client):
    """Test case for aliases_by_id_get

    Get known aliases for Movies or Television shows from passed imdbID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Aliases/ByID/{access_token}/{imdb_id}'.format(access_token='access_token_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aliases_get(client):
    """Test case for aliases_get

    Get known aliases for Movies or Television shows
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Aliases/ByName/{access_token}/{title}'.format(access_token='access_token_example', title='title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

