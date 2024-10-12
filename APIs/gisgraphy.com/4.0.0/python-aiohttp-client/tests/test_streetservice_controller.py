# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.street_search_results_dto import StreetSearchResultsDto


pytestmark = pytest.mark.asyncio

async def test_streetsearch(client):
    """Test case for streetsearch

    Geocode an address
    """
    params = [('lat', 3.4),
                    ('lng', 3.4),
                    ('radius', 10000.0),
                    ('oneway', False),
                    ('distance', True),
                    ('streettype', 'streettype_example'),
                    ('format', XML),
                    ('from', 1),
                    ('to', 10),
                    ('callback', 'param_callback_example'),
                    ('indent', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/street/find',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

