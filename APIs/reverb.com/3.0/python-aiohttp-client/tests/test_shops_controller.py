# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_shops_id_storefronts_get(client):
    """Test case for shops_id_storefronts_get

    Get storefront details on a shop.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shops/{id}/storefronts'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shops_shop_id_shipping_profiles_get(client):
    """Test case for shops_shop_id_shipping_profiles_get

    List of shipping profiles for your shop
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/shops/{shop_id}/shipping_profiles'.format(shop_id='shop_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shops_slug_feedback_buyer_get(client):
    """Test case for shops_slug_feedback_buyer_get

    Get seller's feedback as a buyer
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shops/{slug}/feedback/buyer'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shops_slug_feedback_get(client):
    """Test case for shops_slug_feedback_get

    Get seller's feedback
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shops/{slug}/feedback'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shops_slug_feedback_seller_get(client):
    """Test case for shops_slug_feedback_seller_get

    Get seller's feedback as a seller
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shops/{slug}/feedback/seller'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shops_slug_get(client):
    """Test case for shops_slug_get

    Get details on a shop.
    """
    params = [('include_listing_count', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/shops/{slug}'.format(slug='slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

