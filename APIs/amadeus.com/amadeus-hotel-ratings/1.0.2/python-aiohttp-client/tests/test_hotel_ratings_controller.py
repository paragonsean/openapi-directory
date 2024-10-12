# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error401 import Error401
from openapi_server.models.error500 import Error500
from openapi_server.models.success_sentiments import SuccessSentiments


pytestmark = pytest.mark.asyncio

async def test_get_sentiments_by_hotel_ids(client):
    """Test case for get_sentiments_by_hotel_ids

    Get sentiments by Amadeus Hotel Ids
    """
    params = [('hotelIds', ['[TELONMFS]'])]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/e-reputation/hotel-sentiments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

