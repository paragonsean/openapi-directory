# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_search_who_bought_also_bought200_response_inner import ProductSearchWhoBoughtAlsoBought200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_product_search_accessories(client):
    """Test case for product_search_accessories

    Get Product Search of Accessories
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/accessories/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_show_together(client):
    """Test case for product_search_show_together

    Get Product Search of Show Together
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/showtogether/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_similars(client):
    """Test case for product_search_similars

    Get Product Search of Similars
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/similars/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_suggestions(client):
    """Test case for product_search_suggestions

    Get Product Search of Suggestions
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/suggestions/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_who_bought_also_bought(client):
    """Test case for product_search_who_bought_also_bought

    Get Product Search of Who Bought Also Bought
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/whoboughtalsobought/{product_id}'.format(product_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_who_saw_also_bought(client):
    """Test case for product_search_who_saw_also_bought

    Get Product Search of Who Saw Also Bought
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/whosawalsobought/{product_id}'.format(product_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_who_saw_also_saw(client):
    """Test case for product_search_who_saw_also_saw

    Get Product Search of Who Saw Also Saw
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/crossselling/whosawalsosaw/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

