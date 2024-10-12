# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pricing_countries_response import PricingCountriesResponse
from openapi_server.models.pricing_country_response import PricingCountryResponse
from openapi_server.models.retrieve_pricing_all_countries400_response import RetrievePricingAllCountries400Response
from openapi_server.models.retrieve_pricing_all_countries401_response import RetrievePricingAllCountries401Response


pytestmark = pytest.mark.asyncio

async def test_retrieve_prefix_pricing(client):
    """Test case for retrieve_prefix_pricing

    Retrieve outbound pricing for a specific dialing prefix.
    """
    params = [('api_key', 'api_key_example'),
                    ('api_secret', 'api_secret_example'),
                    ('prefix', 'prefix_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/account/get-prefix-pricing/outbound/{type}'.format(type='sms'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_pricing_all_countries(client):
    """Test case for retrieve_pricing_all_countries

    Retrieve outbound pricing for all countries.
    """
    params = [('api_key', 'api_key_example'),
                    ('api_secret', 'api_secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/account/get-full-pricing/outbound/{type}'.format(type='sms'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_pricing_country(client):
    """Test case for retrieve_pricing_country

    Retrieve outbound pricing for a specific country.
    """
    params = [('api_key', 'api_key_example'),
                    ('api_secret', 'api_secret_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/account/get-pricing/outbound/{type}'.format(type='sms'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

