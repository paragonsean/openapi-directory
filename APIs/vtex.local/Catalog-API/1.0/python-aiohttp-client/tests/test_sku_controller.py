# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_stockkeepingunit_get200_response import ApiCatalogPvtStockkeepingunitGet200Response
from openapi_server.models.api_catalog_pvt_stockkeepingunit_post200_response import ApiCatalogPvtStockkeepingunitPost200Response
from openapi_server.models.api_catalog_pvt_stockkeepingunit_post_request import ApiCatalogPvtStockkeepingunitPostRequest
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_put200_response import ApiCatalogPvtStockkeepingunitSkuIdPut200Response
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_put_request import ApiCatalogPvtStockkeepingunitSkuIdPutRequest
from openapi_server.models.get_sku_alt_id import GetSKUAltID
from openapi_server.models.get_sk_uand_context import GetSKUandContext
from openapi_server.models.sku200_response import Sku200Response
from openapi_server.models.skulistby_product_id import SkulistbyProductId


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_get(client):
    """Test case for api_catalog_pvt_stockkeepingunit_get

    Get SKU by RefId
    """
    params = [('refId', '1')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/stockkeepingunit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_post(client):
    """Test case for api_catalog_pvt_stockkeepingunit_post

    Create SKU
    """
    body = openapi_server.ApiCatalogPvtStockkeepingunitPostRequest()
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
        path='/api/catalog/pvt/stockkeepingunit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_put(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_put

    Update SKU
    """
    body = openapi_server.ApiCatalogPvtStockkeepingunitSkuIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}'.format(sku_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listall_skuids(client):
    """Test case for listall_skuids

    List all SKU IDs
    """
    params = [('page', 1),
                    ('pagesize', 25)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/sku/stockkeepingunitids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sku(client):
    """Test case for sku

    Get SKU
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sku_context(client):
    """Test case for sku_context

    Get SKU and context
    """
    params = [('sc', 1)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/sku/stockkeepingunitbyid/{sku_id}'.format(sku_id=2001773),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sku_idby_ref_id(client):
    """Test case for sku_idby_ref_id

    Get SKU ID by Reference ID
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
        path='/api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/{ref_id}'.format(ref_id='0001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sku_idlistby_ref_idlist(client):
    """Test case for sku_idlistby_ref_idlist

    Retrieve SKU ID list by Reference ID list
    """
    body = ['body_example']
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
        path='/api/catalog_system/pub/sku/stockkeepingunitidsbyrefids',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skuby_alternate_id(client):
    """Test case for skuby_alternate_id

    Get SKU by Alternate ID
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
        path='/api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/{alternate_id}'.format(alternate_id=10),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skulistby_product_id(client):
    """Test case for skulistby_product_id

    Get SKU list by Product ID
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
        path='/api/catalog_system/pvt/sku/stockkeepingunitByProductId/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

