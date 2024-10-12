# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_pricing_bundle_pricing_post(client):
    """Test case for pricing_bundle_pricing_post

    Bundle pricing
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/bundle-pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_competitive_pricing_post(client):
    """Test case for pricing_competitive_pricing_post

    
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/competitive-pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_cost_plus_pricing_post(client):
    """Test case for pricing_cost_plus_pricing_post

    
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/cost-plus-pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_decoy_pricing_post(client):
    """Test case for pricing_decoy_pricing_post

    
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/decoy-pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_odd_pricing_post(client):
    """Test case for pricing_odd_pricing_post

    
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/odd-pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_penetration_pricing_post(client):
    """Test case for pricing_penetration_pricing_post

    
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/penetration-pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_price_elasticity_of_demand_post(client):
    """Test case for pricing_price_elasticity_of_demand_post

    
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/pricing/price-elasticity-of-demand',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

