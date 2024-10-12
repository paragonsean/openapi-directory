# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.imdb_id import ImdbID


pytestmark = pytest.mark.asyncio

async def test_get_imd_bid_get_async(client):
    """Test case for get_imd_bid_get_async

    Gets list of avaiable IMDB ids from Movies and TV Show databases, you can use those to query other end points that need ID's
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/GetIMDBid/ByID/{access_token}/{query}'.format(access_token='access_token_example', query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

