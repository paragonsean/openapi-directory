# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.venues_entity import VenuesEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_venues(client):
    """Test case for fetch_all_venues

    Find all venues
    """
    params = [('label', 'label_example'),
                    ('city', 'city_example'),
                    ('country_code', 'country_code_example'),
                    ('type', 'type_example'),
                    ('sort', label),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/venues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_venue(client):
    """Test case for fetch_one_venue

    Get one venue by ID
    """
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/venues/{venue_id}'.format(venue_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

