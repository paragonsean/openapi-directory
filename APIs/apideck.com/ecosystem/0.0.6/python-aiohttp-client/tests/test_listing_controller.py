# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_listing_response import GetListingResponse
from openapi_server.models.get_listings_response import GetListingsResponse


pytestmark = pytest.mark.asyncio

async def test_listings_all(client):
    """Test case for listings_all

    List listings
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 50),
                    ('external_id', 'external_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/listings'.format(ecosystem_id='ecosystem_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listings_one(client):
    """Test case for listings_one

    Get listing
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/listings/{id}'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

