# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_product_id_salespolicy_get200_response_inner import ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_salespolicy_get(client):
    """Test case for api_catalog_pvt_product_product_id_salespolicy_get

    Get Trade Policies by Product ID
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
        path='/api/catalog/pvt/product/{product_id}/salespolicy'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_salespolicy_tradepolicy_id_delete(client):
    """Test case for api_catalog_pvt_product_product_id_salespolicy_tradepolicy_id_delete

    Remove Product from Trade Policy
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/product/{product_id}/salespolicy/{tradepolicy_id}'.format(product_id=1, tradepolicy_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_salespolicy_tradepolicy_id_post(client):
    """Test case for api_catalog_pvt_product_product_id_salespolicy_tradepolicy_id_post

    Associate Product with Trade Policy
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/product/{product_id}/salespolicy/{tradepolicy_id}'.format(product_id=1, tradepolicy_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_system_pvt_sku_stockkeepingunitidsbysaleschannel_get(client):
    """Test case for api_catalog_system_pvt_sku_stockkeepingunitidsbysaleschannel_get

    List all SKUs of a Trade Policy
    """
    params = [('sc', 1),
                    ('page', 1),
                    ('pageSize', 1),
                    ('onlyAssigned', true)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

