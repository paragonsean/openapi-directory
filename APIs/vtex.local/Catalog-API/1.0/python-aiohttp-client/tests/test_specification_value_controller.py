# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specificationvalue_post200_response import ApiCatalogPvtSpecificationvaluePost200Response
from openapi_server.models.api_catalog_pvt_specificationvalue_post_request import ApiCatalogPvtSpecificationvaluePostRequest
from openapi_server.models.api_catalog_pvt_specificationvalue_specification_value_id_get200_response import ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specificationvalue_post(client):
    """Test case for api_catalog_pvt_specificationvalue_post

    Create Specification Value
    """
    body = openapi_server.ApiCatalogPvtSpecificationvaluePostRequest()
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
        path='/api/catalog/pvt/specificationvalue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specificationvalue_specification_value_id_get(client):
    """Test case for api_catalog_pvt_specificationvalue_specification_value_id_get

    Get Specification Value
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
        path='/api/catalog/pvt/specificationvalue/{specification_value_id}'.format(specification_value_id=143),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specificationvalue_specification_value_id_put(client):
    """Test case for api_catalog_pvt_specificationvalue_specification_value_id_put

    Update Specification Value
    """
    body = openapi_server.ApiCatalogPvtSpecificationvaluePostRequest()
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
        path='/api/catalog/pvt/specificationvalue/{specification_value_id}'.format(specification_value_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

