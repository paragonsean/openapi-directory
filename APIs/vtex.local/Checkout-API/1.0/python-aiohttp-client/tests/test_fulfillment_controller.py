# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_address_by_postal_code(client):
    """Test case for get_address_by_postal_code

    Get address by postal code
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/postal-code/{country_code}/{postal_code}'.format(country_code='BRA', postal_code='1234000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pickup_ppoints_by_location(client):
    """Test case for list_pickup_ppoints_by_location

    List pickup points by location
    """
    params = [('geoCoordinates', [-47.924747467041016,-15.832582473754883]),
                    ('postalCode', '1234000'),
                    ('countryCode', 'BRA')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/pickup-points',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

