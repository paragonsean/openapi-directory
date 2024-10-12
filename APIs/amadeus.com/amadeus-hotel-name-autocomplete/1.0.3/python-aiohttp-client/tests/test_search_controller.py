# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gethotels400_response import Gethotels400Response
from openapi_server.models.gethotels500_response import Gethotels500Response
from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_gethotels(client):
    """Test case for gethotels

    Returns a list of hotels matching a given keyword.
    """
    params = [('keyword', 'PARI'),
                    ('subType', ['sub_type_example']),
                    ('countryCode', 'FR'),
                    ('lang', 'EN'),
                    ('max', 20)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations/hotel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

