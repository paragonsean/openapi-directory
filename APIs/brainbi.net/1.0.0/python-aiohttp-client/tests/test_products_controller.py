# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_beta_scrape_product_copy(client):
    """Test case for beta_scrape_product_copy

    [BETA] Scrape Product Copy
    """
    params = [('url', 'https://www.apple.com/de/shop/buy-homepod/homepod-mini')]
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/analyze/pricing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products(client):
    """Test case for products

    Products
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_products1(client):
    """Test case for products1

    Products
    """
    params = [('', '')]
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='DELETE',
        path='/api/products/1137',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

