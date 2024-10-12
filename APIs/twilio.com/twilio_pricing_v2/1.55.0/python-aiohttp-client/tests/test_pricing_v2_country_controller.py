# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_trunking_country_response import ListTrunkingCountryResponse
from openapi_server.models.list_voice_country_response import ListVoiceCountryResponse
from openapi_server.models.pricing_v2_trunking_country_instance import PricingV2TrunkingCountryInstance
from openapi_server.models.pricing_v2_voice_voice_country_instance import PricingV2VoiceVoiceCountryInstance


pytestmark = pytest.mark.asyncio

async def test_fetch_trunking_country(client):
    """Test case for fetch_trunking_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Trunking/Countries/{iso_country}'.format(iso_country='iso_country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_voice_country(client):
    """Test case for fetch_voice_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Voice/Countries/{iso_country}'.format(iso_country='iso_country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_trunking_country(client):
    """Test case for list_trunking_country

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Trunking/Countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_voice_country(client):
    """Test case for list_voice_country

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Voice/Countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

