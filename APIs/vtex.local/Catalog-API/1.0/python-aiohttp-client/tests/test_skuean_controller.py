# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_sku_alt_id import GetSKUAltID


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_ean_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_ean_delete

    Delete all SKU EAN values
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/ean'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_ean_ean_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_ean_ean_delete

    Delete SKU EAN
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/ean/{ean}'.format(sku_id=1, ean='ABC123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_ean_ean_post(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_ean_ean_post

    Create SKU EAN
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/ean/{ean}'.format(sku_id=1, ean='1234567'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_ean_get(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_ean_get

    Get EAN by SKU ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/ean'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skuby_ean(client):
    """Test case for skuby_ean

    Get SKU by EAN
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/sku/stockkeepingunitbyean/{ean}'.format(ean='1234567890123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

