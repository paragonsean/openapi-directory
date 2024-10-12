# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_collection import CatalogCollection
from openapi_server.models.catalog_collection_data_list import CatalogCollectionDataList
from openapi_server.models.catalog_collection_item_data_list import CatalogCollectionItemDataList
from openapi_server.models.create_catalog_collection import CreateCatalogCollection
from openapi_server.models.create_catalog_collection_items import CreateCatalogCollectionItems
from openapi_server.models.remove_catalog_collection_items import RemoveCatalogCollectionItems
from openapi_server.models.update_catalog_collection import UpdateCatalogCollection


pytestmark = pytest.mark.asyncio

async def test_add_to_collection(client):
    """Test case for add_to_collection

    Add items to catalog collections
    """
    body = {"items":[{"asset":{"id":"1690105108","type":"image"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/collections/{collection_id}/items'.format(collection_id='126351028'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_collection(client):
    """Test case for create_collection

    Create catalog collections
    """
    body = {"items":[{"asset":{"id":"1690105108","type":"image"}}],"name":"New Collection","visibility":"public"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_collection(client):
    """Test case for delete_collection

    Delete catalog collections
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/catalog/collections/{collection_id}'.format(collection_id='126351028'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_from_collection(client):
    """Test case for delete_from_collection

    Remove items from catalog collection
    """
    body = {"items":[{"id":"123"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/catalog/collections/{collection_id}/items'.format(collection_id='126351028'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collections(client):
    """Test case for get_collections

    List catalog collections
    """
    params = [('page', 1),
                    ('per_page', 20),
                    ('sort', newest),
                    ('shared', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalog/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_catalog(client):
    """Test case for search_catalog

    Search catalogs for assets
    """
    params = [('sort', newest),
                    ('page', 1),
                    ('per_page', 20),
                    ('query', 'dogs on the beach'),
                    ('collection_id', ['[\"123456\",\"456789\",\"13579\"]']),
                    ('asset_type', ['[\"image\",\"editorial-image\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalog/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_collection(client):
    """Test case for update_collection

    Update collection metadata
    """
    body = {"cover_asset":{"id":"123"},"name":"My Collection","visibility":"public"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/catalog/collections/{collection_id}'.format(collection_id='126351028'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

