# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_product_id_specification_post200_response import ApiCatalogPvtProductProductIdSpecificationPost200Response
from openapi_server.models.api_catalog_pvt_product_product_id_specification_post_request import ApiCatalogPvtProductProductIdSpecificationPostRequest
from openapi_server.models.api_catalog_pvt_product_product_id_specificationvalue_put200_response_inner import ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner
from openapi_server.models.api_catalog_pvt_product_product_id_specificationvalue_put_request import ApiCatalogPvtProductProductIdSpecificationvaluePutRequest
from openapi_server.models.get_product_specificationby_product_id200_response_inner import GetProductSpecificationbyProductID200ResponseInner
from openapi_server.models.getor_update_product_specification import GetorUpdateProductSpecification


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_specification_post(client):
    """Test case for api_catalog_pvt_product_product_id_specification_post

    Associate Product Specification
    """
    body = openapi_server.ApiCatalogPvtProductProductIdSpecificationPostRequest()
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
        path='/api/catalog/pvt/product/{product_id}/specification'.format(product_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_specificationvalue_put(client):
    """Test case for api_catalog_pvt_product_product_id_specificationvalue_put

    Associate product specification using specification name and group name
    """
    body = openapi_server.ApiCatalogPvtProductProductIdSpecificationvaluePutRequest()
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
        path='/api/catalog/pvt/product/{product_id}/specificationvalue'.format(product_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_all_product_specifications(client):
    """Test case for delete_all_product_specifications

    Delete all Product Specifications by Product ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/product/{product_id}/specification'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deletea_product_specification(client):
    """Test case for deletea_product_specification

    Delete a specific Product Specification
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/product/{product_id}/specification/{specification_id}'.format(product_id=1, specification_id=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_specification(client):
    """Test case for get_product_specification

    Get Product Specification by Product ID
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
        path='/api/catalog_system/pvt/products/{product_id}/specification'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_specificationby_product_id(client):
    """Test case for get_product_specificationby_product_id

    Get Product Specification and its information by Product ID
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
        path='/api/catalog/pvt/product/{product_id}/specification'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_product_specification(client):
    """Test case for update_product_specification

    Update Product Specification by Product ID
    """
    body = {"Id":30,"Name":"Material","Value":["Iron","Plastic"]}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog_system/pvt/products/{product_id}/specification'.format(product_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

