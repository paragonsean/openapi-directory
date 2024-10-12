# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_page import OnDemandPage


pytestmark = pytest.mark.asyncio

async def test_check_if_vod_was_purchased(client):
    """Test case for check_if_vod_was_purchased

    Check if a user has made a purchase or rental from an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/ondemand/purchases'.format(user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_vod_was_purchased_alt1(client):
    """Test case for check_if_vod_was_purchased_alt1

    Check if a user has made a purchase or rental from an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/ondemand/purchases/{ondemand_id}'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_purchases(client):
    """Test case for get_vod_purchases

    Get all the On Demand purchases and rentals that a user has made
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/ondemand/purchases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

