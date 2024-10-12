# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body9 import RequestBody9
from openapi_server.models.sku_kit import SkuKit


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunitkit_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunitkit_delete

    Delete SKU Kit by SKU ID or Parent SKU ID
    """
    params = [('skuId', 1),
                    ('parentSkuId', 1)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunitkit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunitkit_get(client):
    """Test case for api_catalog_pvt_stockkeepingunitkit_get

    Get SKU Kit by SKU ID or Parent SKU ID
    """
    params = [('skuId', 1),
                    ('parentSkuId', 1)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/stockkeepingunitkit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunitkit_kit_id_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunitkit_kit_id_delete

    Delete SKU Kit by KitId
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunitkit/{kit_id}'.format(kit_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunitkit_kit_id_get(client):
    """Test case for api_catalog_pvt_stockkeepingunitkit_kit_id_get

    Get SKU Kit
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
        path='/api/catalog/pvt/stockkeepingunitkit/{kit_id}'.format(kit_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunitkit_post(client):
    """Test case for api_catalog_pvt_stockkeepingunitkit_post

    Create SKU Kit
    """
    body = openapi_server.RequestBody9()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/stockkeepingunitkit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

