# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specification_post200_response import ApiCatalogPvtSpecificationPost200Response
from openapi_server.models.api_catalog_pvt_specification_post_request import ApiCatalogPvtSpecificationPostRequest
from openapi_server.models.request_body6 import RequestBody6
from openapi_server.models.request_body7 import RequestBody7


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_post(client):
    """Test case for api_catalog_pvt_specification_post

    Create Specification
    """
    body = openapi_server.ApiCatalogPvtSpecificationPostRequest()
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
        path='/api/catalog/pvt/specification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_specification_id_get(client):
    """Test case for api_catalog_pvt_specification_specification_id_get

    Get Specification
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
        path='/api/catalog/pvt/specification/{specification_id}'.format(specification_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specification_specification_id_put(client):
    """Test case for api_catalog_pvt_specification_specification_id_put

    Update Specification
    """
    body = openapi_server.RequestBody7()
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
        path='/api/catalog/pvt/specification/{specification_id}'.format(specification_id=88),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

