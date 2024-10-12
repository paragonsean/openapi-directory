# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_json_get200_response import QueryJsonGet200Response


pytestmark = pytest.mark.asyncio

async def test_query_json_get(client):
    """Test case for query_json_get

    Geographic API
    """
    params = [('name', 'name_example'),
                    ('latitude', 'latitude_example'),
                    ('longitude', 'longitude_example'),
                    ('elevation', 56),
                    ('sw', 'sw_example'),
                    ('query', 'query_example'),
                    ('filter', 'filter_example'),
                    ('date_range', 'date_range_example'),
                    ('facets', 0),
                    ('sort', 'sort_example'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/semantic/v2/geocodes/query.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

