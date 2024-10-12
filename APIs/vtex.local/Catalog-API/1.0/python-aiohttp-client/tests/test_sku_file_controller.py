# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_stockkeepingunit_copy_sku_idfrom_sku_idto_file_put200_response_inner import ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_file_get200_response_inner import ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_file_post200_response import ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response
from openapi_server.models.sku_file_url import SKUFileURL


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_copy_sku_idfrom_sku_idto_file_put(client):
    """Test case for api_catalog_pvt_stockkeepingunit_copy_sku_idfrom_sku_idto_file_put

    Copy Files from an SKU to another SKU
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog/pvt/stockkeepingunit/copy/{sku_idfrom}/{sku_idto}/file'.format(sku_idfrom=1, sku_idto=2),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_disassociate_sku_id_file_sku_file_id_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_disassociate_sku_id_file_sku_file_id_delete

    Disassociate SKU File
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/disassociate/{sku_id}/file/{sku_file_id}'.format(sku_id=1, sku_file_id=32),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_file_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_file_delete

    Delete All SKU Files
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/file'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_file_get(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_file_get

    Get SKU Files
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/file'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_catalog_pvt_stockkeepingunit_sku_id_file_post(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_file_post

    Create SKU File
    """
    body = {"Label":"Main","IsMain":True,"Text":"Nike-Red-Janoski","Url":"https://m.media-amazon.com/images/I/610G2-sJx5L._AC_UX695_.jpg","Name":"Nike-Red-Janoski-1"}
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/file'.format(sku_id=123456),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_file_sku_file_id_delete(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_file_sku_file_id_delete

    Delete SKU Image File
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/file/{sku_file_id}'.format(sku_id=1, sku_file_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_file_sku_file_id_put(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_file_sku_file_id_put

    Update SKU File
    """
    body = {"Label":"Main","IsMain":True,"Text":"Nike-Red-Janoski","Url":"https://m.media-amazon.com/images/I/610G2-sJx5L._AC_UX695_.jpg","Name":"Nike-Red-Janoski-1"}
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/file/{sku_file_id}'.format(sku_id=123456, sku_file_id=517),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

