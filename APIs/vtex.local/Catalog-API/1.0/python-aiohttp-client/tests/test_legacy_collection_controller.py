# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_collection_post200_response import ApiCatalogPvtCollectionPost200Response
from openapi_server.models.resquest_body import ResquestBody
from openapi_server.models.resquest_body1 import ResquestBody1


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_collection_collection_id_delete(client):
    """Test case for api_catalog_pvt_collection_collection_id_delete

    Delete Collection
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/collection/{collection_id}'.format(collection_id=151),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_collection_collection_id_get(client):
    """Test case for api_catalog_pvt_collection_collection_id_get

    Get Collection
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
        path='/api/catalog/pvt/collection/{collection_id}'.format(collection_id=151),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_collection_collection_id_put(client):
    """Test case for api_catalog_pvt_collection_collection_id_put

    Update Collection
    """
    body = openapi_server.ResquestBody1()
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
        path='/api/catalog/pvt/collection/{collection_id}'.format(collection_id=151),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_collection_post(client):
    """Test case for api_catalog_pvt_collection_post

    Create Collection
    """
    body = openapi_server.ResquestBody()
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
        path='/api/catalog/pvt/collection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

