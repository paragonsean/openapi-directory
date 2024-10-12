# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pricing import Pricing
from openapi_server.models.pricing_list import PricingList
from openapi_server.models.pricings_list_default_response import PricingsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_pricings_get(client):
    """Test case for pricings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/pricings/{pricing_name}'.format(subscription_id='subscription_id_example', pricing_name='pricing_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricings_list(client):
    """Test case for pricings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/pricings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricings_update(client):
    """Test case for pricings_update

    
    """
    pricing = {"properties":{"freeTrialRemainingTime":"freeTrialRemainingTime","pricingTier":"Free"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/pricings/{pricing_name}'.format(subscription_id='subscription_id_example', pricing_name='pricing_name_example'),
        headers=headers,
        json=pricing,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

