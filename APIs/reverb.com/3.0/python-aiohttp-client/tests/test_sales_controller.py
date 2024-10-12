# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_sales_reverb_get(client):
    """Test case for sales_reverb_get

    View upcoming and live Reverb official sales.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/sales/reverb',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_sale_id_listings_delete(client):
    """Test case for sales_sale_id_listings_delete

    Remove a listing from a sale
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/sales/{sale_id}/listings'.format(sale_id='sale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_sale_id_listings_post(client):
    """Test case for sales_sale_id_listings_post

    Add listings to a sale
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/sales/{sale_id}/listings'.format(sale_id='sale_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_seller_get(client):
    """Test case for sales_seller_get

    View your created sales.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/sales/seller',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_slug_get(client):
    """Test case for sales_slug_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/sales/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

