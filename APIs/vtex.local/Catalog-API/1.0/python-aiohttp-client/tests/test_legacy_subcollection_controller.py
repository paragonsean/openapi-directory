# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_collection_collection_id_position_post_request import ApiCatalogPvtCollectionCollectionIdPositionPostRequest
from openapi_server.models.api_catalog_pvt_collection_collection_id_subcollection_get200_response_inner import ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner
from openapi_server.models.api_catalog_pvt_subcollection_post200_response import ApiCatalogPvtSubcollectionPost200Response
from openapi_server.models.api_catalog_pvt_subcollection_post_request import ApiCatalogPvtSubcollectionPostRequest
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_brand_post200_response import ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_category_post200_response import ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_put_request import ApiCatalogPvtSubcollectionSubCollectionIdPutRequest
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_post200_response import ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response
from openapi_server.models.request_body10 import RequestBody10
from openapi_server.models.request_body11 import RequestBody11
from openapi_server.models.request_body12 import RequestBody12


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_collection_collection_id_position_post(client):
    """Test case for api_catalog_pvt_collection_collection_id_position_post

    Reposition SKU on the Subcollection
    """
    body = openapi_server.ApiCatalogPvtCollectionCollectionIdPositionPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/collection/{collection_id}/position'.format(collection_id=151),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_collection_collection_id_subcollection_get(client):
    """Test case for api_catalog_pvt_collection_collection_id_subcollection_get

    Get Subcollection by Collection ID
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
        path='/api/catalog/pvt/collection/{collection_id}/subcollection'.format(collection_id=151),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_post(client):
    """Test case for api_catalog_pvt_subcollection_post

    Create Subcollection
    """
    body = openapi_server.ApiCatalogPvtSubcollectionPostRequest()
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
        path='/api/catalog/pvt/subcollection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_brand_brand_id_delete(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_brand_brand_id_delete

    Delete Brand from Subcollection
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/subcollection/{sub_collection_id}/brand/{brand_id}'.format(sub_collection_id=1, brand_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_brand_category_id_delete(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_brand_category_id_delete

    Delete Category from Subcollection
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/subcollection/{sub_collection_id}/brand/{category_id}'.format(sub_collection_id=1, category_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_brand_post(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_brand_post

    Associate Brand to Subcollection
    """
    body = openapi_server.RequestBody10()
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
        path='/api/catalog/pvt/subcollection/{sub_collection_id}/brand'.format(sub_collection_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_category_post(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_category_post

    Associate Category to Subcollection
    """
    body = openapi_server.RequestBody11()
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
        path='/api/catalog/pvt/subcollection/{sub_collection_id}/category'.format(sub_collection_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_delete(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_delete

    Delete Subcollection
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/subcollection/{sub_collection_id}'.format(sub_collection_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_get(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_get

    Get Subcollection
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
        path='/api/catalog/pvt/subcollection/{sub_collection_id}'.format(sub_collection_id=17),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_put(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_put

    Update Subcollection
    """
    body = openapi_server.ApiCatalogPvtSubcollectionSubCollectionIdPutRequest()
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
        path='/api/catalog/pvt/subcollection/{sub_collection_id}'.format(sub_collection_id=17),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_post(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_post

    Add SKU to Subcollection
    """
    body = openapi_server.RequestBody12()
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
        path='/api/catalog/pvt/subcollection/{sub_collection_id}/stockkeepingunit'.format(sub_collection_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_sku_id_delete(client):
    """Test case for api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_sku_id_delete

    Delete SKU from Subcollection
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/subcollection/{sub_collection_id}/stockkeepingunit/{sku_id}'.format(sub_collection_id=1, sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

