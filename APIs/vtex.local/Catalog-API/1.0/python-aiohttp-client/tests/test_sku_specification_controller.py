# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_specification_post_request import ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put200_response_inner import ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put_request import ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest
from openapi_server.models.request_body import RequestBody
from openapi_server.models.sku_specification_response import SKUSpecificationResponse


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_specification_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_specification_delete

    Delete all SKU Specifications
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/specification'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_specification_get(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_specification_get

    Get SKU Specifications
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/specification'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_specification_post(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_specification_post

    Associate SKU Specification
    """
    body = openapi_server.ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest()
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/specification'.format(sku_id=1234568387),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_specification_put(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_specification_put

    Update SKU Specification
    """
    body = openapi_server.RequestBody()
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/specification'.format(sku_id=21),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_specification_specification_id_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_specification_specification_id_delete

    Delete SKU Specification
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/specification/{specification_id}'.format(sku_id=1, specification_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put

    Associate SKU specification using specification name and group name
    """
    body = openapi_server.ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest()
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/specificationvalue'.format(sku_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

