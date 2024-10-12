# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pricing_v2_trunking_number import PricingV2TrunkingNumber
from openapi_server.models.pricing_v2_voice_voice_number import PricingV2VoiceVoiceNumber


pytestmark = pytest.mark.asyncio

async def test_fetch_trunking_number(client):
    """Test case for fetch_trunking_number

    
    """
    params = [('OriginationNumber', 'origination_number_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Trunking/Numbers/{destination_number}'.format(destination_number='destination_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_voice_number(client):
    """Test case for fetch_voice_number

    
    """
    params = [('OriginationNumber', 'origination_number_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Voice/Numbers/{destination_number}'.format(destination_number='destination_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

