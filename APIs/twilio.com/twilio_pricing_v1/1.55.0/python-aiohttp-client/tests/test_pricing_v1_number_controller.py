# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pricing_v1_voice_voice_number import PricingV1VoiceVoiceNumber


pytestmark = pytest.mark.asyncio

async def test_fetch_voice_number(client):
    """Test case for fetch_voice_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/Numbers/{number}'.format(number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

