# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_sk_ucomplementsbytype200_response import GetSKUcomplementsbytype200Response
from openapi_server.models.request_body2 import RequestBody2
from openapi_server.models.sku_complement_inner import SkuComplementInner


pytestmark = pytest.mark.asyncio

async def test_create_sku_complement(client):
    """Test case for create_sku_complement

    Create SKU Complement
    """
    body = openapi_server.RequestBody2()
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
        path='/api/catalog/pvt/skucomplement',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sku_complementby_sku_complement_id(client):
    """Test case for delete_sku_complementby_sku_complement_id

    Delete SKU Complement by SKU Complement ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skucomplement/{sku_complement_id}'.format(sku_complement_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sk_ucomplementsbytype(client):
    """Test case for get_sk_ucomplementsbytype

    Get SKU complements by type
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
        path='/api/catalog_system/pvt/sku/complements/{parent_sku_id}/{type}'.format(parent_sku_id=1, type=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sku_complementby_sku_complement_id(client):
    """Test case for get_sku_complementby_sku_complement_id

    Get SKU Complement by SKU Complement ID
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
        path='/api/catalog/pvt/skucomplement/{sku_complement_id}'.format(sku_complement_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sku_complementby_skuid(client):
    """Test case for get_sku_complementby_skuid

    Get SKU Complement by SKU ID
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/complement'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sku_complementsby_complement_type_id(client):
    """Test case for get_sku_complementsby_complement_type_id

    Get SKU Complements by Complement Type ID
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/complement/{complement_type_id}'.format(sku_id=1, complement_type_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

