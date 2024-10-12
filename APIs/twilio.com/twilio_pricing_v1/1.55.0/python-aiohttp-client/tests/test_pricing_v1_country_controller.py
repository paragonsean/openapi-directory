# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_messaging_country_response import ListMessagingCountryResponse
from openapi_server.models.list_phone_number_country_response import ListPhoneNumberCountryResponse
from openapi_server.models.list_voice_country_response import ListVoiceCountryResponse
from openapi_server.models.pricing_v1_messaging_messaging_country_instance import PricingV1MessagingMessagingCountryInstance
from openapi_server.models.pricing_v1_phone_number_phone_number_country_instance import PricingV1PhoneNumberPhoneNumberCountryInstance
from openapi_server.models.pricing_v1_voice_voice_country_instance import PricingV1VoiceVoiceCountryInstance


pytestmark = pytest.mark.asyncio

async def test_fetch_messaging_country(client):
    """Test case for fetch_messaging_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Messaging/Countries/{iso_country}'.format(iso_country='iso_country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_phone_number_country(client):
    """Test case for fetch_phone_number_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/PhoneNumbers/Countries/{iso_country}'.format(iso_country='iso_country_example'),
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
        path='/v1/Voice/Countries/{iso_country}'.format(iso_country='iso_country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_messaging_country(client):
    """Test case for list_messaging_country

    
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
        path='/v1/Messaging/Countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_phone_number_country(client):
    """Test case for list_phone_number_country

    
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
        path='/v1/PhoneNumbers/Countries',
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
        path='/v1/Voice/Countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

