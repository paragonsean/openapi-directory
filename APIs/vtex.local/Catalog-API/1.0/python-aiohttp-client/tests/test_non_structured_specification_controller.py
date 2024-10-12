# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specification_nonstructured_get200_response_inner import ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_nonstructured_delete(client):
    """Test case for api_catalog_pvt_specification_nonstructured_delete

    Delete Non Structured Specification by SKU ID
    """
    params = [('skuId', 1)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/specification/nonstructured',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_nonstructured_get(client):
    """Test case for api_catalog_pvt_specification_nonstructured_get

    Get Non Structured Specification by SKU ID
    """
    params = [('skuId', 1)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/specification/nonstructured',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_nonstructured_id_delete(client):
    """Test case for api_catalog_pvt_specification_nonstructured_id_delete

    Delete Non Structured Specification
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/specification/nonstructured/{id}'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_nonstructured_id_get(client):
    """Test case for api_catalog_pvt_specification_nonstructured_id_get

    Get Non Structured Specification by ID
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
        path='/api/catalog/pvt/specification/nonstructured/{id}'.format(id=1010),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

