# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.multi_response import MultiResponse
from openapi_server.models.pricing_response import PricingResponse


pytestmark = pytest.mark.asyncio

async def test_get_multi_hotel_offers(client):
    """Test case for get_multi_hotel_offers

    getMultiHotelOffers
    """
    params = [('hotelIds', ['[MCLONGHM]']),
                    ('adults', 1),
                    ('checkInDate', '2023-11-22'),
                    ('checkOutDate', '2013-10-20'),
                    ('countryOfResidence', 'country_of_residence_example'),
                    ('roomQuantity', 1),
                    ('priceRange', 'price_range_example'),
                    ('currency', 'currency_example'),
                    ('paymentPolicy', NONE),
                    ('boardType', 'board_type_example'),
                    ('includeClosed', True),
                    ('bestRateOnly', True),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v3/shopping/hotel-offers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_offer_pricing(client):
    """Test case for get_offer_pricing

    getOfferPricing
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v3/shopping/hotel-offers/{offer_id}'.format(offer_id='TSXOJ6LFQ2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

